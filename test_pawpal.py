from pawPal import CareTask, Pet, Owner, DailyPlan, Scheduler

#Pytest 1
def test_filter_tasks_excludes_tasks_that_dont_fit():
    # set up
    task1 = CareTask("Walk", 30, 1)
    task2 = CareTask("Bath", 50, 2)
    owner = Owner("Maria", "", 0, 60, None)
    scheduler = Scheduler(owner, [task1, task2])
    
    # call
    result = scheduler.filter_tasks()
    
    # check
    assert result == [task1]

#pytest 2
def test_filter_tasks_all_fit():
    task1 = CareTask("Walk", 20, 1)
    task2 = CareTask("Bath", 20, 2)
    owner = Owner("Maddy", "", 0, 40, None)
    scheduler = Scheduler(owner, [task1, task2])

    result = scheduler.filter_tasks()

    assert result == [task1, task2]

#pytest 3
def test_make_dailyPlan_returns_dailyplan():
    task1 = CareTask("Walk", 20, 1)
    owner = Owner("Maddy", "", 0, 30, None)
    scheduler = Scheduler(owner, [task1])
    
    result = scheduler.make_dailyPlan()
    
    assert isinstance(result, DailyPlan)

#pytest 4
def test_mark_complete_changes_status():
    task = CareTask("Walk", 30, 1)
    task.mark_complete()
    assert task.trackTask == True
    
#pytest 5
def test_add_task_increases_count():
    pet = Pet("Mochi", 3)
    task = CareTask("Walk", 30, 1)
    pet.add_task(task)
    assert len(pet.taskList) == 1