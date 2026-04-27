from venv import logger
from playwright.sync_api import Page
from pages.base_page import BasePage

class HolidayCalender(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        #locators
        self.holiday_calender_heading = page.locator("xpath=//h1[text()='Holiday Calendar']")
        self.months = page.locator("xpath=//div[@data-testid='month-card']")
    
    def fetch_leave_details(self):
        try:
            logger.info("Fetching leave details")
            count = self.months.count()
            for i in range(count):
                month = self.months.nth(i)
                month_name = month.locator("xpath=.//div/span").first.inner_text().strip()
                print(f"\n {month_name}")
                logger.info(month_name)
                leaves = month.locator("xpath=.//div[@data-testid='smart-image']/ancestor::div[2]")
                if leaves.count()==0:
                    print("No holidays")
                    continue
                for j in range(leaves.count()):
                    leave = leaves.nth(j)
                    text = leave.inner_text().strip()
                    print(text)
                    logger.info(text)
            logger.info("leave details fetched successful")
        except Exception as e:
            logger.error(f"Failed to fetch leave details: {str(e)}")
            raise