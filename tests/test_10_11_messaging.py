import os
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.portal_login_page import PortalLoginPage
from pages.portal_dashboard_page import PortalDashboardPage
from pages.portal_messaging_page import PortalMessagingPage

BASE_URL = os.getenv("BASE_URL")
TIMEOUT = int(os.getenv("TIMEOUT"))

@pytest.mark.regression
@pytest.mark.tc10
def test_send_message(driver):
    driver.get(BASE_URL)
    login_page = PortalLoginPage(driver)
    login_page.login(os.getenv("PATIENT_USERNAME"), os.getenv("PATIENT_PASSWORD"), os.getenv("PATIENT_EMAIL"))
    
    dashboard = PortalDashboardPage(driver)
    dashboard.go_to("messaging")
    
    messages = PortalMessagingPage(driver)
    messages.wait_for_message_page_to_load()
    
    # Step A: get sent count before
    before_count = messages.get_sent_count()
    
    #Step B: send the message
    messages.send_message()
    
    # Step C: wait for the modal to close and for refresh
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(*PortalMessagingPage.MESSAGE_IFRAME))
    WebDriverWait(driver, 15).until(
        lambda d: messages.get_sent_count() > before_count
    )
    
    after_count = messages.get_sent_count()
    
    driver.switch_to.default_content()
    
    assert after_count > before_count, f"Sent count did not increase: before={before_count}, after={after_count}"
    
@pytest.mark.regression
@pytest.mark.tc11
def test_view_messages(driver):
    driver.get(BASE_URL)
    login_page = PortalLoginPage(driver)
    login_page.login(os.getenv("PATIENT_USERNAME"), os.getenv("PATIENT_PASSWORD"), os.getenv("PATIENT_EMAIL"))
    
    dashboard = PortalDashboardPage(driver)
    dashboard.go_to("messaging")
    
    messages = PortalMessagingPage(driver)
    messages.wait_for_message_page_to_load()
    
    all_count = messages.get_all_count()
    
    messages.view_all_messages()
    row_count = messages.count_message_rows()
    
    assert row_count == all_count, f"Mismatch: badge says {all_count}, table has {row_count}"