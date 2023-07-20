import random
import string
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Arriva_POM_Project.login_page import LoginPage
from Arriva_POM_Project.signup_page import SignupPage

# Desired capabilities for the Appium driver
desired_cap = {
    "platformName": "Android",
    "platformVersion": "11",
    "app": "C:\\Users\\HP\\Desktop\\AppiumApps\\com.arriva.bus_2023-06-05.apk"
}

# Generate a random email address

def generate_random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
    email = f"{random_string}@example.com"
    return email

# Initialize the driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

# Wait for the skip button and click on it
wait = WebDriverWait(driver, 20)
skip_button_locator = (By.ID, 'com.arriva.bus:id/skip')
skip_button = wait.until(EC.visibility_of_element_located(skip_button_locator))
TouchAction(driver).tap(skip_button).perform()

# Grant location permission
permission_button_locator = (By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
permission_button = wait.until(EC.visibility_of_element_located(permission_button_locator))
TouchAction(driver).tap(permission_button).perform()

# Create instances of the page objects
login_page = LoginPage(driver)
signup_page = SignupPage(driver)

# Perform actions on the login page
login_page.click_profile_section()
login_page.click_signup()

# Perform actions on the signup page
signup_page.enter_first_name("John")
signup_page.enter_last_name("Doe")
random_email = generate_random_email()
signup_page.enter_email(random_email)
signup_page.enter_confirm_email(random_email)
signup_page = SignupPage(driver)
signup_page.select_passenger_type(0)
signup_page.enter_phone_number("1234567890")
signup_page.enter_create_password("123@Mani")
signup_page.perform_custom_action()
signup_page.enter_confirm_password("123@Mani")
signup_page.click_checkbox()
signup_page.perform_custom_action()
signup_page.click_create_account()
signup_page.click_continue_button()
# Quit the driver
