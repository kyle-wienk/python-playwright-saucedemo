from playwright.sync_api import Page, expect
import helper_saucedemo_hello_world as helper
import time
import pages

# Test data
STANDARD_USERNAME = "standard_user"
PASSWORD = "secret_sauce"
FIRST_NAME = "Peppa"
LAST_NAME = "Pig"
POSTAL_CODE = "1234"

def test_sauce(page: Page):
    helper.navigate_to_saucedemo(page)
    time.sleep(2)

    login_page = pages.login_page(page)
    login_page.login(STANDARD_USERNAME, PASSWORD)
    time.sleep(2)

    helper.open_backpack_product_page(page)
    time.sleep(2)

    helper.add_backpack_to_cart(page)
    time.sleep(2)

    helper.open_cart(page)
    time.sleep(2)

    helper.open_checkout(page)
    time.sleep(2)

    your_information_checkout_page = pages.your_information_checkout_page(page)
    your_information_checkout_page.checkout(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    time.sleep(2)

    helper.complete_checkout_step_2(page)
    time.sleep(2)

    helper.logout(page)
    time.sleep(2)