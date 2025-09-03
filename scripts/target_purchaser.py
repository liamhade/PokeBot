from typing import Tuple, List, Dict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import csv
import time

def wait_and_get(driver, selemnium_selector: Tuple, timeout: int = 10) -> WebElement:
    """Wait for element to appear and return it."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(selemnium_selector)
    )

# def get_cookies(cookie_file: str) -> List[Dict]:
#     """Read cookies from a CSV file and return them as a list of dictionaries."""
#     with open(cookie_file, newline='\n') as f:
#         reader = csv.DictReader(f)
#         return [row for row in reader]
    
# def grab_cookies_from_txt(file: str) -> List[Dict]:
#     """Reads a .txt file containing cookies in 'name=value; name2=value2' format and returns a dictionary of cookies."""
#     with open(file, 'r') as f:
#         cookie_string = f.read()
#     cookies = []
#     for cookie in cookie_string.split('; '):
#         name, value = cookie.split('=', 1)
#         cookies.append({"name": name, "value": value})
#     return cookies

email = "liamhade@gmail.com"
password = "target2025"

# Setting up driver
service = Service("C:\\Users\\liamh\\sandbox\\PokeBot\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Navigate to login page from homepage
driver.get("https://www.target.com")

wait_and_get(driver, (By.ID, "account-sign-in")).click()
wait_and_get(driver, (By.CSS_SELECTOR, "button[data-test=\"accountNav-signIn\"]")).click()

# Send credentials and press enter
wait_and_get(driver, (By.ID, "username")).send_keys(email)
wait_and_get(driver, (By.ID, "login")).click()
wait_and_get(driver, (By.ID, "password")).send_keys(password)

# Get page
driver.get("https://www.target.com/s?searchTerm=Pokemon")

# Adding cookies to the driver
cookie_file = 'C:\\Users\\liamh\\sandbox\\PokeBot\\statics\\target_cookies.txt'
for cookie in grab_cookies_from_txt(cookie_file):
    driver.add_cookie(cookie)

# Click on item
item = wait_and_get(driver, (By.CSS_SELECTOR, "div[data-test=\"@web/site-top-of-funnel/ProductCardWrapper\"]"))
item.click()

# Add to cart
add_to_cart = wait_and_get(driver, (By.CSS_SELECTOR, "[data-test=\"shippingButton\"]"))
add_to_cart.click()

# View cart and checkout (then wait)
checkout = wait_and_get(driver, (By.CSS_SELECTOR, "a[href=\"/cart\"]"))
checkout.click()


input()
"""
Make sure already logged in to Target account, and the accounts have shipping addresses and payment methods saved.
"""

# Place order


# Enter CVV and confirm order
