from pages.base_page import BasePage
from config import BASE_URL

class LoginPage(BasePage):
    URL = BASE_URL

    def load(self):
        """Navigate to the login page"""
        self.navigate(self.URL)

    def enter_username(self, username: str):
        """Enter the username in the login form"""
        self.page.locator('[data-test="username"]').fill(username)

    def enter_password(self, password: str):
        """Enter the password in the login form"""
        self.page.locator('[data-test="password"]').fill(password)

    def click_login(self):
        """Click the login button"""
        self.page.locator('[data-test="login-button"]').click()

    def login(self, username: str, password: str):
        """Complete the login process with the provided credentials"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
