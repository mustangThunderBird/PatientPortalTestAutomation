import os
import pytest
from pages.portal_login_page import PortalLoginPage
from pages.portal_dashboard_page import PortalDashboardPage

BASE_URL = os.getenv("BASE_URL")

@pytest.mark.smoke
@pytest.mark.tc01
def test_valid_login(driver):
    driver.get(BASE_URL)
    login_page = PortalLoginPage(driver)
    login_page.login(os.getenv("PATIENT_USERNAME"), os.getenv("PATIENT_PASSWORD"), os.getenv("PATIENT_EMAIL"))

    dashboard = PortalDashboardPage(driver)
    assert dashboard.is_logged_in(), "Patient should be logged in successfully"
    
@pytest.mark.smoke
@pytest.mark.tc02
def test_invalid_login(driver):
    driver.get(BASE_URL)
    login_page = PortalLoginPage(driver)
    login_page.login("invalid_user", "wrong_password", os.getenv("PATIENT_EMAIL"))

    assert login_page.is_alert_displayed(), "Alert should be displayed for invalid login"
    
@pytest.mark.smoke
@pytest.mark.tc03
def test_logout(driver):
    driver.get(BASE_URL)
    login_page = PortalLoginPage(driver)
    login_page.login(os.getenv("PATIENT_USERNAME"), os.getenv("PATIENT_PASSWORD"), os.getenv("PATIENT_EMAIL"))
    
    dashboard = PortalDashboardPage(driver)
    dashboard.logout()
    
    assert dashboard.is_logged_out(), "Patient should be logged out successfully"