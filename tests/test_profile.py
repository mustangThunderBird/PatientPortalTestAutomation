import os
import pytest
from pages.portal_login_page import PortalLoginPage
from pages.portal_dashboard_page import PortalDashboardPage
from pages.portal_profile_page import PortalProfilePage

BASE_URL = os.getenv("BASE_URL")
TIMEOUT = int(os.getenv("TIMEOUT"))

@pytest.mark.regression
@pytest.mark.tc04
def test_demographics_presence(driver):
    driver.get(BASE_URL)
    login_page = PortalLoginPage(driver)
    login_page.login(os.getenv("PATIENT_USERNAME"), os.getenv("PATIENT_PASSWORD"), os.getenv("PATIENT_EMAIL"))

    dashboard = PortalDashboardPage(driver)
    dashboard.go_to("profile")

    profile = PortalProfilePage(driver)
    profile.wait_until_visible(timeout=TIMEOUT)
    assert profile.is_profile_visible(), "Profile card should be expanded"
    assert profile.demographics_present(), "Demographics fields should not be empty"
    
@pytest.mark.regression
@pytest.mark.tc05
def test_dob_format(driver):
    driver.get(BASE_URL)
    login_page = PortalLoginPage(driver)
    login_page.login(os.getenv("PATIENT_USERNAME"), os.getenv("PATIENT_PASSWORD"), os.getenv("PATIENT_EMAIL"))

    dashboard = PortalDashboardPage(driver)
    dashboard.go_to("profile")

    profile = PortalProfilePage(driver)
    profile.wait_until_visible(timeout=TIMEOUT)
    assert profile.is_dob_formatted(), "DOB field should be formatted as YYYY-MM-DD"

@pytest.mark.regression
@pytest.mark.tc06
def test_phone_format(driver):
    driver.get(BASE_URL)
    login_page = PortalLoginPage(driver)
    login_page.login(os.getenv("PATIENT_USERNAME"), os.getenv("PATIENT_PASSWORD"), os.getenv("PATIENT_EMAIL"))

    dashboard = PortalDashboardPage(driver)
    dashboard.go_to("profile")

    profile = PortalProfilePage(driver)
    profile.wait_until_visible(timeout=TIMEOUT)
    assert profile.is_phone_formatted(), "DOB field should be formatted as ###-###-####"