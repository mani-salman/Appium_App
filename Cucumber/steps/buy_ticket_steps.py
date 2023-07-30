from behave import given, when, then
from appium import webdriver
from login_page import LoginPage
from buy_ticket_page import BuyTicketPage

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
login_page = LoginPage(driver)
buy_ticket_page = BuyTicketPage(driver)

@given("I am on the login page")
def step_impl(context):
    login_page.tap_login_button()

@when("I enter my credentials with {email} and {password}")
def step_impl(context, email, password):
    login_page.enter_credentials(email, password)

@when("I tap the login button")
def step_impl(context):
    login_page.tap_login_cta()

@when("I tap the continue CTA")
def step_impl(context):
    buy_ticket_page.tap_continue_cta()

@when("I grant location permission")
def step_impl(context):
    buy_ticket_page.grant_location_permission()

@when("I tap the buy ticket CTA")
def step_impl(context):
    buy_ticket_page.tap_buy_ticket_cta()

@when("I select the beds & bucks option")
def step_impl(context):
    buy_ticket_page.select_beds_bucks_option()

@when("I select the aylesbury plus option")
def step_impl(context):
    buy_ticket_page.select_aylesbury_plus_option()

@when("I tap the purchase ticket CTA")
def step_impl(context):
    buy_ticket_page.tap_purchase_ticket_cta()

@when("I tap on the adult ticket")
def step_impl(context):
    buy_ticket_page.tap_adult_ticket()

@when("I add 1 adult day 5")
def step_impl(context):
    buy_ticket_page.add_adult_day_5()

@when("I proceed to view the basket")
def step_impl(context):
    buy_ticket_page.proceed_to_view_basket()

@when("I scroll down")
def step_impl(context):
    buy_ticket_page.scroll_down()

@when("I select the payment method")
def step_impl(context):
    buy_ticket_page.select_payment_method()

@then("I should be able to buy the ticket successfully")
def step_impl(context):

    pass

# Quit the driver
driver.quit()
