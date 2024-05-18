from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from pageObjects.common.base_po import BasePo
from helpers.elementUtils import ElementUtils
from helpers.waiters import Waiters
 

class Actions(BasePo):
    max_retry_attempts = 3

    @staticmethod
    def clear_text_in_locator_and_type_text(locator, text, index):
        # Assuming implementation of Waiters.waitForElementToBeVisible & ElementUtils.getElementByLocator
        element = Waiters.wait_for_element_to_be_visible(locator)
        element = ElementUtils.get_element_by_locator(locator, index)
        element.clear()
        element.send_keys(text)

    @staticmethod
    def click_by_locator(locator, index = 0):
        # Assuming implementation of ElementUtils.getElementByLocator
        page_element = ElementUtils.get_element_by_locator(locator, index)
        retry_count = 0

        while retry_count < Actions.max_retry_attempts:
            try:
                # Assuming implementation of Waiters.waitForElementToBeVisible & .waitForElementToBeClickable
                Waiters.wait_for_element_to_be_visible(locator)
                Waiters.wait_for_element_to_be_clickable(locator)
                ActionChains(Actions.driver).move_to_element(page_element).click().perform()
                break
            except Exception as e:
                retry_count += 1
                if retry_count >= Actions.max_retry_attempts:
                    raise Exception(f"{str(e)}. Unable to click on locator '{locator}' after '{retry_count}' retries")

    @staticmethod
    def click_select_dropdown_by_locator(locator, value, index):
        # Assuming implementation of ElementUtils.getElementByLocator
        element = ElementUtils.get_element_by_locator(locator, index)
        # Assuming implementation of Waiters.waitForElementToBeClickable
        Waiters.wait_for_element_to_be_clickable(locator)
        dropdown = Select(element)
        dropdown.select_by_value(value)
