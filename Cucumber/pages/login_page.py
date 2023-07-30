from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def tap_login_button(self):
        login_button_locator = (By.ID, 'com.arriva.bus:id/login')
        login_button = self.wait.until(EC.visibility_of_element_located(login_button_locator))
        login_button.click()

    def enter_credentials(self, email, password):
        email_input_locator = (By.ID, 'com.arriva.bus:id/emailInputField')
        password_input_locator = (By.ID, 'com.arriva.bus:id/passwordInputField')

        email_input = self.wait.until(EC.visibility_of_element_located(email_input_locator))
        password_input = self.wait.until(EC.visibility_of_element_located(password_input_locator))

        email_input.send_keys(email)
        password_input.send_keys(password)

    def tap_login_cta(self):
        login_cta_locator = (By.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.Button')
        login_cta = self.wait.until(EC.visibility_of_element_located(login_cta_locator))
        login_cta.click()
