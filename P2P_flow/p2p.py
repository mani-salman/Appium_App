import pytest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired capabilities for the Appium driver
desired_cap = {
    "platformName": "Android",
    "platformVersion": "11",
    "app": "C:\\Users\\HP\\Desktop\\AppiumApps\\com.arriva.bus_2023-06-05.apk",
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

def test_search_and_select_destination():
    # Tap on the "Where do you want to go?" field and search for "London Road Armoury Gardens"
    destination_field_locator = (By.ID, 'com.arriva.bus:id/search')
    destination_field = wait.until(EC.visibility_of_element_located(destination_field_locator))
    destination_field.click()

    time.sleep(2)

    # Check if the destination search field is clickable
    destination_search_locator = (By.ID, 'com.arriva.bus:id/locationName')
    destination_search = wait.until(EC.element_to_be_clickable(destination_search_locator))
    destination_search.click()

    # Wait briefly before forcefully setting the value in the field
    time.sleep(1)

    search_query = "London Road Armoury Gardens"
    driver.set_value(destination_search, search_query)

    # Wait for the search results to appear and select "London Road Armoury Gardens" from the drop-down
    search_result_locator = (By.XPATH, '//android.view.ViewGroup[@content-desc="item_0"]/android.widget.TextView')
    london_road_armoury_gardens_option = wait.until(EC.visibility_of_element_located(search_result_locator))
    london_road_armoury_gardens_option.click()


def test_select_date_from_calendar():
    # Tap on the calendar to select the date
    calendar_locator = (By.ID, 'com.arriva.bus:id/departureTimeLabel')
    calendar_button = wait.until(EC.visibility_of_element_located(calendar_locator))
    calendar_button.click()


# The test functions will be executed as part of the test suite
if __name__ == "__main__":
    pytest.main(["-v"])
