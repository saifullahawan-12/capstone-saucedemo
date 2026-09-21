import tempfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def get_chrome_options():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-allow-origins=*")
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
    return options

def test_checkout():
    driver = webdriver.Chrome(options=get_chrome_options())
    wait = WebDriverWait(driver, 20)
    try:
        driver.get("https://www.saucedemo.com")
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Test")
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("12345")

        wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

        # FIX: scroll to finish button - headless needs this
        finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        driver.execute_script("arguments[0].scrollIntoView(true);", finish_btn)
        finish_btn.click()

        success = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
        assert "Thank you" in success.text
        print("Checkout PASS")
    except Exception as e:
        driver.save_screenshot("failure_checkout.png")
        print(f"Current URL: {driver.current_url}")
        raise e
    finally:
        driver.quit()
