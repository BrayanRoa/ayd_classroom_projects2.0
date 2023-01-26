class TaskDTO():
    
    def __init__(self, name, description, expired_date, state, group_id) -> None:
        self.name = name
        self.description = description
        self.expired_date = expired_date
        self.state = state
        self.group_id = group_id
