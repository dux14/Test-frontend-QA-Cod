from playwright.sync_api import Page, expect
from config import CART_URL, PRODUCT_1, PRODUCT_2

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        
    def verify_cart_page(self):
        """Verify that we are on the cart page by checking the URL and title"""
        expect(self.page).to_have_url(CART_URL)
        
        title = self.page.locator(".title")
        expect(title).to_have_text("Your Cart")
    
    def verify_product_by_name(self, product_name, expected_price):
        """Verify that a specific product appears in the cart with the correct price"""
        names = self.page.locator(".inventory_item_name")
        
        found = False
        count = names.count()
        
        for i in range(count):
            if names.nth(i).text_content() == product_name:
                found = True
                price = self.page.locator(".inventory_item_price").nth(i)
                expect(price).to_have_text(expected_price)
                break
        
        assert found, f"Product '{product_name}' not found in the cart"
        
    def verify_specific_products(self):
        """Verify that the specific products (Sauce Labs Bike Light and Test.allTheThings() T-Shirt) 
        appear in the cart with the correct data"""
        items = self.page.locator(".cart_item")
        expect(items).to_have_count(2)
        
        self.verify_product_by_name(PRODUCT_1["name"], PRODUCT_1["price"])
        
        self.verify_product_by_name(PRODUCT_2["name"], PRODUCT_2["price"])
        
    def go_to_checkout(self):
        """Click the checkout button to continue with the checkout process"""
        checkout_button = self.page.locator("[data-test=\"checkout\"]")
        checkout_button.click()