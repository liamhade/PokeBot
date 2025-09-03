from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch Chromium (headless=False shows the browser window)
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Go to a page
    base_url = "https://www.target.com"
    page.goto("https://www.target.com/s?searchTerm=Pokemon")

    # Click a link by its text
    items = page.locator("a[data-test='product-title']")
    num_items = items.count()

    # Going to the 5th item
    item_url = base_url + items.nth(5).get_attribute("href")
    page.goto(item_url)

    # Try to add to cart
    page.click("button[data-test='shippingButton']")

    # View cart and checkout (then wait)
    page.click("a[href='/cart']")

    # Click 'sign in and checkout' button 
    page.click("button[data-test='checkout-button']")

    # Sign in
    email = "liamhade@gmail.com"
    password = "target2025"
    page.type("input[name='username']", email, delay=25)  # Typing with a delay to mimic human behavior
    page.type("input[name='password']", password, delay=33)
    page.click("button[id='login']")

    # Place order
    page.click("button[data-test='placeOrderButton']")

    # Enter CVV and confirm order
    page.type("input[id='enter-cvv']", "123", delay=30)  # Typing CVV with a delay
    page.click("button[data-test='confirm-button']")

    input("Done")
