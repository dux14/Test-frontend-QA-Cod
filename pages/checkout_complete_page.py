from playwright.sync_api import Page, expect
from config import CHECKOUT_COMPLETE_URL, INVENTORY_URL

class CheckoutCompletePage:
    def __init__(self, page: Page):
        self.page = page
        
    def verify_checkout_complete_page(self):
        """Verify that we are on the checkout confirmation page by checking the URL and title"""
        expect(self.page).to_have_url(CHECKOUT_COMPLETE_URL)
        
        title = self.page.locator(".title")
        expect(title).to_have_text("Checkout: Complete!")
        
    def verify_confirmation_message(self):
        """Verify that the confirmation message is correct"""
        header = self.page.locator(".complete-header")
        expect(header).to_have_text("Thank you for your order!")
        
        text = self.page.locator(".complete-text")
        expect(text).to_have_text("Your order has been dispatched, and will arrive just as fast as the pony can get there!") 