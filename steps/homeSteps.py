from basePackage import BasePo
from enums import HeaderMenuItemsEnum, ContactDetailsEnum, FormEnum, JobRoleEnum
from helpers import Assertions, DataProviders, StepUtils, StringUtils
from pages.homePage import HomePage

class HomeSteps(BasePo):
    def __init__(self, driver):
        self.homepage = HomePage(driver)

    def user_lands_on_home_page(self):
        self.homepage.open_landing_page()

    def click_on_menu_item(self, item):
        self.homepage.click_on_header_menu_button(HeaderMenuItemsEnum[item].value)
        StepUtils.add_log(f"The User clicks on the {item} button")

    def assert_menu_item(self, item):
        base_url = DataProviders.get_url_test_data("tendableUrl")
        final_url = base_url + HeaderMenuItemsEnum[item].value
        expected_url = StringUtils.replace_all_string_for_value(
            StringUtils.get_string_to_lower_case(final_url), " ", "-"
        )
        Assertions.expect_to_equal(
            self.homepage.get_current_url(),
            expected_url,
            f"URL does not contain expected text for {item}"
        )
        StepUtils.add_log(f"The {item} webpage is opened")

    def assert_request_demo_button(self, item):
        Assertions.expect_to_display(
            self.homepage.get_request_demo_button(item),
            f"Request a Demo button is not displayed on {item}"
        )
        Assertions.expect_to_be_enabled(
            self.homepage.get_request_demo_button(item),
            f"Request a Demo button is disabled on {item}"
        )
        StepUtils.add_log("The demo button is active and displayed")

    def fill_contact_form(self, field_name, text):
        self.homepage.type_contact_us_form(FormEnum[field_name].value, ContactDetailsEnum[text].value)
        StepUtils.add_log(f"The user types {ContactDetailsEnum[text].value} in the {FormEnum[field_name].value} field")

    def clicking_on_contact_button(self):
        self.homepage.click_on_contact_button()
        StepUtils.add_log("The User clicks on the contact button")

    def select_job_role_in_drop_down(self, option):
        self.homepage.select_job_role_by_name(JobRoleEnum[option].value)
        StepUtils.add_log(f"The user selects {JobRoleEnum[option].value} option from the job role dropdown")

    def clicking_on_submit_button(self):
        self.homepage.click_on_submit_button()
        StepUtils.add_log("The user clicks on the submit button")

    def asserting_error_message(self):
        Assertions.expect_to_display(self.homepage.get_error_message(), "Error message is not displayed")
        StepUtils.add_log("Error message is displayed")
