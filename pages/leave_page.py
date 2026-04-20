from venv import logger

from playwright.sync_api import Page, expect

class LeavePage:

    def __init__(self, page: Page):
        self.page = page

        #Locators
        #self.profile_icon = page.locator("//span[text()='hashedintestuser109LastN, hashedintestuser109FirstN'], .profile_icon")
        self.profile_icon = page.locator("//span[@class='custom-avatar-string']")
        self.page_title = page.locator("//h1[text()='LEAVE MANAGEMENT TOOL']")
        self.heading = page.locator("//h3[text()='Leave Summary']")

    #def close_popup(self):
        #popup_close = self.page.locator("//div[@class='ot-close-cntr']")
        #popup_close = self.page.locator("//button[@id='close-pc-btn-handler']")
        #popup_close.first.wait_for(state="visible", timeout=5000)
        #popup_close.first.click()

    #Validation
    def validation_login_success(self):
        logger.info("Validating the user login successful")
        expect(self.profile_icon).to_be_visible(timeout=10000)

    def validate_redirection_to_LMS_dashboard(self):
        #expect(self.page).to_have_url(lambda url: "/dashboard" in url)
        #expect(self.page_title).to_be_visible()
        expect(self.page_title).to_contain_text("LEAVE MANAGEMENT TOOL")
        logger.info("User redirected to Leave Management Tool")

    def validate_heading_displayed(self):
        expect(self.heading).to_be_visible() 
        expect(self.heading).to_have_text("Leave Summary")
        logger.info("Validated the Leave Summary Heading")

        

        