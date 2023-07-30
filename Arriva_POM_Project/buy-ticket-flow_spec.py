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

# Create page objects
login_page = LoginPage(driver)
buy_ticket_page = BuyTicketPage(driver)

# Test steps using the page objects
login_page.tap_login_button()
login_page.enter_credentials("testuser@gmaiil.com", "Arriva123$")
login_page.tap_login_cta()

buy_ticket_page.tap_continue_cta()
buy_ticket_page.grant_location_permission()
buy_ticket_page.tap_buy_ticket_cta()
buy_ticket_page.select_beds_bucks_option()
buy_ticket_page.select_aylesbury_plus_option()
buy_ticket_page.tap_purchase_ticket_cta()
buy_ticket_page.tap_adult_ticket()
buy_ticket_page.add_adult_day_5()
buy_ticket_page.proceed_to_view_basket()
buy_ticket_page.scroll_down()
buy_ticket_page.select_payment_method()

# Quit the driver
driver.quit()
