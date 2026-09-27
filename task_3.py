class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self._calc_avg_grade()

        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calc_avg_grade() < other._calc_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calc_avg_grade() == other._calc_avg_grade()

    def _calc_avg_grade(self):
        if not self.grades:
            return 0

        all_grades = [g for v in self.grades.values() for g in v]
        return (sum(all_grades) / len(all_grades)) if all_grades else 0


class Reviewer(Mentor):
    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res

    def _is_valid(self, course, student):
        return (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        )

    def rate_hw(self, student, course, grade):
        if self._is_valid(course, student) and 0 < grade < 11:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        avg_grade = self._calc_avg_grade()

        in_progress = (
            ", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет"
        )
        finished = ", ".join(self.finished_courses) if self.finished_courses else "Нет"

        res = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
            f"Курсы в процессе изучения: {in_progress}\n"
            f"Завершенные курсы: {finished}"
        )
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calc_avg_grade() < other._calc_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calc_avg_grade() == other._calc_avg_grade()

    def _calc_avg_grade(self):
        if not self.grades:
            return 0

        all_grades = [g for v in self.grades.values() for g in v]
        return (sum(all_grades) / len(all_grades)) if all_grades else 0

    def _is_valid(self, course, lecturer):
        return (
            isinstance(lecturer, Lecturer)
            and course in lecturer.courses_attached
            and course in self.courses_in_progress
        )

    def rate_lecture(self, lecturer, course, grade):
        if self._is_valid(course, lecturer) and 0 < grade < 11:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"


reviewer = Reviewer("Some", "Buddy")
lecturer = Lecturer("Some", "Buddy")
student = Student("Ruoy", "Eman", "M")

reviewer.courses_attached += ["Python", "Git"]
lecturer.courses_attached += ["Python", "Java"]
student.courses_in_progress += ["Python", "Java"]
student.finished_courses += ["Git"]

student.rate_lecture(lecturer, "Python", 10)
student.rate_lecture(lecturer, "Python", 9)
student.rate_lecture(lecturer, "Java", 10)

reviewer.rate_hw(student, "Python", 10)
reviewer.rate_hw(student, "Python", 9)
reviewer.rate_hw(student, "Java", 10)


print(reviewer)
print(lecturer)
print(student)
