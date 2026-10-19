import streamlit as st
import folium
from streamlit_folium import st_folium
from services.geocoding import geocode
from services.routing import get_routes

st.title("🧭 Route Planner")

start_q = st.text_input("Start", "Hassan")
end_q = st.text_input("Destination", "Electronic City, Bengaluru")
mode = st.selectbox("Travel mode", ["Walking","Cycling","Driving"])

if st.button("Find Routes", type="primary"):
    s, e = geocode(start_q), geocode(end_q)
    if not s or not e:
        st.error("Could not geocode one or both locations.")
        st.session_state["routes"] = None
        st.session_state["coords"] = None
    else:
        routes = get_routes((s[0],s[1]), (e[0],e[1]))
        st.session_state["routes"] = routes
        st.session_state["coords"] = (s, e)
        st.success(f"Found {len(routes)} route(s)")

# --- Render map OUTSIDE button, from session_state ---
if st.session_state.get("routes"):
    routes = st.session_state["routes"]
    s, e = st.session_state["coords"]
    
    m = folium.Map(location=[s[0], s[1]], zoom_start=11)
    folium.Marker([s[0], s[1]], tooltip="Start", icon=folium.Icon(color="green")).add_to(m)
    folium.Marker([e[0], e[1]], tooltip="End", icon=folium.Icon(color="red")).add_to(m)
    
    colors = ["#00D4FF","#16C784","#F59E0B"]
    for i, r in enumerate(routes):
        pts = [(lat, lon) for lon, lat in r["geometry"]]
        folium.PolyLine(pts, color=colors[i%3], weight=5,
                        tooltip=f"Route {i+1}").add_to(m)
    
    # IMPORTANT: fixed key prevents flicker
    st_folium(m, height=500, use_container_width=True, key="main_map")
