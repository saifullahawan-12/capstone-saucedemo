from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_wait():
  driver = webdriver.Chrome()
  driver.get("https://www.saucedemo.com")
  driver.maximize_window()
  wait = WebDriverWait(driver,10)


  driver.find_element(By.ID, "user-name").send_keys("standard_user")
  driver.find_element(By.ID, "password").send_keys("secret_sauce")
  driver.find_element(By.ID, "login-button").click()

  wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
  wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))).click()

  wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
  wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()


  driver.find_element(By.ID, "first-name").send_keys("saif")
  driver.find_element(By.ID, "last-name").send_keys("awan")
  driver.find_element(By.ID, "postal-code").send_keys("22600")
  

  wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()


  wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

  success_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))).text
  print(success_message)
  assert success_message == "Thank you for your order!"

  driver.quit()

