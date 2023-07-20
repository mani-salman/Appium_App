from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input_locator = (By.ID, "com.arriva.bus:id/emailInputField")
        self.password_input_locator = (By.ID, "com.arriva.bus:id/passwordInputField")
        self.login_button_locator = (By.ID, "com.arriva.bus:id/loginButton")
        self.wait = WebDriverWait(self.driver, 20)  # Create WebDriverWait instance

    def click_profile_section(self):
        profile_button_locator = (
        By.XPATH, '//android.widget.FrameLayout[@content-desc="Account"]/android.widget.ImageView')
        profile_button = self.wait.until(EC.visibility_of_element_located(profile_button_locator))
        TouchAction(self.driver).tap(profile_button).perform()

    def click_signup(self):
        signup_button_locator = (By.ID, 'com.arriva.bus:id/signUp')
        signup_button = self.wait.until(EC.visibility_of_element_located(signup_button_locator))
        TouchAction(self.driver).tap(signup_button).perform()

    def enter_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.email_input_locator))
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input_locator))
        password_input.send_keys(password)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.login_button_locator))
        login_button.click()
