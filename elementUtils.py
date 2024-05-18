from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from base_po import BasePo
from waiters import Waiters

class ElementUtils(BasePo):
    max_retry_attempts = 3

    @staticmethod
    def get_element_by_locator(locator, index=0):
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
    def get_text_by_locator(locator, index=0):
        element = ElementUtils.get_element_by_locator(locator, index)
        if element is not None:
            return element.text
        else:
            raise NoSuchElementException(f"No element found with locator '{locator}'")