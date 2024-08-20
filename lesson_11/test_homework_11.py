import unittest

from lesson_11.homework_11 import log_event


class MyTest(unittest.TestCase):

    def test_logging_info(self):
        username = 'First_user'
        status = 'success'
        log_event(username, status)
        with open('login_system.log') as file:
            last_line = file.readlines()[-1]
            needed_log_info = last_line[(last_line.find('Login event')):-1]
        self.assertEqual(needed_log_info, f'Login event - Username: {username}, Status: {status}')

    def test_logging_warning(self):
        username = 'Second_user'
        status = 'expired'
        log_event(username, status)
        with open('login_system.log') as file:
            last_line = file.readlines()[-1]
            needed_log_info = last_line[(last_line.find('Login event')):-1]
        self.assertEqual(needed_log_info, f'Login event - Username: {username}, Status: {status}')

    def test_logging_error(self):
        username = 'Third_user'
        status = 'failed'
        log_event(username, status)
        with open('login_system.log') as file:
            last_line = file.readlines()[-1]
            needed_log_info = last_line[(last_line.find('Login event')):-1]
        self.assertEqual(needed_log_info, f'Login event - Username: {username}, Status: {status}')
