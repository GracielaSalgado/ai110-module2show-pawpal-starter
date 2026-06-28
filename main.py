from pawPal import Owner, Pet, CareTask, DailyPlan, Scheduler

owner = Owner("Maria", "Sephi", 0, 500, None)

task1 = CareTask("Morning Walk", 30, 1)
task2 = CareTask("Bath", 20, 2)
task3 = CareTask("Snack", 10, 3)
task4 = CareTask("Walk Again", 0, 4)
care_tasks = [task1, task2, task3, task4]


scheduler = Scheduler(owner, care_tasks)
plan = scheduler.make_dailyPlan()

print("Today's Schedule: ")
print(plan.display_plan())
print(plan.explain_task())

conflicts = scheduler.detect_conflicts()
if conflicts:
    print("Warning: conflicts detected for:", conflicts)
else:
    print("No conflicts detected.")
