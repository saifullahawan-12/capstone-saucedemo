import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
if os.getenv("CI"):
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-allow-origins=*")
    options.add_argument("--user-data-dir=C:\\Windows\\Temp\\chrome-user-data")

def test_checkout():
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 16)
    
    try:
        driver.get("https://www.saucedemo.com")
        
        # Login + add 1 item
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))).click()
        
        # Checkout flow
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Test")
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()
        
        # Verify success
        success = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
        assert "Thank you" in success.text
        
    except Exception as e:
        driver.save_screenshot("failure_checkout.png")
        print(driver.page_source)
        raise e
    finally:
        driver.quit()
