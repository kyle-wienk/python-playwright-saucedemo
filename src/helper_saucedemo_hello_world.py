from playwright.sync_api import Page, expect

# TODO: Generally move away from a basic procedural paradigm/style
# TODO: Remove hardcoded test data from functions
# TODO: Refactor to a test functions file and page classes file
# TODO: Increase validations quality and quantity

def navigate_to_saucedemo(page: Page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")

def login_standard(page: Page):
    user_name_input = page.locator("id=user-name")
    password_input = page.locator("id=password")
    login_button = page.locator("id=login-button")
    user_name_input.fill("standard_user")
    password_input.fill("secret_sauce")
    login_button.click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def open_backpack_product_page(page: Page):
    backpack_link = page.locator("text=Sauce Labs Backpack")
    backpack_link.click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory-item.html?id=4")

def add_backpack_to_cart(page: Page):
    backpack_add_to_cart = page.locator("id=add-to-cart-sauce-labs-backpack")
    backpack_add_to_cart.click()
    expect(page.locator("id=remove-sauce-labs-backpack")).to_be_visible()

def open_cart(page: Page):
    cart_link = page.locator("id=shopping_cart_container")
    cart_link.click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

def open_checkout(page: Page):
    checkout_button = page.locator("id=checkout")
    checkout_button.click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

def complete_checkout_step_1(page: Page):
    first_name_input = page.locator("id=first-name")
    last_name_input = page.locator("id=last-name")
    postal_code_input = page.locator("id=postal-code")
    continue_button = page.locator("id=continue")
    first_name_input.fill("Derek")
    last_name_input.fill("Zoolander")
    postal_code_input.fill("1234")
    continue_button.click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

def complete_checkout_step_2(page: Page):
    finish_button = page.locator("id=finish")
    finish_button.click()
    expect(page).not_to_have_url("https://www.saucedemo.com/checkout-complete.html")


def logout(page: Page):
    menu_button = page.locator("id=react-burger-menu-btn")
    logout_button = page.locator("id=logout_sidebar_link")
    if logout_button.is_hidden():
        menu_button.click()
    logout_button.click()
    expect(page).to_have_url("https://www.saucedemo.com/")