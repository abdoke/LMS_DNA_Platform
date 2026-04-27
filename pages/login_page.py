from venv import logger
from pages.base_page import BasePage
from config.settings import BASE_URL


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        #Locators
        self.username = page.locator("xpath=(//input[@name='username'])[2]")
        self.password = page.locator("xpath=(//input[@name='password'])[2]")
        self.login_btn = page.locator("xpath=(//input[@type='Submit'])[2]")
        self.login_sso = page.locator("xpath=//button[@type='button']")
        self.login_sso_text = page.locator("xpath=//span[text()='Login using SSO']")
        #self.close_popup = page.locator("xapth=//button[contains(@class, 'close') or contains(@aria-label='close')]")

    #Executing the URL in browser
    def navigate(self):
        try:
            logger.info("Launching LMS application")
            self.page.goto(f"{BASE_URL}")
        except Exception as e:
            logger.error(f"Navigation failed: {str(e)}")
            raise

    #Clicking on SSO to login
    def click_sso(self):
        try:
            self.wait_for_element(self.login_sso)
            logger.info("Clicking SSO button")
            self.login_sso.click()
        except Exception as e:
            logger.error(f"SSO click failed: {str(e)}")
            raise
    #Login with credentials
    def login(self, user, pwd):
        try:
            logger.info(f"Entering the credentials for user: {user}")
            self.wait_for_element(self.username)
            self.username.fill(user)
            self.wait_for_element(self.password)
            self.password.fill(pwd)
            self.wait_for_element(self.login_btn)
            self.login_btn.click()        
            close_popup = self.page.locator("(//button[contains(@class, 'close') or contains(@aria-label,'close')])[1]")
            close_popup.is_visible(timeout=3000)
            close_popup.first.click()
        except Exception as e:
            logger.error(f"login failed: {str(e)}")
            raise

    #logged out validation
    def validate_logged_out(self):
        try:
            logger.info("validation logged out successful")
            self.wait_for_element(self.login_sso_text)
            assert self.login_sso_text.is_visible(), "Login text not visible"
            logger.info("User logged out successfully")
        except Exception as e:
            logger.error(f"logged out validation failed: {str(e)}")
            raise
