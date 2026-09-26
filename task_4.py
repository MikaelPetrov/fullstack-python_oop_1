class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __str__(self):
        avg_grade = self._calc_avg_grade()

        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}"
        return res

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

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
        if self._is_valid(course, student):
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
        if self._is_valid(course, lecturer):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"


reviewer = Reviewer("Some", "Buddy")

lecturer1 = Lecturer("Some", "Buddy")
lecturer1.grades = {"Python": [10, 9], "Java": [10]}
lecturer2 = Lecturer("Another", "Lecturer")
lecturer2.grades = {"Python": [10, 7], "Java": [8]}

student1 = Student("Ruoy", "Eman", "M")
student1.grades = {"Python": [10, 9], "Java": [10]}
student1.courses_in_progress += ["Python", "Java"]
student1.finished_courses += ["Git"]
student2 = Student("Some", "Body", "F")
student2.grades = {"Python": [8, 7], "Java": [8]}
student2.courses_in_progress += ["Python", "Java"]
student2.finished_courses += ["Git"]


def avg_grade_all_students(students_list, course_name):
    all_grades = []

    for student in students_list:
        if isinstance(student, Student) and course_name in student.grades:
            all_grades.extend(student.grades[course_name])

    if not all_grades:
        return f"Нет оценок по курсу '{course_name}'"

    return sum(all_grades) / len(all_grades)


def avg_grade_all_lecturers(lecturers_list, course_name):
    all_grades = []

    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])

    if not all_grades:
        return f"Нет оценок по курсу '{course_name}'"

    return sum(all_grades) / len(all_grades)


avg_students_python = avg_grade_all_students([student1, student2], "Python")
avg_lecturers_python = avg_grade_all_lecturers([lecturer1, lecturer2], "Python")

print(f"Средняя оценка всех студентов по курсу 'Python': {avg_students_python:.1f}")
print(f"Средняя оценка всех лекторов по курсу 'Python': {avg_lecturers_python:.1f}")
