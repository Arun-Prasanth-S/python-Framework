from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from basePackage import BasePo  # Assuming BasePo is converted to Python and saved as base_po.py
from waiters import Waiters  # Ensure Waiters is adapted to Python and available

class ElementUtils(BasePo):
    max_retry_attempts = 3

    @staticmethod
    def get_element_by_locator(locator, index):
        last_exception = None
        for retry_count in range(ElementUtils.max_retry_attempts):
            try:
                page_elements = ElementUtils.driver.find_elements(locator)
                if len(page_elements) > index:
                    return page_elements[index]
            except NoSuchElementException as e:
                last_exception = e
                Waiters.wait_with_sleep_timeout()
        raise Exception(f"Unable to get locator '{locator}' after {ElementUtils.max_retry_attempts} retries") from last_exception

    @staticmethod
    def get_text_by_locator(locator, index):
        element = ElementUtils.get_element_by_locator(locator, index)
        return element.text
