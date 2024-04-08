from selenium.webdriver.common.by import By
from basePackage import BasePo  # Make sure to have your BasePo class adapted to Python
from helpers import Action, ElementUtils, Waiters  # Ensure these helper classes are adapted to Python
from helpers import DataProviders  # Assuming DataProviders is adapted to Python for getting URL test data
from enums import FormEnum  # Ensure the Enum is adapted to Python

class HomePage(BasePo):
    def __init__(self, driver):
        self.driver = driver  # Assuming driver is managed in BasePo

    def header_item(self, item_name):
        return By.LINK_TEXT, item_name

    def contact_form(self, formname):
        return By.NAME, formname

    contact_button = (By.CSS_SELECTOR, "button[data-target='.toggle-163701']")
    submit_button = (By.NAME, "form_page_submit")
    error_message = (By.CSS_SELECTOR, ".ff-form-errors")

    def open_landing_page(self):
        self.driver.get(DataProviders.get_url_test_data("tendableUrl"))

    def get_current_url(self):
        return self.driver.current_url

    def click_on_header_menu_button(self, item_name):
        Waiters.wait_for_element_to_be_displayed(self.header_item(item_name))
        Action.click_by_locator(self.header_item(item_name), 0)

    def get_request_demo_button(self, item_name):
        return ElementUtils.get_element_by_locator(self.header_item(item_name), 0)

    def click_on_contact_button(self):
        Action.click_by_locator(self.contact_button, 0)

    def type_contact_us_form(self, field_name, text):
        Action.clear_text_in_locator_and_type_text(self.contact_form(field_name), text, 0)

    def select_job_role_by_name(self, option):
        Action.click_select_dropdown_by_locator(self.contact_form(FormEnum.JobRole.get_value()), option, 0)

    def click_on_submit_button(self):
        Action.click_by_locator(self.submit_button, 0)

    def get_error_message(self):
        return ElementUtils.get_element_by_locator(self.error_message, 0)
