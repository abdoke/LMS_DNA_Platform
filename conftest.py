import pytest
import logging
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utils.test_data import TestData

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        
        #Launcing the browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function")
def login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.click_sso()
    login_page.login(TestData.USERNAME, TestData.PASSWORD)
    return page