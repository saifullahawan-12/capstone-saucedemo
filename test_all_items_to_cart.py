from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_all_to_cart():
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for button in buttons:
        button.click()
        time.sleep(2)

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    cart_badge == "6", f"expected 6 but got {cart_badge}"

    driver.quit()