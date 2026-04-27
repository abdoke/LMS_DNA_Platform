
import time
from venv import logger
from playwright.sync_api import Page
from pages.base_page import BasePage

class TrackerPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        #Locators
        self.filter = page.locator("xpath=//button[@aria-label='Open filters']")
        self.leaves = page.locator("xpath=//span[text()='Leaves']")
        self.apply = page.locator("xpath=//span[text()='Apply']")
        self.date = page.locator("xpath=(//div[text()='18 Nov - 19 Nov'])")
        self.cancel = self.date.locator("xpath=(//span[text()='Cancel'])")
        self.type = page.locator("xpath=(//span[@aria-label='collapsed'])")
        self.confirm = page.locator("xpath=(//span[text()='Confirm'])")

        self.wfh = page.locator("xpath=//span[text()='Work from Home']")
        self.wfh_date = page.locator("xpath=(//div[text()='11 Nov - 12 Nov'])")
        self.wfh_cancel = self.wfh_date.locator("xpath=(//span[text()='Cancel'])")

    def click_filter(self):
        try:
            logger.info("Clicking on filter")
            self.wait_for_element(self.filter)
            self.filter.click()
            self.type.click()
        except Exception as e:
            logger.error(f"Failed to click filter: {str(e)}")
            raise
    
    def click_leaves(self):
        try:
            logger.info("Clicking on leaves checkbox")
            self.wait_for_element(self.leaves)
            self.leaves.click()
            time.sleep(2)
        except Exception as e:
            logger.error(f"Failed to click leaves: {str(e)}")
            raise
    def click_wfh(self):
        try:
            logger.info("Clicking on wfh checkbox")
            self.wait_for_element(self.wfh)
            self.wfh.click()
            time.sleep(2)
        except Exception as e:
            logger.error(f"Failed to click wfh: {str(e)}")
            raise

    def click_apply(self):
        try:
            logger.info("Clicking on apply button")
            self.wait_for_element(self.apply)
            self.apply.click()
        except Exception as e:
            logger.error(f"Failed to click apply: {str(e)}")
            raise

    def click_cancel(self):
        try:
            logger.info("Clicking on cancel")
            self.wait_for_element(self.cancel)
            self.cancel.click()
            time.sleep(2)
        except Exception as e:
            logger.error(f"Failed to cancel leave: {str(e)}")
            raise

    def click_confirm(self):
        try:
            logger.info("Clicking on confirm pop up")
            self.wait_for_element(self.confirm)
            self.confirm.click()
            time.sleep(2)
            logger.info("Leave cancelled successfully")
        except Exception as e:
            logger.error(f"Failed to click confirm: {str(e)}")
            raise

    def click_wfh_cancel(self):
        try:
            logger.info("Clicking on wfh cancel")
            self.wait_for_element(self.wfh_cancel)
            self.wfh_cancel.click()
            time.sleep(2)
        except Exception as e:
            logger.error(f"Failed to cancel wfh: {str(e)}")
            raise
    
    