# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

```
Today's Schedule:

- Morning Walk | priority: 1
- Bath | priority: 2
- Snack | priority: 3
Scheduled 3 tasks totaling 60 minutes.
No conflicts detected.
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest
```

Sample test output:

```
platform darwin -- Python 3.13.0, pytest-9.1.1, pluggy-1.6.0
collected 5 items

test_pawpal.py .....                                    [100%]

5 passed in 0.01s
```

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `filter_tasks()` | Sorts by priority before scheduling |
| Filtering | `filter_tasks()` | Skips tasks if owner's time runs out |
| Conflict handling | `detect_conflicts()` | Warns if total task time exceeds available time |
| Recurring tasks | not yet implemented | |

## 📸 Demo Walkthrough

1. Enter your name and pet name in the input fields
2. Add tasks using the Task form (title, duration, priority)
3. Click "Generate schedule" to run the scheduler
4. View the scheduled tasks and explanation in the output
5. Tasks are automatically sorted by priority and filtered to fit your available time
