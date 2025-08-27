import os
import pytest
from pages.portal_login_page import PortalLoginPage
from pages.portal_dashboard_page import PortalDashboardPage

BASE_URL = os.getenv("BASE_URL")

@pytest.mark.smoke
def test_valid_login(driver):
    driver.get(BASE_URL)
    login_page = PortalLoginPage(driver)
    login_page.login(os.getenv("PATIENT_USERNAME"), os.getenv("PATIENT_PASSWORD"), os.getenv("PATIENT_EMAIL"))

    dashboard = PortalDashboardPage(driver)
    assert dashboard.is_logged_in(), "Patient should be logged in successfully"