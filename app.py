import streamlit as st
from pathlib import Path

st.set_page_config(page_title="SafeRoute AI", page_icon="🧭", layout="wide",
                   initial_sidebar_state="expanded")

# Load CSS
css = Path("assets/styles.css")
if css.exists():
    st.markdown(f"<style>{css.read_text()}</style>", unsafe_allow_html=True)

st.sidebar.title("🧭 SafeRoute AI")
st.sidebar.caption("Navigate Smarter. Travel With Greater Confidence.")
st.sidebar.info("Informational tool. Cannot guarantee safety. Dial **112** in emergency (India).")

st.markdown("""
<div class="hero">
<h1>SafeRoute AI</h1>
<p>Intelligent Safety Navigator — evaluate routes with transparency about data limits.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 🗺️ Plan\nEnter start & destination, compare alternatives.")
with col2:
    st.markdown("### 🛡️ Assess\nExplainable scores with confidence & missing data.")
with col3:
    st.markdown("### 🆘 SOS\nOne-tap emergency access, trusted contacts.")

st.warning("DEMO MODE: Bengaluru sample data is synthetic and labeled DEMO DATA. Not real incidents.")

st.page_link("pages/1_Route_Planner.py", label="Start Planning →", icon="🧭")

with st.expander("Data limitations"):
    st.write("- Lighting tags show mapped infrastructure, not working lamps.\n"
             "- Incident data is historical, not predictive.\n"
             "- Missing data reduces confidence, never implies safety.")
