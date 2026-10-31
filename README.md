# ScopeCut

ScopeCut is a lightweight project planning tool built to solve a common engineering failure mode: scope creep during short-term builds and hackathons. 

When developers start new projects with strict time limits (such as a 4-hour MVP sprint), they frequently overestimate what can be achieved. Instead of focusing on core value delivery, they spend valuable time building non-essential scaffolding like user authentication, payment integrations, or complex UI styling. ScopeCut acts as an automated product manager that evaluates project goals against time constraints and enforces strict feature prioritization.

---

## The Problem

Most project planners and task trackers assume that every requested feature is equally important and simply generate an endless list of to-dos. This often leads to incomplete projects because the developer runs out of time before finishing the core functionality. 

Developers need a tool that actively helps them make trade-offs: deciding what must be built for a working minimum viable product (MVP) versus what should be deliberately cut.

---

## How It Works

1. **Input Collection:** The user inputs their project goal, available time in hours, and technical constraints.
2. **Deterministic Evaluation:** A rule-based prioritization engine categorizes requested features into essential MVP components (`BUILD`) and premature optimizations (`CUT`).
3. **Time Budgeting:** The system generates a structured timeline allocating specific percentage blocks for environment setup, core development, testing, and documentation.

---

## Technical Stack

- **Language:** Python
- **Interface:** Streamlit
- **Data Persistence:** JSON / Local State

---

## Architectural Decisions & Trade-Offs

- **Why Streamlit?** Chosen to minimize frontend boilerplate, allowing rapid iteration on core decision logic rather than CSS styling.
- **Deterministic vs. LLM Scoping:** While LLMs can brainstorm features, a deterministic priority engine ensures consistent, predictable scoping decisions without hallucinations or bloated feature suggestions.

---

## Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/satzgits/scopecut.git
   cd scopecut
   ```

2. Install dependencies:
   ```bash
   pip install streamlit pandas
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```
