class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


lecturer = Lecturer("Иван", "Иванов")
reviewer = Reviewer("Пётр", "Петров")
print(isinstance(lecturer, Mentor))  # True
print(isinstance(reviewer, Mentor))  # True
print(lecturer.courses_attached)  # []
print(reviewer.courses_attached)  # []
