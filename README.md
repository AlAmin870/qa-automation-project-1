# Selenium UI Test Automation — Sauce Demo

[![UI Tests](https://github.com/AlAmin870/qa-automation-project-1/actions/workflows/tests.yml/badge.svg)](https://github.com/AlAmin870/qa-automation-project-1/actions/workflows/tests.yml)

End-to-end UI tests for the [Sauce Demo](https://www.saucedemo.com/) e-commerce site, written in **Python + Selenium WebDriver + PyTest** using the **Page Object Model**. Tests run headless on every push through GitHub Actions.

## What's covered (11 tests)

| Area | Scenarios |
|---|---|
| Login | Valid login; invalid credentials, locked-out user, empty username, empty password (data-driven with `pytest.mark.parametrize`) |
| Cart | Add one item, add multiple items, remove item, sort products by price (low → high) |
| Checkout | Full purchase flow with item-total check; required-field validation on postal code |

## Framework design

- **Page Object Model** — locators and page actions live in `pages/`, so tests read like user steps and a UI change is fixed in one place.
- **Explicit waits** — `BasePage` wraps `WebDriverWait`; there is no `time.sleep()` anywhere.
- **Fixtures** — `driver` opens and always closes the browser (even on failure); `logged_in` reuses the login step.
- **Screenshot on failure** — a PyTest hook saves a screenshot to `reports/screenshots/` for any failed test.
- **HTML report** — `pytest-html` writes `reports/report.html`; CI uploads it as a build artifact.
- **No driver setup** — Selenium Manager downloads the matching ChromeDriver automatically.

```
├── pages/                 # Page objects
│   ├── base_page.py       # Explicit-wait helpers
│   ├── login_page.py
│   ├── inventory_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
├── conftest.py            # Browser fixture, login fixture, screenshot hook
├── pytest.ini
├── requirements.txt
└── .github/workflows/tests.yml
```

## Run locally

```bash
pip install -r requirements.txt
pytest                      # headless, report at reports/report.html
HEADLESS=false pytest       # watch the browser
```

Requires Python 3.10+ and Google Chrome.
