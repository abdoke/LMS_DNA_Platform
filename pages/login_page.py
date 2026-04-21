from venv import logger
from pages.base_page import BasePage
from config.settings import BASE_URL


class LoginPage(BasePage):
    def __init__(self, page):
        self.page = page
        
        #Locators
        self.username = "(//input[@name='username'])[2]"
        self.password = "(//input[@name='password'])[2]"
        self.login_btn = "(//input[@type='Submit'])[2]"
        self.login_sso = "//button[@type='button']"

    #Executing the URL in browser
    def navigate(self):
        logger.info("launching application LMS")
        self.page.goto(f"{BASE_URL}")

    #Clicking on SSO to login
    def click_sso(self):
        self.page.click(self.login_sso)
        
    #Login with credentials
    def login(self, user, pwd):
        logger.info("Entering the credentials for user"+ user)
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_btn)
