from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get("https://elzero.org/")

print(browser.title)


# browser.find_element(By.ID, 'search').send_keys("Front End Developer")

# browser.driver.find_element(By.CSS_SELECTOR, 'input.search-submit').click()
