import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.pointer_actions import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input_locator = (By.ID, "com.arriva.bus:id/firstNameInputField")
        self.last_name_input_locator = (By.ID, "com.arriva.bus:id/lastNameInputField")
        self.email_input_locator = (By.ID, "com.arriva.bus:id/emailInputField")
        self.confirm_email_input_locator = (By.ID, "com.arriva.bus:id/emailInputField2")
        self.passenger_type_dropdown_locator = (By.ID, "com.arriva.bus:id/passengerType")
        self.phone_number_input_locator = (By.ID, "com.arriva.bus:id/phoneNumberInputField")
        self.create_password_input_locator = (By.ID, "com.arriva.bus:id/passwordInputField")
        self.confirm_password_input_locator = (By.ID, "com.arriva.bus:id/passwordInputField2")
        self.checkbox_locator = (By.ID, "com.arriva.bus:id/chSelectAll")
        self.create_account_button_locator = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.Button")
        self.create_continue_button_locator = (By.ID,"com.arriva.bus:id/getStartedButton")
        self.wait = WebDriverWait(self.driver, 20)

    def enter_first_name(self, first_name):
        first_name_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_name_input_locator))
        first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.last_name_input_locator))
        last_name_input.send_keys(last_name)

    def enter_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.email_input_locator))
        email_input.send_keys(email)

    def enter_confirm_email(self, email):
        confirm_email_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.confirm_email_input_locator))
        confirm_email_input.send_keys(email)

    def select_passenger_type(self, index):
        passenger_type_dropdown_locator = (By.ID, "com.arriva.bus:id/passengerType")
        passenger_type_option_locator = (By.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[{index + 1}]")

        dropdown = self.wait.until(EC.visibility_of_element_located(passenger_type_dropdown_locator))
        dropdown.click()

        option = self.wait.until(EC.visibility_of_element_located(passenger_type_option_locator))
        option.click()

    def enter_phone_number(self, phone_number):
        phone_number_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.phone_number_input_locator))
        phone_number_input.send_keys(phone_number)

    def enter_create_password(self, password):
        create_password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.create_password_input_locator))
        create_password_input.send_keys(password)

    def perform_custom_action(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.create_password_input_locator))
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(513, 1739)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(516, 847)
        actions.w3c_actions.pointer_action.release()
        actions.perform()



    def enter_confirm_password(self, password):
        confirm_password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.confirm_password_input_locator))
        confirm_password_input.send_keys(password)

    def select_terms_and_conditions(self):
        checkbox = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.checkbox_locator))
        checkbox.click()

    def click_checkbox(self):
        checkbox_locator = (By.ID, "com.arriva.bus:id/chSelectAll")
        checkbox = self.wait.until(EC.visibility_of_element_located(checkbox_locator))
        checkbox.click()

    def click_create_account(self):
        create_account_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.create_account_button_locator))
        create_account_button.click()

    def click_continue_button(self):
        create_continue_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.create_continue_button_locator))
        create_continue_button.click()