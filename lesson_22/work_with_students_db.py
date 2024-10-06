from lesson_22.add_student_course import session
from lesson_22.students_data_model import Course, Student


def get_students_by_course(course_name):
    course = session.query(Course).filter_by(name=course_name).first()
    if not course:
        print(f"Курс з назвою '{course_name}' не знайдено.")
        return

    students = course.students
    if students:
        print(f"Студенти, котрі були зареєстровані на курс з назвою '{course_name}' це:")
        for student in students:
            print(f"{student.first_name} {student.last_name}")
    else:
        print(f"На курс із назвою '{course_name}' нікого не зареєстровано.")


def get_courses_by_student(first_name, last_name):
    student = session.query(Student).filter_by(first_name=first_name, last_name=last_name).first()
    if not student:
        print(f"Студента {first_name} {last_name} не знайдено.")
        return

    courses = student.courses
    if courses:
        print(f"Курси, на які було додано студента {first_name} {last_name} це:")
        for course in courses:
            print(course.name)
    else:
        print(f"Студент {first_name} {last_name} поки що не зареєструвався на жоден курс.")


def update_student(student_id, new_first_name=None, new_last_name=None):
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        print(f"Студента з ID {student_id} не знайдено у базі даних.")
        return

    if new_first_name:
        student.first_name = new_first_name
    if new_last_name:
        student.last_name = new_last_name

    session.commit()
    print(f"Дані студента з ID {student_id} успішно оновлено в базі даних.")


def delete_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        print(f"Студента з ID {student_id} не знайдено у базі даних.")
        return

    session.delete(student)
    session.commit()
    print(f"Студента з ID {student_id} успішно видалено з бази даних.")
