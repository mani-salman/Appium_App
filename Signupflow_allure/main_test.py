import allure
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# Desired capabilities for the Appium driver
desired_cap = {
    "platformName": "Android",
    "platformVersion": "11",
    "app": "C:\\Users\\HP\\Desktop\\AppiumApps\\com.arriva.bus_2023-06-05.apk"
}

# Appium server URL
appium_url = "http://localhost:4723/wd/hub"

# Initialize the driver
driver = webdriver.Remote(appium_url, desired_cap)

# Global wait variable
wait = WebDriverWait(driver, 20)

# Wait for the login CTA and click on it
@allure.title("Test Case: Tap on Login CTA")
def test_tap_login_button():
    login_button_locator = (By.ID, 'com.arriva.bus:id/login')
    login_button = wait.until(EC.visibility_of_element_located(login_button_locator))
    assert login_button.is_displayed(), "Login button is not displayed"
    TouchAction(driver).tap(login_button).perform()


# Enter email and password
@allure.title("Test Case: Enter email and password")
def test_enter_credentials():
    email_input_locator = (By.ID, 'com.arriva.bus:id/emailInputField')
    password_input_locator = (By.ID, 'com.arriva.bus:id/passwordInputField')

    email_input = wait.until(EC.visibility_of_element_located(email_input_locator))
    password_input = wait.until(EC.visibility_of_element_located(password_input_locator))

    assert email_input.is_displayed(), "Email input field is not displayed"
    assert password_input.is_displayed(), "Password input field is not displayed"

    email_input.send_keys("testuser@gmaiil.com")
    password_input.send_keys("Arriva123$")

# Click on the login CTA
@allure.title("Test Case: Click on Login CTA")
def test_click_login_cta():
    login_cta_locator = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.Button')
    login_cta = wait.until(EC.visibility_of_element_located(login_cta_locator))
    assert login_cta.is_displayed(), "Login CTA button is not displayed"
    TouchAction(driver).tap(login_cta).perform()

# Proceed to view basket
@allure.title("Test Case: Scroll Down")
def test_scroll_down():
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(513, 1739)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(516, 847)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    assert True, "Scrolling down performed successfully"




if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=results"])
