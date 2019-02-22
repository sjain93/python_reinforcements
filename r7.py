class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date


class ToDo:
    tasks = []
    def __init__(self, list_name):
        self.name = list_name

    @classmethod
    def add_tasks(cls, description, due_date):
        add_task = Task(description, due_date)
        cls.tasks.append(add_task)


List1 = ToDo("This week")

task1 = ToDo.add_tasks("Clean house", "Monday")
task2 = ToDo.add_tasks("Do groceries", "Tuesday")
task3 = ToDo.add_tasks("Water the cactus", "Wednesday")

print(ToDo.tasks[0].description)
