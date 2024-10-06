from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

student_courses = Table('student_courses', Base.metadata,
                        Column('student_id', Integer, ForeignKey('students.id')),
                        Column('course_id', Integer, ForeignKey('courses.id'))
                        )


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    courses = relationship('Course', secondary=student_courses, back_populates='students')


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    students = relationship('Student', secondary=student_courses, back_populates='courses')


engine = create_engine('sqlite:///students.db', echo=True)

Base.metadata.create_all(engine)
