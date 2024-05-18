from selenium.webdriver.common.by import By
from helpers.action import Actions
from pageObjects.common.base_po import BasePo
from helpers.elementUtils import ElementUtils
from enums.enums import FormEnum
from helpers.dataProviders import DataProvider
from helpers.waiters import Waiters  # Ensure the Enum is adapted to Python

class HomePage(BasePo):
    def __init__(self, driver):
        self.driver = driver  # Assuming driver is managed in BasePo

    def header_item(self, item_name):
        headerBy =(By.XPATH, f"//a[text()='{item_name}']")
        return headerBy

    def contact_form(self, formname):
        return (By.NAME, formname)
    header =(By.XPATH, "//a[text()='Our Story']")
    contact_button = (By.CSS_SELECTOR, "button[data-target='.toggle-163701']")
    submit_button = (By.NAME, "form_page_submit")
    error_message = (By.CSS_SELECTOR, ".ff-form-errors")

    def open_landing_page(self):
        self.driver.get(DataProvider.get_url_test_data("tendableUrl"))

    def get_current_url(self):
        return self.driver.current_url

    def click_on_header_menu_button(self, item_name):
        print(ElementUtils.get_text_by_locator(self.header))

        Waiters.wait_for_element_to_be_displayed(self.header_item(item_name))
        
        Actions.click_by_locator(self.header)

    def get_request_demo_button(self, item_name):
        return ElementUtils.get_element_by_locator(self.header_item(item_name))

    def click_on_contact_button(self):
        Actions.click_by_locator(self.contact_button)

    def type_contact_us_form(self, field_name, text):
        Actions.clear_text_in_locator_and_type_text(self.contact_form(field_name), text)

    def select_job_role_by_name(self, option):
        Actions.click_select_dropdown_by_locator(self.contact_form(FormEnum.JobRole.get_value()), option)

    def click_on_submit_button(self):
        Actions.click_by_locator(self.submit_button)

    def get_error_message(self):
        return ElementUtils.get_element_by_locator(self.error_message)
