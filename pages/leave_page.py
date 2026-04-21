from venv import logger
from playwright.sync_api import Page, expect

class LeavePage:
    def __init__(self, page: Page):
        self.page = page

        #Locators
        self.profile_icon = page.locator("//span[@class='custom-avatar-string']")
        self.page_title = page.locator("//h1[text()='LEAVE MANAGEMENT TOOL']")
        self.heading = page.locator("//h3[text()='Leave Summary']")
        self.leave_categories = page.locator("//h3[text()='Leave Summary']/following::div[contains(@class,'legend-label')]")
        self.leave_category_counts = page.locator("//div[@class='legend-value']")
        self.user_email = page.locator("//p[text()='hashedintestuser108@deloitte.com']")
        self.user_role = page.locator("//p[text()='Quality Engineer-I']")
        self.emp_id = page.locator("//p[contains(text(),'Emp Id')]")
        self.side_panel_option = page.locator("//li[@role='menuitem']")
        self.user_icon = page.locator("//div[@class='user-profile-container']")
        self.apply_leave = page.locator("//span[text()='Apply Leave']")

    #Validation for login
    def validation_login_success(self):
        logger.info("Validating the user login successful")
        self.user_icon.first.wait_for(state="visible")
        expect(self.user_icon).to_be_visible(timeout=10000)

    #Validation for user redirected to home page
    def validate_redirection_to_LMS_dashboard(self):
        expect(self.page_title).to_contain_text("LEAVE MANAGEMENT TOOL")
        print("User redirected to home page:" + self.page_title.inner_text())
        #logger.info("User redirected to Leave Management Tool")

    #Validation of header
    def validate_heading_displayed(self):
        expect(self.heading).to_be_visible() 
        expect(self.heading).to_have_text("Leave Summary")
        print("Validated the heading: " + self.heading.inner_text())
        #logger.info("Validated the Leave Summary Heading")
    
    #Validation of leave categories count
    def validate_leave_categories_count(self):
        logger.info("Verifying total category count")
        self.leave_categories.first.wait_for(state="visible")
        return self.leave_categories.count()
    
    #Print details
    def print_leave_details(self):
        logger.info("Printing details")
        count = self.leave_categories.count()
        for i in range(count):
            category = self.leave_categories.nth(i).inner_text()
            self.leave_category_counts.first.wait_for(state="visible")
            value = self.leave_category_counts.nth(i).inner_text()
            logger.info(f"{category} : {value}")

    #Click on profile
    def click_profile(self):
        self.user_icon.click()

    #Validation of user
    def user_validation(self):
        logger.info("Started user validation")
        print("Email: " + self.user_email.inner_text() + "\n" + "Role: " + self.user_role.inner_text() + "\n" + "Emp_id" + self.emp_id.inner_text())
        return {
            "email": self.user_email.inner_text(),
            "role": self.user_role.inner_text(),
            "emp_id": self.emp_id.inner_text()
        }
    
    #Count side options
    def get_side_option_count(self):
        logger.info("Verifying the side options count")
        return self.page.locator("//li[@role='menuitem']").count()
    
    #Click on apply leave
    def click_apply_leave(self):
        self.apply_leave.click()

    #Pop up handling method
    #def close_popup(self):
        #popup_close = self.page.locator("//div[@class='ot-close-cntr']")
        #popup_close = self.page.locator("//button[@id='close-pc-btn-handler']")
        #popup_close.first.wait_for(state="visible", timeout=5000)
        #popup_close.first.click()

        

        