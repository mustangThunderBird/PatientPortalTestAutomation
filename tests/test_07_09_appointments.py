import os
import pytest
from pages.portal_login_page import PortalLoginPage
from pages.portal_dashboard_page import PortalDashboardPage
from pages.portal_appointments_page import PortalAppointmentsPage

BASE_URL = os.getenv("BASE_URL")
TIMEOUT = int(os.getenv("TIMEOUT"))

@pytest.mark.regression
@pytest.mark.tc07
def test_request_appointment(driver):
    driver.get(BASE_URL)
    login_page = PortalLoginPage(driver)
    login_page.login(os.getenv("PATIENT_USERNAME"), os.getenv("PATIENT_PASSWORD"), os.getenv("PATIENT_EMAIL"))
    
    dashboard = PortalDashboardPage(driver)
    dashboard.go_to("appointments")
    
    appointments = PortalAppointmentsPage(driver)
    appointments.wait_until_visible(appointments.APPOINTMENTS_CARD, timeout=TIMEOUT)
    
    appointment_saved = appointments.request_appointment()
    
    assert appointment_saved, "Appointment was not saved successfully"
    
@pytest.mark.regression
@pytest.mark.tc08
def test_edit_appointment(driver):
    driver.get(BASE_URL)
    login_page = PortalLoginPage(driver)
    login_page.login(os.getenv("PATIENT_USERNAME"), os.getenv("PATIENT_PASSWORD"), os.getenv("PATIENT_EMAIL"))
    
    dashboard = PortalDashboardPage(driver)
    dashboard.go_to("appointments")
    
    appointments = PortalAppointmentsPage(driver)
    appointments.wait_until_visible(appointments.APPOINTMENTS_CARD, timeout=TIMEOUT)
    
    appointment_changed = appointments.edit_appointment()
    
    assert appointment_changed, "Appointment was not edited successfully"