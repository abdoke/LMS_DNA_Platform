from venv import logger
from pages.login_page import LoginPage
from pages.leave_page import LeavePage
from utils.test_data import TestData

def test_valid_login(page):
    logger.info("++++++++++Test case: Login validation started executing++++++++++")
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.click_sso()
    login_page.login(TestData.USERNAME, TestData.PASSWORD)
    
    #Validation for home screen
    leave_page = LeavePage(page)
    #leave_page.close_popup()
    leave_page.validation_login_success()
    #leave_page.validate_redirection_to_LMS_dashboard()
    leave_page.validate_heading_displayed()
    logger.info("Test case completed")
