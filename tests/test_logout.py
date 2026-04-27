from venv import logger

from pages.login_page import LoginPage
from pages.leave_page import LeavePage

def test_logout(login):
    logger.info("++++++++++Test case: Logout validation started executing++++++++++")
    leave_page =LeavePage(login)

    logger.info("logging out")
    leave_page.click_profile()
    leave_page.click_logout_option()

    login_page= LoginPage(login)
    login_page.validate_logged_out()