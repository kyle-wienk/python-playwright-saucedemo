from playwright.sync_api import Page, expect

class login_page:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("id=user-name")
        self.password_input = page.locator("id=password")
        self.login_button = page.locator("id=login-button")
    
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

class your_information_checkout_page:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator("id=first-name")
        self.last_name_input = page.locator("id=last-name")
        self.postal_code_input = page.locator("id=postal-code")
        self.continue_button = page.locator("id=continue")
    
    def checkout(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")