import pytest
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright
import allure

# params=["chromium","firefox","edge"]
@pytest.fixture(params=["chromium"],scope="function")
def browser(request):
 browser_type = request.param

 with sync_playwright() as p:
     if browser_type == "firefox":
          browser = p.firefox.launch(headless=False)
     elif browser_type == "chromium":
          browser = p.chromium.launch(channel="chrome",headless=False)
     elif browser_type =="edge":
          browser = p.chromium.launch(channel="msedge",headless=False)
     else:
         raise ValueError("Unsupported Browser input")
     yield browser
     browser.close()

@pytest.fixture(scope="function")
def page(browser):
 context = browser.new_context()
 page = context.new_page()
 page.set_viewport_size({"width": 1920, "height": 1080})
 yield page
 page.close()

# @pytest.fixture(autouse=True)
# def set_up_function(page):
#     page.goto("https://advantageonlineshopping.com/")

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(page.screenshot(path="screenshot/failureScreenshot.png"), name="Failed screenshot",
                      attachment_type=AttachmentType.PNG)




