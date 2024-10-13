import time
from assertpy import assert_that
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from lesson_26.conftest import web_driver_creation


class TestFrameVerification:
    BASE_URL: str = "http://localhost:8000/dz.html"

    def test_verify_frame1(self, web_driver_creation):
        web_driver_creation.get(self.BASE_URL)

        web_driver_creation.switch_to.frame("frame1")

        input_field: WebElement = web_driver_creation.find_element(By.ID, "input1")
        input_field.click()
        input_field.send_keys("Frame1_Secret")

        verify_button: WebElement = web_driver_creation.find_element(By.XPATH, "//button[text()='Перевірити']")
        verify_button.click()

        time.sleep(2)
        alert = Alert(web_driver_creation)
        alert_text = alert.text
        alert.accept()

        assert_that(alert_text).is_equal_to("Верифікація пройшла успішно!")

        web_driver_creation.switch_to.default_content()

    def test_verify_frame2(self, web_driver_creation):
        web_driver_creation.get(self.BASE_URL)

        web_driver_creation.switch_to.frame("frame2")

        input_field: WebElement = web_driver_creation.find_element(By.ID, "input2")
        input_field.click()
        input_field.send_keys("Frame2_Secret")

        verify_button: WebElement = web_driver_creation.find_element(By.XPATH, "//button[text()='Перевірити']")
        verify_button.click()

        time.sleep(2)
        alert = Alert(web_driver_creation)
        alert_text = alert.text
        alert.accept()

        assert_that(alert_text).is_equal_to("Верифікація пройшла успішно!")

        web_driver_creation.switch_to.default_content()
