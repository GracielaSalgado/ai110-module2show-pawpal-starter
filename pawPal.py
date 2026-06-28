class CareTask:
    def __init__(self, taskName, duration, priority):
        self.taskName = taskName
        self.duration = duration
        self.priority = priority
        self.trackTask = False

    def get_taskName(self):
        return self.taskName

    def get_duration(self):
        return self.duration

    def get_priority(self):
        return self.priority

    def get_trackTask(self):
        return self.trackTask

    def set_taskName(self, taskName):
        self.taskName = taskName

    def set_duration(self, duration):
        self.duration = duration

    def set_priority(self, priority):
        self.priority = priority

    def set_trackTask(self, trackTask):
        self.trackTask = trackTask

    def mark_complete(self):
        """Marks the task as complete by setting trackTask to True"""
        self.trackTask = True


class Pet:
    def __init__(self, petName, petAge):
        self.petName = petName
        self.petAge = petAge
        self.taskList = []

    def get_petName(self):
        return self.petName

    def get_petAge(self):
        return self.petAge

    def add_task(self, task):
        self.taskList.append(task)

class Owner:
    def __init__(self, name, constraints, dropOffTime, pickUpTime, pet):
        self.name = name
        self.constraints = constraints
        self.dropOffTime = dropOffTime
        self.pickUpTime = pickUpTime
        self.pet = pet

    def get_name(self):
        return self.name

    def get_constraints(self):
        return self.constraints

    def get_dropOffTime(self):
        return self.dropOffTime

    def get_pickUpTime(self):
        return self.pickUpTime

    def set_dropOffTime(self, dropOffTime):
        self.dropOffTime = dropOffTime

    def set_pickUpTime(self, pickUpTime):
        self.pickUpTime = pickUpTime


class DailyPlan:
    def __init__(self, date):
        self.date = date
        self.taskList = []
        self.totalTime = 0

    def get_date(self):
        return self.date

    def get_taskList(self):
        return self.taskList

    def get_totalTime(self):
        return self.totalTime

    def display_plan(self):
        result = ""
        for plan in self.taskList:
            result += "\n- " + plan.taskName + " | priority: " + str(plan.priority)
        return result

    def explain_task(self):
        result = "Scheduled " + str(len(self.taskList)) + " tasks totaling " + str(self.totalTime) + " minutes."
        return result

    def add_task(self, task):
        self.taskList.append(task)
        self.totalTime += task.duration


class Scheduler:
    def __init__(self, owner, availableTasks):
        self.owner = owner
        self.availableTasks = availableTasks

    def make_dailyPlan(self):
        plan = DailyPlan("2026-06-20")
        tasks = self.filter_tasks() 
        for task in tasks:
            plan.add_task(task)
        return plan

    """returns only the tasks that fit within the owner's avaliablity"""
    def filter_tasks(self):
        available_time = self.owner.pickUpTime - self.owner.dropOffTime
        filtered = []
        time_used = 0

        sorted_tasks = sorted(self.availableTasks, key=lambda task: task.priority)
        for task in self.availableTasks:
            if time_used + task.duration <= available_time:
                filtered.append(task)
                time_used += task.duration

        return filtered

    def detect_conflicts(self):
        available_time = self.owner.pickUpTime - self.owner.dropOffTime
        total = sum(task.duration for task in self.availableTasks)
        if total > available_time:
            return f"Warning: tasks total {total} min but only {available_time} min available."
        return None

