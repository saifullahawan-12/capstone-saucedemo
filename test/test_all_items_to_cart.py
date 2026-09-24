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
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-allow-origins=*")
   
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
    return options

def test_all_items_to_cart():
    driver = webdriver.Chrome(options=get_chrome_options())
    wait = WebDriverWait(driver, 15)
    try:
        driver.get("https://www.saucedemo.com")
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory")))
        for item in items:
            driver.execute_script("arguments[0].click();", item)

        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        driver.execute_script("arguments[0].click();", cart_button)

        cart_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item")))
        assert len(cart_items) == 6
        print("SUCCESS: All 6 items in cart")
    except Exception as e:
        driver.save_screenshot("failure_all_items.png")
        raise e
    finally:
        driver.quit()