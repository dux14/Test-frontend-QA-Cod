from playwright.sync_api import Page, expect
from config import CHECKOUT_STEP_TWO_URL, INVENTORY_URL, PRODUCT_1, PRODUCT_2, SUBTOTAL, TAX, TOTAL

class CheckoutStepTwoPage:
    def __init__(self, page: Page):
        self.page = page
        
    def verify_checkout_step_two_page(self):
        """Verify that we are on the second checkout page by checking the URL and title"""
        expect(self.page).to_have_url(CHECKOUT_STEP_TWO_URL)
        
        title = self.page.locator(".title")
        expect(title).to_have_text("Checkout: Overview")
        
    def verify_product_by_name(self, product_name, expected_price):
        """Verify that a specific product appears in the summary with the correct price"""
        names = self.page.locator(".inventory_item_name")
        
        found = False
        count = names.count()
        
        for i in range(count):
            if names.nth(i).text_content() == product_name:
                found = True
                price = self.page.locator(".inventory_item_price").nth(i)
                expect(price).to_have_text(expected_price)
                break
        
        assert found, f"Product '{product_name}' not found in the checkout summary"
        
    def verify_product_summary(self):
        """Verify that the products appear in the checkout summary"""
        items = self.page.locator(".cart_item")
        expect(items).to_have_count(2)
        
        self.verify_product_by_name(PRODUCT_1["name"], PRODUCT_1["price"])
        
        self.verify_product_by_name(PRODUCT_2["name"], PRODUCT_2["price"])
        
    def verify_total(self):
        """Verify that the total amount is correct"""
        subtotal = self.page.locator(".summary_subtotal_label")
        expect(subtotal).to_contain_text(SUBTOTAL)
        
        tax = self.page.locator(".summary_tax_label")
        expect(tax).to_contain_text(TAX)
        
        total = self.page.locator(".summary_total_label")
        expect(total).to_contain_text(TOTAL)
        
    def finish_purchase(self):
        """Click the finish button to complete the purchase"""
        finish_button = self.page.locator("[data-test=\"finish\"]")
        finish_button.click() 