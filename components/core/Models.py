class User:
    def __init__(self, userName, password, auth, email):
        self.userName=userName
        self.password=password
        self.auth=auth
        self.email=email

class AuthLeval:
    ADMIN, STUDENT, ACADEMIC, NONACADEMIC= range(4)

class Download:
    def __init__(self, link, userName):
        self.link=link
        self.userName=userName

class Status:

    DEFAULT, STARTED, DELETED, COMPLETED, ERROR= range(5)