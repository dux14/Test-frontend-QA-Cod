import pytest
from playwright.sync_api import sync_playwright
import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage
from config import STANDARD_USER, STANDARD_PASSWORD, TEST_USER, TEST_DATA_GENERATION
from utils.test_data_generator import generate_test_user_data

def get_user_data():
    """
    Get user data for testing, either random or fixed based on configuration
    
    Returns:
        A dictionary containing user data (first_name, last_name, postal_code)
    """
    if TEST_DATA_GENERATION["use_random_data"]:
        return generate_test_user_data(
            country_format=TEST_DATA_GENERATION["postal_code_format"]
        )
    else:
        return TEST_USER

@pytest.fixture(scope="function")
def page_context():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def test_login(page_context):
    """Test to verify the login functionality"""
    login_page = LoginPage(page_context)
    login_page.load()
    
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    
    assert "inventory" in page_context.url

def test_add_products_to_cart(page_context):
    """Test to verify that we can add products to the cart correctly"""
    login_page = LoginPage(page_context)
    login_page.load()
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    
    product_page = ProductPage(page_context)
    product_page.verify_product_page()
    
    product_page.add_specific_products_to_cart()
    
    product_page.verify_cart(2)

def test_verify_products_in_cart(page_context):
    """Test to verify that the added products appear correctly in the cart"""
    login_page = LoginPage(page_context)
    login_page.load()
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    
    product_page = ProductPage(page_context)
    product_page.verify_product_page()
    
    product_page.add_specific_products_to_cart()
    
    product_page.go_to_cart()
    
    cart_page = CartPage(page_context)
    cart_page.verify_cart_page()
    
    cart_page.verify_specific_products()

def test_checkout_process(page_context):
    """Test to verify the complete checkout process"""
    login_page = LoginPage(page_context)
    login_page.load()
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)
    
    product_page = ProductPage(page_context)
    product_page.verify_product_page()
    
    product_page.add_specific_products_to_cart()
    
    product_page.go_to_cart()
    
    cart_page = CartPage(page_context)
    cart_page.verify_cart_page()
    
    cart_page.verify_specific_products()
    
    cart_page.go_to_checkout()
    
    checkout_page = CheckoutPage(page_context)
    checkout_page.verify_checkout_step_one_page()
    
    user_data = get_user_data()
    
    checkout_page.enter_user_information(
        user_data["first_name"], 
        user_data["last_name"], 
        user_data["postal_code"]
    )
    
    print(f"\nUsing test data: {user_data}")
    
    checkout_page.continue_to_step_two()
    
    checkout_step_two_page = CheckoutStepTwoPage(page_context)
    checkout_step_two_page.verify_checkout_step_two_page()
    
    checkout_step_two_page.verify_product_summary()
    
    checkout_step_two_page.verify_total()
    
    checkout_step_two_page.finish_purchase()
    
    checkout_complete_page = CheckoutCompletePage(page_context)
    checkout_complete_page.verify_checkout_complete_page()
    
    checkout_complete_page.verify_confirmation_message()
