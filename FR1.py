class Task:
    def __init__(self, title: str, description: str, priority: str, status: str, due_date: str):
        self.title       = title
        self.description = description
        self.priority    = priority
        self.status      = status
        self.due_date    = due_date
        