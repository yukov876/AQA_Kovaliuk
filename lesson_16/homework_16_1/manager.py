from lesson_16.homework_16_1.employee import Employee


class Manager(Employee):
    department: str

    def __init__(self, name: str, salary: int, department: str):
        super().__init__(name, salary)
        self.department = department

    @property
    def get_name(self):
        return self._name

    @property
    def get_salary(self):
        return self._salary