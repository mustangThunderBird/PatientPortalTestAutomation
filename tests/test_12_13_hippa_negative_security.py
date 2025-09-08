import os
import pytest
from pages.portal_login_page import PortalLoginPage
from pages.portal_dashboard_page import PortalDashboardPage
from pages.portal_documents_page import PortalDocumentsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

BASE_URL = os.getenv("BASE_URL")
TIMEOUT = int(os.getenv("TIMEOUT"))

@pytest.mark.security
@pytest.mark.tc12
def test_hipaa_negative_cross_patient_access(driver):
    driver.get(BASE_URL)
    login_page = PortalLoginPage(driver)
    login_page.login(os.getenv("PATIENT_USERNAME"), os.getenv("PATIENT_PASSWORD"), os.getenv("PATIENT_EMAIL"))

    dashboard = PortalDashboardPage(driver)
    dashboard.go_to("documents")

    documents = PortalDocumentsPage(driver)

    # Try to hack into another patient’s docs
    error_text = documents.try_to_manually_switch_patient_id_in_url()

    # Assert unauthorized access is blocked
    assert error_text is not None, "Expected unauthorized access to show an error message"
    assert "unauthorized" in error_text.lower(), f"Unexpected error text: {error_text}"
    
@pytest.mark.security
@pytest.mark.tc13
def test_hipaa_negative_admin_page_access(driver):
    driver.get(BASE_URL)
    login_page = PortalLoginPage(driver)
    login_page.login(
        os.getenv("PATIENT_USERNAME"),
        os.getenv("PATIENT_PASSWORD"),
        os.getenv("PATIENT_EMAIL")
    )

    dashboard = PortalDashboardPage(driver)
    assert dashboard.is_logged_in(), "Patient failed to log in"

    # Attempt to directly access the admin page
    target_url = "https://demo.openemr.io/openemr/interface/main/tabs/main.php"
    driver.get(target_url)

    # Expect either redirect OR error message
    try:
        WebDriverWait(driver, 5).until(EC.url_contains("login.php"))
        redirected = True
    except:
        redirected = False

    if not redirected:
        # Fall back: look for error message on the page
        error_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Site ID is missing')]"))
        )
        assert "Site ID is missing" in error_elem.text, f"Unexpected page content: {error_elem.text}"
    