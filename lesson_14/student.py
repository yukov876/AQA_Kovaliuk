class Student:
    def __init__(self, name: str, surname: str, age: int, average_score: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def change_score(self):
        decision = input(print("Do you want to change student's average score? (input 'Yes' or 'No')"))
        if decision == 'Yes':
            new_average_score = 100
        else:
            new_average_score = our_student.average_score
        return f"Our student's name is {our_student.name}, surname is {our_student.surname}, age is {our_student.age}, average score is {new_average_score}"


# оголошення об*єкту
our_student: Student = Student('Olha', 'Ilko', 22, 98)



print(our_student.change_score())
