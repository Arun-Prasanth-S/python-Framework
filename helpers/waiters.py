from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pageObjects.common.base_po import BasePo


class Waiters(BasePo):
    timeout_in_seconds = 10
    
    @staticmethod
    def wait_with_sleep_timeout():
        sleep(2.5)  # Sleep for 2.5 seconds

    @staticmethod
    def wait_for_element_to_be_displayed(locator):
        WebDriverWait(Waiters.driver, Waiters.timeout_in_seconds).until(
            EC.visibility_of_element_located(locator)
        )

    @staticmethod
    def wait_for_element_to_be_visible(locator):
        WebDriverWait(Waiters.driver, Waiters.timeout_in_seconds).until(
            EC.visibility_of_element_located(locator)
        )

    @staticmethod
    def wait_for_element_to_be_clickable(locator):
        WebDriverWait(Waiters.driver, Waiters.timeout_in_seconds).until(
            EC.element_to_be_clickable(locator)
        )
