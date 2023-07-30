from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class BuyTicketPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def tap_continue_cta(self):
        continue_cta_locator = (By.ID, 'com.arriva.bus:id/continueButton')
        continue_cta = self.wait.until(EC.visibility_of_element_located(continue_cta_locator))
        continue_cta.click()

    def grant_location_permission(self):
        permission_button_locator = (
        By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        permission_button = self.wait.until(EC.visibility_of_element_located(permission_button_locator))
        permission_button.click()

    def tap_buy_ticket_cta(self):
        buy_ticket_locator = (By.ID, 'com.arriva.bus:id/tickets')
        buy_ticket_cta = self.wait.until(EC.visibility_of_element_located(buy_ticket_locator))
        buy_ticket_cta.click()

    def select_beds_bucks_option(self):
        beds_bucks_locator = (By.XPATH,
                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView')
        beds_bucks_option = self.wait.until(EC.visibility_of_element_located(beds_bucks_locator))
        beds_bucks_option.click()

    def select_aylesbury_plus_option(self):
        aylesbury_plus_locator = (By.XPATH,
                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.ImageView')
        aylesbury_plus_option = self.wait.until(EC.visibility_of_element_located(aylesbury_plus_locator))
        aylesbury_plus_option.click()

    def tap_purchase_ticket_cta(self):
        purchase_ticket_locator = (By.XPATH,
                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.Button')
        purchase_ticket_cta = self.wait.until(EC.visibility_of_element_located(purchase_ticket_locator))
        purchase_ticket_cta.click()

    def tap_adult_ticket(self):
        adult_ticket_locator = (By.XPATH,
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView')
        adult_ticket_option = self.wait.until(EC.visibility_of_element_located(adult_ticket_locator))
        adult_ticket_option.click()

    def add_adult_day_5(self):
        adult_day_5_locator = (By.XPATH,
                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.ImageView[3]')
        adult_day_5_option = self.wait.until(EC.visibility_of_element_located(adult_day_5_locator))
        adult_day_5_option.click()

    def proceed_to_view_basket(self):
        view_basket_locator = (By.XPATH,
                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.view.ViewGroup/android.widget.TextView[1]')
        view_basket_button = self.wait.until(EC.visibility_of_element_located(view_basket_locator))
        view_basket_button.click()

    def scroll_down(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(513, 1739)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(516, 847)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def select_payment_method(self):
        payment_method_locator = (By.XPATH,
                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.Button')
        payment_method_button = self.wait.until(EC.visibility_of_element_located(payment_method_locator))
        payment_method_button.click()

        payment_method_selector = (By.XPATH,
                                   '//androidx.recyclerview.widget.RecyclerView[@content-desc="Supported payment methods"]/android.widget.RelativeLayout[2]')
        payment_selector_button = self.wait.until(EC.visibility_of_element_located(payment_method_selector))
        payment_selector_button.click()
