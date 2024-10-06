from sqlalchemy.orm import sessionmaker

from lesson_22.students_data_model import engine, Course, Student

Session = sessionmaker(bind=engine)
session = Session()


def add_student_to_course(first_name, last_name, course_name):
    course = session.query(Course).filter_by(name=course_name).first()

    if not course:
        print(f"Курс з назвою '{course_name}' не знайдено.")
        return

    new_student = Student(first_name=first_name, last_name=last_name)

    new_student.courses.append(course)

    session.add(new_student)

    session.commit()

    print(f"Студент {first_name} {last_name} був доданий до курсу '{course_name}'.")

    added_student = session.query(Student).filter_by(first_name=first_name, last_name=last_name).first()

    if added_student:
        print(f"Студента {added_student.first_name} {added_student.last_name} було успішно додано до бази даних.")
    else:
        print(f"Студента {first_name} {last_name} не було додано до бази даних.")

    registered_courses = added_student.courses
    if course in registered_courses:
        print(f"Студент {first_name} {last_name} було успішно додано на курс '{course_name}'.")
    else:
        print(f"Студента {first_name} {last_name} не вдалося додати на курс '{course_name}'.")
