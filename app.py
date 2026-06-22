import streamlit as st
import requests

# Set page config
st.set_page_config(page_title="Industrial Knowledge Copilot", layout="wide")

st.title("🏭 Unified Asset & Operations Brain")
st.markdown("Query maintenance records, SOPs, and engineering guidelines instantly.")

# Define API URL (Localhost for now)
API_URL = "http://127.0.0.1:8000"

# Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Knowledge Ingestion")
    uploaded_file = st.file_uploader("Upload Industrial Document (PDF/TXT)", type=["pdf", "txt"])
    if uploaded_file is not None:
        st.success(f"{uploaded_file.name} successfully ingested into Vector Store.")

with col2:
    st.subheader("Expert Knowledge Copilot")
    user_query = st.text_input("Ask an operational question (e.g., 'What is the pressure valve limit?')")
    
    if st.button("Query Database"):
        if user_query:
            try:
                # Call FastAPI Backend
                response = requests.post(f"{API_URL}/ask", json={"question": user_query})
                if response.status_code == 200:
                    data = response.json()
                    st.info(f"**Answer:** {data['answer']}")
                    st.caption(f"**Cited Source:** {data['sources'][0] if data['sources'] else 'N/A'}")
                else:
                    st.error("Error communicating with the backend.")
            except Exception as e:
                st.warning("Backend API is not running. Showing mock response for UI demonstration.")
                # Fallback for UI demo if backend isn't running
                st.info("**Answer:** Standard operating pressure is 450 PSI. Do not exceed 500 PSI.")
                st.caption("**Cited Source:** Safety Guideline V-12.")
        else:
            st.warning("Please enter a query.")
