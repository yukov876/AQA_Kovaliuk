from lesson_16.homework_16_1.teamLead import TeamLead
from assertpy import assert_that


class TestEmployee:
    qa_automation_team_lead: TeamLead = TeamLead("Olha", 7000, "Main Test Department", 20)

    expected_olha_attrs: dict[str, object] = {
        "name": "Olha",
        "salary": 7000,
        "department": "Main Test Department",
        "team_size": 20
    }

    def test_employee_attrs(self):
        print(self.qa_automation_team_lead.__dict__)
        (assert_that(self.qa_automation_team_lead.__dict__,
                     "Desired user's attrs are not equal to desired dict of attributes")
         .is_equal_to(self.expected_olha_attrs))
