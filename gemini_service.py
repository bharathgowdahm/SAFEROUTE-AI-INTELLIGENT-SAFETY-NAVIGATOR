import os, streamlit as st

def explain_routes(route_summaries: str):
    key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", "")
    if not key:
        return ("AI unavailable (no API key). Compare manually: check distance, "
                "lighting coverage, and data confidence for each route.")
    try:
        import google.generativeai as genai
        genai.configure(api_key=key)
        m = genai.GenerativeModel("gemini-1.5-flash")
        prompt = (f"Explain these route options factually, do not invent incidents or lighting. "
                  f"Data:\n{route_summaries}\nKeep under 150 words.")
        return m.generate_content(prompt).text
    except Exception as e:
        return f"AI temporarily unavailable: {e}"
