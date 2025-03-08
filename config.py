"""
Configuration file for test variables
"""

# URLs
BASE_URL = "https://www.saucedemo.com"
INVENTORY_URL = f"{BASE_URL}/inventory.html"
CART_URL = f"{BASE_URL}/cart.html"
CHECKOUT_STEP_ONE_URL = f"{BASE_URL}/checkout-step-one.html"
CHECKOUT_STEP_TWO_URL = f"{BASE_URL}/checkout-step-two.html"
CHECKOUT_COMPLETE_URL = f"{BASE_URL}/checkout-complete.html"

# Credentials
STANDARD_USER = "standard_user"
STANDARD_PASSWORD = "secret_sauce"

# Product data
PRODUCT_1 = {
    "name": "Sauce Labs Bike Light",
    "price": "$9.99",
    "id": "sauce-labs-bike-light"
}

PRODUCT_2 = {
    "name": "Test.allTheThings() T-Shirt (Red)",
    "price": "$15.99",
    "id": "test.allthethings()-t-shirt-(red)"
}

# Checkout data
SUBTOTAL = "$25.98" 
TAX = "$2.08"
TOTAL = "$28.06"  

# Test user data
TEST_USER = {
    "first_name": "Test",
    "last_name": "User",
    "postal_code": "12345"
}

# Test data generation settings
TEST_DATA_GENERATION = {
    "use_random_data": True,  
    "postal_code_format": "US", 
    "name_min_length": 3,
    "name_max_length": 7
} 