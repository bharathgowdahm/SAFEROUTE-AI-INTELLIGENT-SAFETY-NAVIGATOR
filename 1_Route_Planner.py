import streamlit as st
from services.geocoding import geocode
from services.routing import get_routes
from services.safety_scoring import score_route
import folium
from streamlit_folium import st_folium

st.title("🧭 Route Planner")
c1, c2 = st.columns(2)
start_q = c1.text_input("Start", "MG Road, Bengaluru")
end_q = c2.text_input("Destination", "Electronic City, Bengaluru")
mode = st.selectbox("Travel mode", ["Walking","Cycling","Driving"])

if st.button("Find Routes", type="primary"):
    s, e = geocode(start_q), geocode(end_q)
    if not s or not e:
        st.error("Could not geocode one or both locations. Try a more specific address.")
    else:
        routes = get_routes((s[0],s[1]), (e[0],e[1]))
        if not routes:
            st.warning("No routes available.")
        else:
            st.session_state["routes"] = routes
            st.success(f"Found {len(routes)} route(s) via {routes[0].get('source','')}")
            m = folium.Map(location=[s[0],s[1]], zoom_start=12)
            folium.Marker([s[0],s[1]], tooltip="Start").add_to(m)
            folium.Marker([e[0],e[1]], tooltip="End").add_to(m)
            colors = ["#00D4FF","#16C784","#F59E0B"]
            for i, r in enumerate(routes):
                pts = [(lat, lon) for lon, lat in r["geometry"]]
                folium.PolyLine(pts, color=colors[i%3], weight=5,
                    tooltip=f"Route {i+1}: {r['distance_m']/1000:.1f} km").add_to(m)
            st_folium(m, height=450, use_container_width=True)
            for i, r in enumerate(routes):
                with st.expander(f"Route {i+1} — {r['distance_m']/1000:.1f} km, {r['duration_s']/60:.0f} min"):
                    demo_ind = {"lighting":(0.6,0.5),"incidents":(None,0),
                        "road_condition":(0.7,0.4),"ped_infra":(0.5,0.4),
                        "community":(None,0),"crossing":(0.6,0.3)}
                    sc = score_route(demo_ind)
                    st.metric("Assessment", sc["score"] or sc["label"])
                    st.caption(f"Confidence: {sc['confidence']} | Missing: {', '.join(sc['missing'])}")
                    for reason in sc["reasons"]: st.write("- "+reason)
