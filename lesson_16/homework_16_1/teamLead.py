from lesson_16.homework_16_1.manager import Manager
from lesson_16.homework_16_1.testEngineer import TestEngineer


class TeamLead(Manager, TestEngineer):

    team_size: int

    def __init__(self, name: str, salary: int, department: str, team_size: int):
        super().__init__(name, salary, department)
        self.team_size = team_size
