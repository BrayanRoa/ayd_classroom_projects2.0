

class PersonGroupDTO():
    
    def __init__(self, person_id, group_id, cancelleb, state):
        self.person_id = person_id
        self.group_id = group_id
        self.cancelled = cancelleb
        self.state = state
    