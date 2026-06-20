class CareTask:
    def __init__(self, taskName, duration, priority):
        self.taskName = taskName
        self.duration = duration
        self.priority = priority
        self.trackTask = False

    def get_taskName(self):
        pass

    def get_duration(self):
        pass

    def get_priority(self):
        pass

    def get_trackTask(self):
        pass

    def set_taskName(self, taskName):
        pass

    def set_duration(self, duration):
        pass

    def set_priority(self, priority):
        pass

    def set_trackTask(self, trackTask):
        pass


class Pet:
    def __init__(self, petName, petAge):
        self.petName = petName
        self.petAge = petAge

    def get_petName(self):
        pass

    def get_petAge(self):
        pass


class Owner:
    def __init__(self, name, constraints, dropOffTime, pickUpTime, pet):
        self.name = name
        self.constraints = constraints
        self.dropOffTime = dropOffTime
        self.pickUpTime = pickUpTime
        self.pet = pet

    def get_name(self):
        pass

    def get_constraints(self):
        pass

    def get_dropOffTime(self):
        pass

    def get_pickUpTime(self):
        pass

    def set_dropOffTime(self, dropOffTime):
        pass

    def set_pickUpTime(self, pickUpTime):
        pass


class DailyPlan:
    def __init__(self, date):
        self.date = date
        self.taskList = []
        self.totalTime = 0

    def get_date(self):
        pass

    def get_taskList(self):
        pass

    def get_totalTime(self):
        pass

    def display_plan(self):
        pass

    def explain_task(self):
        pass


class Scheduler:
    def __init__(self, owner, availableTasks):
        self.owner = owner
        self.availableTasks = availableTasks

    def make_dailyPlan(self):
        pass

    def filter_tasks(self):
        pass
