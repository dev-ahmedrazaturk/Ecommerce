import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

use_lambdatest = bool(os.getenv("LT_USERNAME") and os.getenv("LT_ACCESS_KEY"))

if use_lambdatest:
    caps = {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "LT:Options": {"platformName": "Windows 11", "build": "GitLab CI Demo", "name": "basic-sanity"}
    }
    grid_url = f"https://{os.environ['LT_USERNAME']}:{os.environ['LT_ACCESS_KEY']}@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(command_executor=grid_url, options=webdriver.ChromeOptions(), desired_capabilities=caps)
else:
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=opts)

driver.get("https://example.com")
assert "Example Domain" in driver.title
print("Title OK:", driver.title)
driver.quit()
