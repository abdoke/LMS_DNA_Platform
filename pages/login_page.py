from venv import logger

from config.settings import BASE_URL


class LoginPage:
    def __init__(self, page):
        self.page = page
        
        #Locators
        self.username = "(//input[@name='username'])[2]"
        self.password = "(//input[@name='password'])[2]"
        self.login_btn = "(//input[@type='Submit'])[2]"
        self.login_sso = "//button[@type='button']"

    def navigate(self):
        logger.info("launching application LMS")
        self.page.goto(f"{BASE_URL}")

    def click_sso(self):
        self.page.click(self.login_sso)
        
    def login(self, user, pwd):
        logger.info("Entering the credentiuals for user"+ user)
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_btn)
