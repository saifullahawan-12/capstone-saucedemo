from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_checkout():

   driver = webdriver.Chrome()
   driver.get("https://www.saucedemo.com")
   driver.maximize_window()

   driver.find_element(By.ID, "user-name").send_keys("standard_user")
   driver.find_element(By.ID, "password").send_keys("secret_sauce")
   driver.find_element(By.ID, "login-button").click()
   time.sleep(3)

   buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
   for button in buttons:
     button.click()
     time.sleep(1)

   driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
   time.sleep(1)

   driver.find_element(By.ID, "checkout").click()
   time.sleep(1)

   driver.find_element(By.ID, "first-name").send_keys("standard_user")
   driver.find_element(By.ID, "last-name").send_keys("secret_sauce")
   driver.find_element(By.ID, "postal-code").send_keys("22600")
   time.sleep(1)

   driver.find_element(By.ID, "continue").click()
   time.sleep(1)
   driver.find_element(By.ID, "finish").click()
   time.sleep(1)

   success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
   print(success_message)
   assert success_message == "Thank you for your order!"
   driver.quit()