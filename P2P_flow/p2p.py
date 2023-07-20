import time
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired capabilities for the Appium driver
desired_cap = {
    "platformName": "Android",
    "platformVersion": "11",
    "app": "C:\\Users\\HP\\Desktop\\AppiumApps\\com.arriva.bus_2023-06-05.apk",
    "appPackage": "com.arriva.bus",
    "appActivity": "your_app_activity" # Replace with your app's activity name
}

# Appium server URL
appium_url = "http://localhost:4723/wd/hub"

# Initialize the driver
driver = webdriver.Remote(appium_url, desired_cap)

# Global wait variable
wait = WebDriverWait(driver, 20)

def test_login():
    # Wait for the login CTA and click on it
    login_button_locator = (By.ID, 'com.arriva.bus:id/login')
    login_button = wait.until(EC.element_to_be_clickable(login_button_locator))
    login_button.click()

    # Enter email and password
    email_input_locator = (By.ID, 'com.arriva.bus:id/emailInputField')
    password_input_locator = (By.ID, 'com.arriva.bus:id/passwordInputField')

    email_input = wait.until(EC.visibility_of_element_located(email_input_locator))
    password_input = wait.until(EC.visibility_of_element_located(password_input_locator))

    email_input.send_keys("testuser@gmaiil.com")
    password_input.send_keys("Arriva123$")

    # Click on the login CTA
    login_cta_locator = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.Button')
    login_cta = wait.until(EC.element_to_be_clickable(login_cta_locator))
    login_cta.click()

def test_grant_permission():
    # Wait for the continue CTA and click on it
    continue_cta_locator = (By.ID, 'com.arriva.bus:id/continueButton')
    continue_cta = wait.until(EC.element_to_be_clickable(continue_cta_locator))
    continue_cta.click()

    # Grant location permission
    permission_button_locator = (By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
    permission_button = wait.until(EC.element_to_be_clickable(permission_button_locator))
    permission_button.click()

def test_pin_location_on_map():
    # Wait for the map to load
    map_locator = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]')
    map_element = wait.until(EC.visibility_of_element_located(map_locator))

    # Define the coordinates of the main city (e.g., London)
    city_latitude = 51.5074
    city_longitude = -0.1278

    # Set the map's center to the desired coordinates
    script = f"map.setCenter({city_latitude}, {city_longitude});"
    driver.execute_script(script)

    # Wait for a few seconds to allow the map to load the new location
    time.sleep(5)

def test_quit_driver():
    driver.quit()

if __name__ == "__main__":
    # Run the test functions using pytest
    pytest.main(["-v"])
