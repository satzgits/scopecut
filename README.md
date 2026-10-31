# ScopeCut ✂️

> **The ruthless project manager that decides what NOT to build.**

ScopeCut is a lightweight productivity tool designed to combat scope creep. When starting new projects with limited time (e.g., a 4-hour hackathon or MVP sprint), developers and students often get overwhelmed trying to build too much. ScopeCut evaluates your project goal and available hours, then ruthlessly separates essential MVP features from non-essential distractions.

---

## 🚀 The Problem
People start projects with ambitious goals but limited time. They don't know what to build first, what to cut, or what a realistic MVP looks like. Most tools are task generators; ScopeCut is a decision-making tool that tells you what **NOT** to build.

---

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Interface:** Streamlit
- **Logic:** Deterministic rule-based feature prioritization engine

---

## ⚙️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/satzgits/scopecut.git
   cd scopecut
   ```

2. Install dependencies:
   ```bash
   pip install streamlit pandas
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## 💡 Key Design Decisions
- **Why Streamlit?** Allowed building a fully functional interactive UI in under 15 minutes without heavy frontend boilerplate.
- **Why Rule-Based Cut/Keep?** Deterministic scoping prevents hallucinated feature bloat and gives immediate, actionable trade-offs.
