class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_stud(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lec:
                lecturer.grades_lec[course] += [grade]
            else:
                lecturer.grades_lec[course] = [grade]
        else:
            return 'Ошибка'

    def avg(self):
        count = 0
        for gradeskey in self.grades:
            count += len(self.grades[gradeskey])
        self.avg = round((sum(map(sum, self.grades.values())) / count), 2)
        return self.avg

    def __str__(self):
        res = f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашнее задание: {self.avg()}
Курсы в процессе изучения: {','.join(self.courses_in_progress)}
Завершенные курсы: {','.join(self.finished_courses)}
        """
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Студент не найден!')
            return
        return self.average_hw() < other.average_hw()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lec = {}

    def avg_lec(self):
        count = 0
        for gradval in self.grades_lec:
            count += len(self.grades_lec[gradval])
        self.avg_lec = round((sum(map(sum, self.grades_lec.values())) / count), 2)
        return self.avg_lec

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_lec()}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Лектор с такой фамилией отсутствует')
            return
        return self.ave_lec() < other.ave_lec()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_rev(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


lecturer_1 = Lecturer('Jon', 'Marly')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Herold', 'Hero')
lecturer_2.courses_attached += ['JS']

lecturer_3 = Lecturer('Steave', 'Jobs')
lecturer_3.courses_attached += ['Django']

student_1 = Student('Roy', 'Eminem', 'male')
student_1.courses_in_progress += ['Python', 'JS', 'Django']
student_1.finished_courses += ['Английский для программистов']
student_1.rate_stud(lecturer_1, 'Python', 5)
student_1.rate_stud(lecturer_2, 'JS', 7)
student_1.rate_stud(lecturer_3, 'Django', 3)

student_2 = Student('Nikola', 'Tesla', 'male')
student_2.courses_in_progress += ['Python', 'JS', 'Django']
student_2.finished_courses += ['Английский для программистов']
student_2.rate_stud(lecturer_1, 'Python', 2)
student_2.rate_stud(lecturer_2, 'JS', 4)
student_2.rate_stud(lecturer_3, 'Django', 9)

reviewer_1 = Reviewer('Donald', 'Trump')
reviewer_1.courses_attached += ['Python']
reviewer_1.rate_rev(student_1, 'Python', 7)
reviewer_1.rate_rev(student_2, 'Python', 3)

reviewer_2 = Reviewer('Vladimir', 'Putin')
reviewer_2.courses_attached += ['JS', 'Django']
reviewer_2.rate_rev(student_1, 'JS', 9)
reviewer_2.rate_rev(student_1, 'Django', 3)
reviewer_2.rate_rev(student_2, 'JS', 8)
reviewer_2.rate_rev(student_2, 'Django', 7.6)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2, lecturer_3]


def all_student(student_list, course):
    all_grade_stud = []
    for student in student_list:
        for course_key in student.grades.keys():
            if course == course_key:
                all_grade_stud.append(student.grades[course_key])
    return sum(sum(all_grade_stud, [])) / len(sum(all_grade_stud, []))


def all_lerturer(lecturer_list, course):
    all_grade_lec = []
    for lecturer in lecturer_list:
        for course_key in lecturer.grades_lec.keys():
            if course == course_key:
                all_grade_lec.append(lecturer.grades_lec[course_key])
    return sum(sum(all_grade_lec, [])) / len(sum(all_grade_lec, []))


print(student_1)
print(lecturer_1)
print(reviewer_1)
print(all_student(student_list, 'JS'))
print(all_lerturer(lecturer_list, 'JS'))