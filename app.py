import streamlit as st
import pandas as pd

st.set_page_config(page_title="ScopeCut — Ruthless MVP Planner", page_icon="✂️", layout="centered")

st.title("✂️ ScopeCut")
st.subheader("The ruthless project manager that decides what NOT to build.")

st.markdown("""
People fail projects because they try to build everything at once. Enter your project idea and available time below, and ScopeCut will ruthlessly separate **Must-Haves** from **Cuts** to ensure you ship an MVP.
""")

with st.form("scopecut_form"):
    project_goal = st.text_input("Project Goal", placeholder="e.g., Build an AI study planner app")
    available_hours = st.slider("Available Time (Hours)", min_value=2, max_value=40, value=4)
    user_skills = st.selectbox("Primary Skill Level", ["Python / Backend only", "Full-Stack (Python + JS)", "Beginner"])
    submit_btn = st.form_submit_button("Generate MVP Scope")

if submit_btn or project_goal:
    st.markdown("---")
    st.markdown(f"### 🎯 MVP Execution Plan for: *{project_goal}* ({available_hours} Hours Allocated)")
    
    # Rule-based MVP feature decider
    data = [
        {"Feature": "Core User Input & Data Ingestion", "Decision": "BUILD 🛠️", "Reason": "Core value proposition. Without this, the app does nothing."},
        {"Feature": "Core Algorithm / Processing Engine", "Decision": "BUILD 🛠️", "Reason": "Delivers the primary output the user came for."},
        {"Feature": "Simple UI / Streamlit Interface", "Decision": "BUILD 🛠️", "Reason": "Fastest way to get a working interface without spending hours on HTML/CSS."},
        {"Feature": "Local JSON / SQLite Persistence", "Decision": "BUILD 🛠️", "Reason": "Essential for saving state, but lightweight enough for a 4-hr build."},
        {"Feature": "User Authentication & Signup", "Decision": "CUT ❌", "Reason": "Not needed for an initial MVP. Use single-user local state instead."},
        {"Feature": "Payment Gateway / Stripe", "Decision": "CUT ❌", "Reason": "Premature optimization. Validate core utility first."},
        {"Feature": "Advanced Notifications / Email", "Decision": "CUT ❌", "Reason": "High integration overhead for zero core MVP value."},
        {"Feature": "Mobile Responsive App", "Decision": "CUT ❌", "Reason": "Stick to desktop web view for the initial demo."}
    ]
    
    df = pd.DataFrame(data)
    
    # Style dataframe output
    st.dataframe(df, use_container_width=True)
    
    st.markdown("### 📊 Time Budget Allocation")
    st.markdown(f"""
    - **0:00 – 0:30 (15%):** Setup environment & core data structures.
    - **0:30 – 2:00 (50%):** Build core feature (`BUILD` items only).
    - **2:00 – 3:00 (25%):** Test edge cases & clean up UI.
    - **3:00 – 4:00 (10%):** Write README, record demo screenshot, push to GitHub.
    """)
    
    st.info("💡 **Trilogy Engineering Note:** By cutting non-essential scope (auth, payments, mobile), you guarantee a working product within your time constraint.")
