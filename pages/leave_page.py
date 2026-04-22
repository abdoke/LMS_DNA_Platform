import time
from venv import logger
from playwright.sync_api import Page, expect
from conftest import page
from pages.base_page import BasePage

class LeavePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        #Locators
        self.profile_icon = page.locator("xpath=//span[@class='custom-avatar-string']")
        self.page_title = page.locator("xpath=//h1[contains(text()='LEAVE MANAGEMENT TOOL']")
        self.heading = page.locator("xpath=//h3[text()='Leave Summary']")
        self.leave_categories = page.locator("xpath=//h3[text()='Leave Summary']/following::div[contains(@class,'legend-label')]")
        self.leave_category_counts = page.locator("xpath=//div[@class='legend-value']")
        self.user_email = page.locator("xpath=//p[text()='hashedintestuser108@deloitte.com']")
        self.user_role = page.locator("xpath=//p[text()='Quality Engineer-I']")
        self.user_emp_id = page.locator("xpath=//p[contains(text(),'Emp Id')]")
        self.side_panel_option = page.locator("xpath=//li[@role='menuitem']")
        self.user_icon = page.locator ("xpath=//div[@class='user-profile-container']")
        self.apply_leave_click = page.locator("xpath=//span[text()='Apply Leave']")
        self.side_panel_options = page.locator("xpath=//li[@role='menuitem']")

        self.leave_type_dropdown = page.locator("xpath=(//div[contains(@class, 'ant-select-selector')])[1]")
        self.leave_type_option = page.locator("xpath=(//div[@class='ant-select-item-option-content'])[4]")
        self.start_date = page.locator("//input[@placeholder='Start Date']")
        self.end_date = page.locator("//input[@placeholder='End Date']")
        self.reason_input = page.locator("//textarea[@placeholder='Input details']")
        self.apply_button = page.locator("//button[.//span[text()='Apply']]")
        self.sucess_popup = page.locator("css=.toast-success")

    #Validation for login
    def validation_login_success(self):
        try:
            logger.info("Validating the login success")
            #self.page.wait_for_load_state("netwokidle")
            self.user_icon.first.wait_for(state="visible")
            self.wait_for_element(self.user_icon)
            expect(self.user_icon).to_be_visible(timeout=10000)
            logger.info("login successful")
        except Exception as e:
            logger.error(f"Login validation failed: {str(e)}")
            raise

    #Validation for user redirected to home page
    def validate_redirection_to_LMS_dashboard(self):
        try:
            logger.info("Validating redirection to LMS dashboard")
            self.page_title.first.wait_for(state="visible")
            self.wait_for_element(self.page_title)
            expect(self.page_title).to_contain_text("LEAVE MANAGEMENT TOOL")
            logger.info(f"User redirected successfully: {self.page_title.inner_text()}")
        except Exception as e:
            logger.error(f"Redirection validation failed: {str(e)}")
            raise

    #Validation of header
    def validate_heading_displayed(self):
        try:
            logger.info("Validation leave summary heading")
            self.wait_for_element(self.heading)
            expect(self.heading).to_be_visible() 
            expect(self.heading).to_have_text("Leave Summary")
            logger.info(f"Heading validated: {self.heading.inner_text()}")
        except Exception as e:
            logger.error(f"Heading validation failed: {str(e)}")
            raise
        
    #Validation of leave categories count
    def validate_leave_categories_count(self):
        try:
            logger.info("Validating leave category count")
            self.leave_categories.first.wait_for(state="visible")
            self.wait_for_element(self.leave_categories)
            count = self.leave_categories.count()
            logger.info(f"Total categoeries: {count}")
            return count
        except Exception as e:
            logger.error(f"Category count validation failed: {str(e)}")
            raise

    #Print details
    def print_leave_details(self):
        try:
            logger.info("Printing leave details")
            self.wait_for_element(self.leave_categories)
            count = self.leave_categories.count()
            for i in range(count):
                category = self.leave_categories.nth(i).inner_text()
                value = self.leave_category_counts.nth(i).inner_text()
                logger.info(f"{category} : {value}")
        except Exception as e:
            logger.error(f"Failed to print leave details: {str(e)}")
            raise

    #Click on profile
    def click_profile(self):
        try:
            logger.info("Clicking on profile icon")
            self.wait_for_element(self.user_icon)
            self.user_icon.click()
        except Exception as e:
            logger.error(f"Failed to click profile: {str(e)}")
            raise

    #Validation of user
    def user_validation(self):
        try:
            logger.info("Validating user details")
            self.wait_for_element(self.user_email)
            self.wait_for_element(self.user_role)
            self.wait_for_element(self.user_emp_id)
            logger.info(f"Email: {self.user_email.inner_text()}")
            logger.info(f"Role: {self.user_role.inner_text()}")
            logger.info(f"Emp_Id: {self.user_emp_id.inner_text()}")
            return {
                "email": self.user_email.inner_text(),
                "role": self.user_role.inner_text(),
                "emp_id": self.user_emp_id.inner_text()
            }
        except Exception as e:
            logger.error(f"User validation failed: {str(e)}")
            raise
    
    #Count side options
    def get_side_option_count(self):
        try:
            logger.info("Verifying the side options count")
            self.wait_for_element(self.side_panel_option)
            locals.__init__(f"Side panel option count: {self.side_panel_option.count()}")
            return self.side_panel_option.count()
        except Exception as e:
            logger.error(f"Side option count validation failed: {str(e)}")
            raise
    
    #Click on apply leave
    def click_apply_leave(self):
        try:
            logger.info("Click on apply leave")
            self.wait_for_element(self.apply_leave)
            self.apply_leave.click()
        except Exception as e:
            logger.error(f"Click apply leave failed: {str(e)}")
            raise

    #Apply for leave
    def apply_leave(self,  reason="Leave Test"):
        try:
            logger.info("Applying for leave")
            self.apply_leave_click.click()
            self.leave_type_dropdown.first.wait_for(state="visible")
            self.wait_for_element(self.leave_type_dropdown)
            self.leave_type_dropdown.click()
            self.leave_type_option.click()
            
            #Need to update
            """
            #self.start_date.click()
            self.start_date.click()
            nxt_btn = page.locator("//button[@aria-label='Next month (PageDown)']")
            while True:
                month = self.page.locator(".ant-picker-month-btn").inner_text()
                if month.strip() == "Nov":
                    break
                nxt_btn.click()
            self.page.locator("//div[text()='18']").click()

            time.sleep(2)
            #self.end_date.click()
            self.end_date.fill("2026-11-19")
            page.self.end_date.press("Enter")
            time.sleep(2)
            #self.reason_input.click()
            self.reason_input.fill(reason)
            time.sleep(2)
            """
            logger.info("Leave applied successfully")
        except Exception as e:
                logger.error(f"applying leave failed: {str(e)}")
                raise


        

        