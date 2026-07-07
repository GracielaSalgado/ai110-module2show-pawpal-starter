import datetime
import streamlit as st
from pawPal import CareTask, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Time Constraints")
col_a, col_b = st.columns(2)
with col_a:
    drop_off_time = st.time_input("Drop-off time", value=datetime.time(8, 0))
with col_b:
    pick_up_time = st.time_input("Pick-up time", value=datetime.time(16, 0))

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    st.session_state.tasks.append(
        {"title": task_title, "duration_minutes": int(duration), "priority": priority}
    )

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    # Step 1: create owner
    drop_off_minutes = drop_off_time.hour * 60 + drop_off_time.minute
    pick_up_minutes = pick_up_time.hour * 60 + pick_up_time.minute

    if pick_up_minutes <= drop_off_minutes:
        st.error("Pick-up time must be after drop-off time.")
        st.stop()

    owner = Owner(owner_name, "", drop_off_minutes, pick_up_minutes, None)

    # Step 2: create care tasks from session state
    care_tasks = []
    for task in st.session_state.tasks:
        t = CareTask(task["title"], task["duration_minutes"], task["priority"])
        care_tasks.append(t)
    
    # Step 3: create scheduler and generate plan
    scheduler = Scheduler(owner, care_tasks)
    plan = scheduler.make_dailyPlan()
    
    # Step 4: display
    st.write(plan.display_plan())
    st.write(plan.explain_task())

