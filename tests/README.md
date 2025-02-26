# QA Automation Project 1: Web Testing with Selenium

Automates functional tests for [Sauce Demo](https://www.saucedemo.com/) using Python and Selenium WebDriver.

## Setup
1. Install Python 3.x and Selenium: `pip install selenium`.
2. Install ChromeDriver 133.0.6943.98 and add to PATH.
3. (Optional) Install PyTest: `pip install pytest`.
4. Run tests: `python tests/test_sauce.py` or `pytest tests/test_sauce.py -v`.

## Tests
- **Valid Login:** Logs in with `standard_user/secret_sauce`.
- **Invalid Login:** Verifies error with wrong credentials.
- **Add to Cart:** Adds a backpack to the cart.
- **Remove from Cart:** Removes the item.
- **Checkout:** Completes a purchase flow.

## Sample Output
![Login Success](login_success.png)

## Results
All 5 tests passed using PyTest on Chrome 133.0.6943.142.