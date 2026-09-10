import os # ADD THIS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options # ADD THIS

# ADD THIS WHOLE BLOCK
options = Options()
if os.getenv("CI"): # Jenkins sets this automatically
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-allow-origins=*")
    options.add_argument("--user-data-dir=C:\\Windows\\Temp\\chrome-user-data")

def test_wait():
    driver = webdriver.Chrome(options=options) # CHANGED THIS LINE
    wait = WebDriverWait(driver, 22)

    try: # ADD TRY
        driver.get("https://www.saucedemo.com")
        
        # ADD THIS: only maximize if NOT on Jenkins
        if not os.getenv("CI"):
            driver.maximize_window()

        # Login
        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(
            By.ID, "password"
        ).send_keys("secret_sauce")

        wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        ).click()

        # Add products
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()

        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-bike-light")
            )
        ).click()

        # Open cart
        wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        ).click()

        # Checkout
        wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

        # Customer information
        wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys("Saif")

        driver.find_element(
            By.ID, "last-name"
        ).send_keys("Awan")

        driver.find_element(
            By.ID, "postal-code"
        ).send_keys("22600")

        # Continue
        wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        ).click()

        # Wait for Finish button
        wait.until(
            EC.presence_of_element_located((By.ID, "finish"))
        )

        wait.until(
            EC.element_to_be_clickable((By.ID, "finish"))
        ).click()

        # Wait for successful order message
        success_message = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-header")
            )
        ).text

        print(success_message)

        assert success_message == "Thank you for your order!"

    except Exception as e: # ADD THIS
        driver.save_screenshot("failure_wait.png") # Jenkins will save this
        print(driver.page_source)
        raise e
    finally:
        driver.quit()
