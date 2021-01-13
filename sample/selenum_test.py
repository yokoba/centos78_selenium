from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options

CHROME_DRIVER = "./chromedriver"

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(executable_path=CHROME_DRIVER, chrome_options=options)

driver.get("https://google.com")

print(f"document title :{driver.title}")
