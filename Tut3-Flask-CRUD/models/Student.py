class Student:
    def __init__(self):
        pass

    def __init__(self, id, name, dateOfBirth, address):
        self.id = id
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.address = address

    def __init__(self, name, dateOfBirth, address):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.address = address

    def __str__(self) -> str:
        return super().__str__()
