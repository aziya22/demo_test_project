from selenium import webdriver
from selenium.webdriver.common.by import By

# Function to automate successful login
def successful_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get(base_url)
    username_field = context.driver.find_element(By.ID, 'user-name')
    password_field = context.driver.find_element(By.ID, 'password')
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button = context.driver.find_element(By.ID, 'login-button')
    login_button.click()
    assert context.driver.current_url == base_url + "inventory.html"
    app_logo = context.driver.find_element(By.CLASS_NAME, 'app_logo')
    assert app_logo.is_displayed()

# Function to automate failed login
def failed_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get(base_url)
    username_field = context.driver.find_element(By.ID, 'user-name')
    password_field = context.driver.find_element(By.ID, 'password')
    username_field.send_keys("locked_out_user")
    password_field.send_keys("secret_sauce")
    login_button = context.driver.find_element(By.ID, 'login-button')
    login_button.click()
    error_message = context.driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert "Sorry, this user has been banned." in error_message.text

# Function to automate order a product scenario
def order_product(context):
    context.driver.get(base_url + "inventory.html")
    sort_dropdown = context.driver.find_element(By.CLASS_NAME, 'product_sort_container')
    sort_dropdown.click()
    option_low_to_high = context.driver.find_element(By.XPATH, "//option[@value='lohi']")
    option_low_to_high.click()
    
    # Click on the first product to add to cart
    add_to_cart_button = context.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
    add_to_cart_button.click()
    
    # Click on the shopping cart icon to proceed to checkout
    shopping_cart_icon = context.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    shopping_cart_icon.click()
    
    # Click on the checkout button
    checkout_button = context.driver.find_element(By.XPATH, "//a[@class='btn_action checkout_button']")
    checkout_button.click()
    
    # Enter user information
    first_name_field = context.driver.find_element(By.ID, 'first-name')
    last_name_field = context.driver.find_element(By.ID, 'last-name')
    zip_code_field = context.driver.find_element(By.ID, 'postal-code')
    
    first_name_field.send_keys("John")
    last_name_field.send_keys("Doe")
    zip_code_field.send_keys("123")
    
    # Click on the continue button to proceed
    continue_button = context.driver.find_element(By.XPATH, "//input[@value='CONTINUE']")
    continue_button.click()
    
    # Verify total amount in Checkout overview page
    total_amount_element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'summary_total_label')))
    total_amount_text = total_amount_element.text
    total_amount_value = float(total_amount_text.split('$')[1].strip())
    assert total_amount_value == 8.63, f"Total amount is not $8.63, actual amount is {total_amount_value}"
    
    # Click on the finish button to complete the order
    finish_button = context.driver.find_element(By.XPATH, "//button[contains(text(),'Finish')]")
    finish_button.click()
    
    # Verify Thank You header on Checkout Complete page
    thank_you_header_element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'complete-header')))
    
    assert thank_you_header_element.is_displayed(), "Thank You header is not displayed on the Checkout Complete page"

# Call functions to run scenarios
successful_login()
failed_login()
order_product()
