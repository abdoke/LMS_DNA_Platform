from venv import logger

class BasePage:
    def __init__(self, page):
        self.page = page
    
    def wait_for_element(self, locator, timeout=10000):
        try:
            if hasattr(locator, "wait_for"):
                element = locator
            else:
                element = self.page.locator(locator)
            element.first.wait_for(
                state="visible", 
                timeout=timeout
                )
        except Exception as e:
            logger.error(f"Element not visible: {locator} | Error: {str(e)}")
            raise
