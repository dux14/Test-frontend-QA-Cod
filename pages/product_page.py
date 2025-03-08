from playwright.sync_api import Page, expect
import re
from config import INVENTORY_URL, PRODUCT_1, PRODUCT_2

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        
    def verify_product_page(self):
        """Verify that we are on the products page by checking the URL and title"""
        expect(self.page).to_have_url(INVENTORY_URL)
        
        title = self.page.locator("[data-test=\"title\"]")
        expect(title).to_have_text("Products")
        
    def verify_cart(self, expected_count):
        """Verify that the cart shows the correct number of products"""
        cart = self.page.locator("[data-test=\"shopping-cart-badge\"]")
        expect(cart).to_have_text(str(expected_count), timeout=2000)
    
    def get_cart_count(self):
        """Get the current number of products in the cart"""
        try:
            cart = self.page.locator("[data-test=\"shopping-cart-badge\"]")
            if cart.count() > 0:
                return int(cart.text_content(timeout=1000))
            return 0
        except Exception as e:
            print(f"Exception in get_cart_count: {e}")
            return 0
    
    def add_specific_products_to_cart(self):
        """Add the specific requested products to the cart: 
        Test.allTheThings() T-Shirt (Red) and Sauce Labs Bike Light"""
        initial_count = self.get_cart_count()
        
        add_button1 = self.page.locator(f"[data-test=\"add-to-cart-{PRODUCT_1['id']}\"]")
        add_button1.wait_for(state="visible", timeout=5000)
        add_button1.click()
        
        if initial_count == 0:
            self.page.wait_for_selector("[data-test=\"shopping-cart-badge\"]", timeout=5000)
        
        add_button2 = self.page.locator(f"[data-test=\"add-to-cart-{PRODUCT_2['id']}\"]")
        add_button2.wait_for(state="visible", timeout=5000)
        add_button2.click()
        
        self.page.wait_for_timeout(500)
        
        expected_count = initial_count + 2
        self.verify_cart(expected_count)
        
    def add_product_to_cart(self, product_id=None):
        """Add a specific product to the cart or the default products if none is specified"""
        initial_count = self.get_cart_count()
        
        if product_id:
            add_button = self.page.locator(f"[data-test=\"add-to-cart-{product_id}\"]")
            add_button.wait_for(state="visible", timeout=5000)
            add_button.click()
        else:
            self.add_specific_products_to_cart()
            return
        
        self.page.wait_for_timeout(500)
        
        expected_count = initial_count + 1
        self.verify_cart(expected_count)
    
    def go_to_cart(self):
        """Navigate to the cart page by clicking the cart icon"""
        cart_icon = self.page.locator("a.shopping_cart_link")
        cart_icon.wait_for(state="visible", timeout=5000)
        cart_icon.click()



    