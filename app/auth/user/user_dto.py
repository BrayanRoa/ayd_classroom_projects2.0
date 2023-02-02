

class UserDtO():
    
    def __init__(self, institutional_mail, role) -> None:
        self.institutional_mail = institutional_mail
        self.role = role
    
    def __str__(self):
        return {"email": self.institutional_mail, "role": self.role}