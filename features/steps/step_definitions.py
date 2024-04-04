from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys

# Define global variables
base_url = "https://www.saucedemo.com/"
screenshot_path = "screenshots/"

def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

# Function to take screenshot
def take_screenshot(driver, screenshot_name):
    driver.save_screenshot(screenshot_path + screenshot_name + ".png")


# Scenario 1: Successful Login
@given('I am on the Demo Login Page')
def visit_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get(base_url)

@when('I fill the account information for account StandardUser into the Username field and the Password field')
def fill_standard_user_credentials(context):
    username_field = context.driver.find_element(By.ID, 'user-name')
    password_field = context.driver.find_element(By.ID, 'password')
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")

@when('I click the Login Button')
def click_login_button(context):
    login_button = context.driver.find_element(By.ID, 'login-button')
    login_button.click()
    
@then('I am redirected to the Demo Main Page')
def verify_redirected_to_main_page(context):
    try:
        alert = context.driver.switch_to.alert
        alert.accept()
    except NoAlertPresentException:
        pass
    assert context.driver.current_url == base_url + "inventory.html"
    take_screenshot(context.driver, "successful_login")

@then('I verify the App Logo exists')
def verify_app_logo(context):
    app_logo = context.driver.find_element(By.CLASS_NAME, 'app_logo')
    assert app_logo.is_displayed()

# Scenario 2: Failed Login
@given('I am on the Sauce Demo Login Page')
def visit_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get(base_url)

@when('I fill the account information for account LockedOutUser into the Username field and the Password field')
def fill_locked_out_user_credentials(context):
    username_field = context.driver.find_element(By.ID, 'user-name')
    password_field = context.driver.find_element(By.ID, 'password')
    username_field.send_keys("locked_out_user")
    password_field.send_keys("secret_sauce")

@then('I verify the Error Message contains the text "Sorry, this user has been banned."')
def verify_error_message(context):
    error_message = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
    assert "Epic sadface: Sorry, this user has been locked out." in error_message.text
    take_screenshot(context.driver, "failed_login")

# Scenario 3: Order a product
@given('I am on the inventory page')
def visit_inventory_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get(base_url)
    context.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    context.driver.find_element(By.ID, 'login-button').click()
    try:
        alert = context.driver.switch_to.alert
        alert.accept()
    except NoAlertPresentException:
        pass
    context.driver.get(base_url + "inventory.html")

@when('user sorts products from low price to high price')
def sort_products_low_to_high(context):
    sort_dropdown = context.driver.find_element(By.CLASS_NAME, 'product_sort_container')
    sort_dropdown.click()
    option_low_to_high = context.driver.find_element(By.XPATH, "//option[@value='lohi']")
    option_low_to_high.click()

@when('user adds lowest priced product')
def add_lowest_priced_product(context):
    add_to_cart_buttons = context.driver.find_elements(By.CLASS_NAME, 'btn_primary')
    add_to_cart_buttons[0].click()

@when('user clicks on cart')
def click_cart(context):
    cart_button = context.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_button.click()
    take_screenshot(context.driver, "added_to_cart")

@when('user clicks on checkout')
def click_checkout(context):
    checkout_button = context.driver.find_element(By.ID, 'shopping_cart_container')
    checkout_button.click()
    checkout = context.driver.find_element(By.ID, 'checkout')
    checkout.click()
    take_screenshot(context.driver, "checkout")

@when('user enters first name John')
def enter_firstName(context):
    first_name = context.driver.find_element(By.ID, 'first-name')
    first_name.send_keys('John')

@when('user enters last name Doe')
def enter_lastName(context):
    last_name = context.driver.find_element(By.ID, 'last-name')
    last_name.send_keys('Doe')

@when('user enters zip code 123')
def enter_zipcode(context):
    zipcode = context.driver.find_element(By.ID, 'postal-code')
    zipcode.send_keys('123')

@when('user clicks Continue button')
def click_continue(context):
    continue_btn = context.driver.find_element(By.XPATH, '//input[@type="submit" and @id="continue"]')
    continue_btn.click()

@then('I verify in Checkout overview page if the total amount for the added item is $8.63')
def verify_total_amt(context):
    total_amount_element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'summary_total_label')))
    total_amount_text = total_amount_element.text
    total_amount_value = float(total_amount_text.split('$')[1].strip())
    assert total_amount_value == 8.63, f"Total amount is not $8.63, actual amount is {total_amount_value}"
    take_screenshot(context.driver, "checkout_overview_page")

@when('user clicks Finish button')
def click_finish(context):
    finish_btn = WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.XPATH,'//button[contains(text(),"Finish")]')))
    scroll_to_element(context.driver, finish_btn)
    finish_btn = WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(),"Finish")]')))
    finish_btn.click()

@then('Thank You header is shown in Checkout Complete page')
def thankyou_header(context):
    thank_you_header_element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'complete-header')))
    assert thank_you_header_element.is_displayed(), "Thank You header is not displayed on the Checkout Complete page"
    take_screenshot(context.driver, "thank_you")

# Cleanup after each scenario
def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()

