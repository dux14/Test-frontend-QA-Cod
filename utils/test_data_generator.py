"""
Utility module for generating random test data with specific patterns
"""

import random
import string
import re

def generate_random_name(min_length=3, max_length=10):
    """
    Generate a random first or last name with proper capitalization.
    Names will only contain letters and will be properly capitalized.
    
    Args:
        min_length: Minimum length of the name
        max_length: Maximum length of the name
        
    Returns:
        A random name string
    """
    length = random.randint(min_length, max_length)
    
    first_letter = random.choice(string.ascii_uppercase)
    rest_of_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(length - 1))
    
    return first_letter + rest_of_name

def generate_random_postal_code(country_format="US"):
    """
    Generate a random postal code based on the specified country format.
    
    Args:
        country_format: The country format to use (default: "US")
            - "US": 5 digits (e.g., 12345)
            - "US_EXTENDED": 5 digits + hyphen + 4 digits (e.g., 12345-6789)
            - "CA": Letter + Number + Letter + space + Number + Letter + Number (e.g., A1A 1A1)
            - "UK": Outward code + space + inward code (e.g., AB1 2CD)
            
    Returns:
        A random postal code string matching the specified format
    """
    if country_format == "US":
        return ''.join(random.choice(string.digits) for _ in range(5))
    
    elif country_format == "US_EXTENDED":
        first_part = ''.join(random.choice(string.digits) for _ in range(5))
        second_part = ''.join(random.choice(string.digits) for _ in range(4))
        return f"{first_part}-{second_part}"
    
    elif country_format == "CA":
        letters = string.ascii_uppercase
        digits = string.digits
        
        return (
            f"{random.choice(letters)}{random.choice(digits)}{random.choice(letters)} "
            f"{random.choice(digits)}{random.choice(letters)}{random.choice(digits)}"
        )
    
    elif country_format == "UK":

        outward_letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(random.randint(1, 2)))
        outward_digits = ''.join(random.choice(string.digits) for _ in range(random.randint(1, 2)))
        outward = outward_letters + outward_digits
        
        inward_digit = random.choice(string.digits)
        inward_letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        inward = inward_digit + inward_letters
        
        return f"{outward} {inward}"
    
    else:
        return ''.join(random.choice(string.digits) for _ in range(5))

def validate_name(name):
    """
    Validate that a name follows the proper pattern:
    - Starts with a capital letter
    - Contains only letters
    - Has a minimum length of 2
    
    Args:
        name: The name to validate
        
    Returns:
        True if the name is valid, False otherwise
    """
    pattern = r'^[A-Z][a-z]+$'
    return bool(re.match(pattern, name)) and len(name) >= 2

def validate_postal_code(postal_code, country_format="US"):
    """
    Validate that a postal code follows the proper pattern for the specified country.
    
    Args:
        postal_code: The postal code to validate
        country_format: The country format to validate against
        
    Returns:
        True if the postal code is valid, False otherwise
    """
    if country_format == "US":
        pattern = r'^\d{5}$'
    elif country_format == "US_EXTENDED":
        pattern = r'^\d{5}-\d{4}$'
    elif country_format == "CA":
        pattern = r'^[A-Z]\d[A-Z] \d[A-Z]\d$'
    elif country_format == "UK":
        pattern = r'^[A-Z]{1,2}\d{1,2} \d[A-Z]{2}$'
    else:
        pattern = r'^\d{5}$'
    
    return bool(re.match(pattern, postal_code))

def generate_test_user_data(country_format="US"):
    """
    Generate a complete set of test user data including first name, last name, and postal code.
    
    Args:
        country_format: The country format to use for the postal code
        
    Returns:
        A dictionary containing the generated user data
    """
    first_name = generate_random_name()
    last_name = generate_random_name()
    postal_code = generate_random_postal_code(country_format)
    
    return {
        "first_name": first_name,
        "last_name": last_name,
        "postal_code": postal_code
    } 