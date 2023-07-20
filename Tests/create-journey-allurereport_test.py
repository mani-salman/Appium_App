import random
import string
import allure
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Generate a random email address
def generate_random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
    email = f"{random_string}@example.com"
    return email

class SignupPage:
    def __init__(self, driver):
        self.driver = driver

        self.wait = WebDriverWait(self.driver, 20)

    def enter_first_name(self, first_name):
        first_name_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_name_input_locator))
        first_name_input.send_keys(first_name)

    # Rest of the methods in SignupPage...

# Desired capabilities for the Appium driver
desired_cap = {
    "platformName": "Android",
    "platformVersion": "11",
    "app": "C:\\Users\\HP\\Desktop\\AppiumApps\\com.arriva.bus_2023-06-05.apk",
    "adbExecTimeout": 30000  # Set adb execution timeout to 30 seconds
}

@pytest.fixture(scope="class")
def driver_setup(request):
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    def driver_teardown():
        driver.quit()

    request.addfinalizer(driver_teardown)
    return driver

@allure.feature("Signup Test")
class TestSignup:

    @allure.story("Signup with valid details")
    def test_signup_valid_details(self, driver_setup):
        driver = driver_setup
        signup_page = SignupPage(driver)

        # Wait for the skip button and click on it
        wait = WebDriverWait(driver, 20)
        skip_button_locator = (By.ID, 'com.arriva.bus:id/skip')
        skip_button = wait.until(EC.visibility_of_element_located(skip_button_locator))
        TouchAction(driver).tap(skip_button).perform()

        # Grant location permission
        permission_button_locator = (By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        permission_button = wait.until(EC.visibility_of_element_located(permission_button_locator))
        TouchAction(driver).tap(permission_button).perform()


        # Add Allure step descriptions and attachments
        allure.attach("Signup Test Passed", "Test completed successfully!", allure.attachment_type.TEXT)

if __name__ == "__main__":
    # Run the tests with pytest and Allure reporting
    pytest.main(['-s', '-v', '--alluredir', 'allure-results', '--capture=no'])
