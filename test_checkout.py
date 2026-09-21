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
    wait = WebDriverWait(driver, 25)
    try:
        driver.get("https://www.saucedemo.com")
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
        wait.until(EC.url_contains("cart.html"))
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        # FIX 1: wait for each field separately - this is the main fix
        first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        first_name.clear()
        first_name.send_keys("Test")

        last_name = wait.until(EC.visibility_of_element_located((By.ID, "last-name")))
        last_name.clear()
        last_name.send_keys("User")

        postal = wait.until(EC.visibility_of_element_located((By.ID, "postal-code")))
        postal.clear()
        postal.send_keys("12345")

        # FIX 2: scroll + js click
        continue_btn = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
        driver.execute_script("arguments[0].scrollIntoView(true);", continue_btn)
        driver.execute_script("arguments[0].click();", continue_btn)

        # FIX 3: if it still stays on same page, print the error
        try:
            wait.until(EC.url_contains("checkout-step-two.html"))
        except:
            try:
                error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
                print(f"VALIDATION ERROR ON PAGE: {error}")
            except:
                print("No error message found, but stayed on step-one")
            raise

        finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        driver.execute_script("arguments[0].scrollIntoView(true);", finish_btn)
        driver.execute_script("arguments[0].click();", finish_btn)

        success = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
        assert "Thank you" in success.text
        print(f"SUCCESS: {success.text}")

    except Exception as e:
        driver.save_screenshot("failure_checkout.png")
        print(f"URL FAILED AT: {driver.current_url}")
        raise e
    finally:
        driver.quit()
