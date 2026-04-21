class BasePage:
    def __init__(self, page):
        self.page = page
    
    def wait_for_element(locator):
        locator.first.wait_for(state="visible")