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

# Wait for the login CTA and click on it
login_button_locator = (By.ID, 'com.arriva.bus:id/login')
wait = WebDriverWait(driver, 20)
login_button = wait.until(EC.visibility_of_element_located(login_button_locator))
TouchAction(driver).tap(login_button).perform()

# Enter email and password
email_input_locator = (By.ID, 'com.arriva.bus:id/emailInputField')
password_input_locator = (By.ID, 'com.arriva.bus:id/passwordInputField')

email_input = wait.until(EC.visibility_of_element_located(email_input_locator))
password_input = wait.until(EC.visibility_of_element_located(password_input_locator))

email_input.send_keys("testuser@gmaiil.com")
password_input.send_keys("Arriva123$")

# Click on the login CTA
login_cta_locator = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.Button')
login_cta = wait.until(EC.visibility_of_element_located(login_cta_locator))
TouchAction(driver).tap(login_cta).perform()

# Tap on the continue CTA
continue_cta_locator = (By.ID, 'com.arriva.bus:id/continueButton')
continue_cta = wait.until(EC.visibility_of_element_located(continue_cta_locator))
TouchAction(driver).tap(continue_cta).perform()

# Grant location permission
permission_button_locator = (By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
permission_button = wait.until(EC.visibility_of_element_located(permission_button_locator))
TouchAction(driver).tap(permission_button).perform()

# Tap on the buy ticket CTA
buy_ticket_locator = (By.ID, 'com.arriva.bus:id/tickets')
buy_ticket_cta = wait.until(EC.visibility_of_element_located(buy_ticket_locator))
TouchAction(driver).tap(buy_ticket_cta).perform()

# Select beds & bucks option
beds_bucks_locator = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView')
beds_bucks_option = wait.until(EC.visibility_of_element_located(beds_bucks_locator))
TouchAction(driver).tap(beds_bucks_option).perform()

# Select aylesbury plus option
aylesbury_plus_locator = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.ImageView')
aylesbury_plus_option = wait.until(EC.visibility_of_element_located(aylesbury_plus_locator))
TouchAction(driver).tap(aylesbury_plus_option).perform()

# Tap on the purchase ticket CTA
purchase_ticket_locator = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.Button')
purchase_ticket_cta = wait.until(EC.visibility_of_element_located(purchase_ticket_locator))
TouchAction(driver).tap(purchase_ticket_cta).perform()

# Tap on the adult ticket
adult_ticket_locator = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView')
adult_ticket_option = wait.until(EC.visibility_of_element_located(adult_ticket_locator))
TouchAction(driver).tap(adult_ticket_option).perform()

# Add 1 adult day 5
adult_day_5_locator = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.ImageView[3]')
adult_day_5_option = wait.until(EC.visibility_of_element_located(adult_day_5_locator))
TouchAction(driver).tap(adult_day_5_option).perform()

# Proceed to view basket
view_basket_locator = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.view.ViewGroup/android.widget.TextView[1]')
view_basket_button = wait.until(EC.visibility_of_element_located(view_basket_locator))
TouchAction(driver).tap(view_basket_button).perform()

# Scroll down
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(513, 1739)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(516, 847)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Select payment method
payment_method_locator = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.Button')
payment_method_button = wait.until(EC.visibility_of_element_located(payment_method_locator))
TouchAction(driver).tap(payment_method_button).perform()

payment_method_selector = (By.XPATH, '//androidx.recyclerview.widget.RecyclerView[@content-desc="Supported payment methods"]/android.widget.RelativeLayout[2]')
payment_selector_button = wait.until(EC.visibility_of_element_located(payment_method_selector))
TouchAction(driver).tap(payment_selector_button).perform()


# Quit the driver