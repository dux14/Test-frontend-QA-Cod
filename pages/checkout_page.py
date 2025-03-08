from playwright.sync_api import Page, expect
from config import CHECKOUT_STEP_ONE_URL

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        
    def verify_checkout_step_one_page(self):
        """Verify that we are on the first checkout page by checking the URL and title"""
        expect(self.page).to_have_url(CHECKOUT_STEP_ONE_URL)
        
        title = self.page.locator(".title")
        expect(title).to_have_text("Checkout: Your Information")
        
    def enter_user_information(self, first_name, last_name, postal_code):
        """Enter the user information in the checkout form"""
        self.verify_checkout_step_one_page()
        
        first_name_input = self.page.locator("[data-test=\"firstName\"]")
        first_name_input.fill(first_name)
        
        last_name_input = self.page.locator("[data-test=\"lastName\"]")
        last_name_input.fill(last_name)
        
        postal_code_input = self.page.locator("[data-test=\"postalCode\"]")
        postal_code_input.fill(postal_code)
        
    def continue_to_step_two(self):
        """Click the continue button to go to the second checkout page"""
        continue_button = self.page.locator("[data-test=\"continue\"]")
        continue_button.click() 