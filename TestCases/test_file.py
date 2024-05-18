import pytest
from pageObjects.common.base_po import BasePo
from enums.enums import ContactDetailsEnum, FormEnum, HeaderMenuItemsEnum, JobRoleEnum
from stepFile.homeSteps import HomeSteps


@pytest.fixture(scope="class")
def setup():
    driver = BasePo.browser_launch()
    yield driver# This allows the test setup to execute before the test
    BasePo.close_browser()

@pytest.mark.usefixtures("setup")
class Test1(BasePo):
    def test_top_level_menu_accessibility(self):
        driver = self.driver 
        home_steps = HomeSteps(driver)
        home_steps.user_lands_on_home_page()
        for item in [HeaderMenuItemsEnum.OurStory, HeaderMenuItemsEnum.OurSolution, HeaderMenuItemsEnum.WhyTendableWithSpecialCharacter]:
            home_steps.click_on_menu_item("Our Story")

    def test_request_a_demo_button_presence_and_is_active(self):
        self.home_steps.user_lands_on_home_page()
        for item in [HeaderMenuItemsEnum.OurSolution, HeaderMenuItemsEnum.OurStory, HeaderMenuItemsEnum.WhyTendableWithSpecialCharacter]:
            self.home_steps.click_on_menu_item(item.name)
            self.home_steps.assert_request_demo_button(HeaderMenuItemsEnum.RequestADemo.value)

    def test_contact_us_form_submission(self):
        self.home_steps.user_lands_on_home_page()
        self.home_steps.click_on_menu_item(HeaderMenuItemsEnum.ContactUs.name)
        self.home_steps.clicking_on_contact_button()
        self.home_steps.fill_contact_form(FormEnum.FullName.name, ContactDetailsEnum.FullName.name)
        self.home_steps.fill_contact_form(FormEnum.OrganisationName.name, ContactDetailsEnum.OrganisationName.name)
        self.home_steps.fill_contact_form(FormEnum.CellPhone.name, ContactDetailsEnum.CellPhone.name)
        self.home_steps.fill_contact_form(FormEnum.Email.name, ContactDetailsEnum.Email.name)
        self.home_steps.select_job_role_in_drop_down(JobRoleEnum.Management.name)
        self.home_steps.clicking_on_submit_button()
        self.home_steps.asserting_error_message()
