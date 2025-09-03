from typing import Tuple, List, Dict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import pyautogui

def wait_and_get(driver, selemnium_selector: Tuple, timeout: int = 10) -> WebElement:
    """Wait for element to appear and return it."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(selemnium_selector)
    )

# Setting up driver
service = Service("C:\\Users\\liamh\\sandbox\\PokeBot\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# # Navigate to login page from homepage
# driver.get("https://www.target.com")

# # Wait for manual login
# while not os.path.exists("continue.txt"):
#     print("Login and create continue.txt to continue...")
#     time.sleep(3)

# Get page
driver.get("https://www.target.com/p/pokemon-trading-card-game-trick-or-trade-booster-bundle/-/A-87266074#lnk=sametab")

# # Click on item
# item = wait_and_get(driver, (By.CSS_SELECTOR, "div[data-test=\"@web/site-top-of-funnel/ProductCardWrapper\"]"))
# item.click()

# Add to cart
add_to_cart = wait_and_get(driver, (By.CSS_SELECTOR, "[data-test=\"shippingButton\"]"))
add_to_cart.click()

# View cart and checkout (then wait)
go_to_cart = wait_and_get(driver, (By.CSS_SELECTOR, "a[href=\"/cart\"]"))
go_to_cart.click()

# Click 'sign in and checkout' button
wait_and_get(driver, (By.CSS_SELECTOR, "button[data-test=\"checkout-button\"]"))
driver.find_elements(By.CSS_SELECTOR, "button[data-test=\"checkout-button\"]")[-1].click()

# Sign in
email = "liamhade@gmail.com"
password = "target2025"
wait_and_get(driver, (By.CSS_SELECTOR, "input[id=\"username\"]")).click()
pyautogui.write(email)
wait_and_get(driver, (By.CSS_SELECTOR, "input[name=\"password\"]")).send_keys(password)
wait_and_get(driver, (By.CSS_SELECTOR, "button[id=\"login\"]")).click()

# Place order
wait_and_get(driver, (By.CSS_SELECTOR, "button[data-test=\"placeOrderButton\"]"))
driver.find_elements(By.CSS_SELECTOR, "button[data-test=\"placeOrderButton\"]")[-1].click()

# Enter CVV and confirm order
