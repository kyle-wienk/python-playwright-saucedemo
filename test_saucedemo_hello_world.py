from playwright.sync_api import Page, expect
import helper_saucedemo_hello_world as helper
import time


def test_sauce(page: Page):
    helper.navigate_to_saucedemo(page)
    time.sleep(2)

    helper.login_standard(page)
    time.sleep(2)

    helper.open_backpack_product_page(page)
    time.sleep(2)

    helper.add_backpack_to_cart(page)
    time.sleep(2)

    helper.open_cart(page)
    time.sleep(2)

    helper.open_checkout(page)
    time.sleep(2)

    helper.complete_checkout_step_1(page)
    time.sleep(2)

    helper.complete_checkout_step_2(page)
    time.sleep(2)

    helper.logout(page)
    time.sleep(2)