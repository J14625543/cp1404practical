from datetime import datetime

class Project:
    def __init__(self, name, start_date_str, priority_level, cost, completion):
        self.name = name
        # Convert the date string to a date object
        self.start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
        self.priority = int(priority_level)
        self.cost_estimate = float(cost)
        self.completion_percentage = int(completion)
