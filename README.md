# OpenEMR Patient Portal Test Automation
- This project is a Selenium + PyTest based automation suite for validating the OpenEMR Patient Portal demo site. It follows the Page Object Model (POM) design and includes coverage for authentication, patient profile integrity, appointments, secure messaging, and HIPAA-style negative security checks.
- The suite is designed as a portfolio-grade example of healthcare QA automation, featuring structured tests, HTML reporting with screenshots, headless execution, and GitHub Actions CI.

---

## Features

- **Page Object Model (POM)** structure for maintainable test code
- **Authentication tests** (valid login, invalid login, logout)
- **Profile tests** (demographics presence, DOB format, phone format)
- **Appointment tests** (request, edit, cancel)
- **Messaging tests** (send and view messages)
- **HIPAA-style security tests** (cross-patient URL tampering, admin page access)
- **HTML reporting** via `pytest-html` with embedded screenshots on failure
- **Headless execution** toggle for CI or local runs
- **PyTest markers** (`smoke`, `regression`, `security`, plus per-test IDs)
- **CI pipeline** with GitHub Actions

---

## Project Structure
```text
PatientPortalTestAutomation/
├── pages/                   
│   ├── base_page.py
│   ├── portal_login_page.py
│   ├── portal_dashboard_page.py
│   ├── portal_profile_page.py
│   ├── portal_appointments_page.py
│   ├── portal_messaging_page.py
│   └── portal_documents_page.py
├── tests/                   
│   ├── test_01_03_auth.py
│   ├── test_04_06_profile.py
│   ├── test_07_09_appointments.py
│   ├── test_10_11_messaging.py
│   └── test_12_13_hippa_negative_security.py
├── utils/                   
│   └── screenshot.py
├── conftest.py              
├── requirements.txt         
├── pytest.ini               
├── run_tests.yml            
├── .env.example             
└── README.md
```

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/PatientPortalTestAutomation.git
cd PatientPortalTestAutomation
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
`pip install -r requirements.txt`

### 4. Configure environment variables

```bash
BASE_URL=https://demo.openemr.io/openemr/portal/index.php
PATIENT_USERNAME=Susan2
PATIENT_PASSWORD=susan
PATIENT_EMAIL=nana@invalid.email.com
HEADLESS=false
TIMEOUT=10
```

### 5. Set PYTHONPATH
Before running locally, set the project root to PYTHONPATH:
```bash
$env:PYTHONPATH = "$PWD"    # On Windows
export PYTHONPATH=$PWD      # On Linux/Mac
```

## Running Tests

### Run all tests (default HTML report enabled via `pytest.ini`)
`pytest --browser=chrome`

### Run specific test cases
```bash
pytest -m smoke --browser=chrome
pytest -m regression --browser=chrome
pytest -m security --browser=chrome
```

### Run by Test ID
```pytest -m tc07 --browser=chrome```

### Generate test report
- Reports are saved automatically to `reports/report.html`.

## Continuous Integration
- The included GitHub Actions workflow (`.github/workflows/run_tests.yml`) runs tests headlessly on Chrome for each push or pull request. Reports are uploaded as build artifacts.

## Test Plan Coverage
Mapped to manual test cases documented in OpenEMR Patient Portal Test Plan.md:
- TC01–TC03: Authentication
- TC04–TC06: Profile demographics
- TC07–TC09: Appointments
- TC10–TC11: Messaging
- TC12–TC13: HIPAA/security

## Troubleshooting
- Ensure ChromeDriver is available in PATH (Selenium handles this in most modern versions).
- Use `HEADLESS=false` in `.env` to debug visually.
- Delete `reports/` if reports fail to regenerate.
- If tests fail inconsistently, increase TIMEOUT var in `.env`.

## License
This project is for educational and portfolio purposes. It is not affiliated with or endorsed by OpenEMR.