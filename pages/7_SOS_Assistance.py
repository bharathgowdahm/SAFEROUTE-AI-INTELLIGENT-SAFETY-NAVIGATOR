
import streamlit as st
from services.emergency_service import sos_actions

st.title("🆘 SOS Assistance")
a = sos_actions()
st.error("In immediate danger, call your local emergency number now.")
st.markdown(f"### India Emergency: [{a['emergency_number']}]({a['dial_link']})")
st.caption(a["note"])
confirm = st.checkbox("I understand this opens my phone dialer and does not auto-send alerts.")
if st.button("📞 Open Dialer (112)", disabled=not confirm, type="primary"):
    st.markdown(f'<meta http-equiv="refresh" content="0;url={a["dial_link"]}">',
                unsafe_allow_html=True)
    st.info("If the dialer did not open, manually dial 112.")
st.warning("Streamlit Cloud cannot provide background tracking or guaranteed dispatch.")
