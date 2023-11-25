from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.wait import WebDriverWait


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 

s = Service(r"C:\Users\a\Desktop\Lern python\Nouveau dossier\chromedriver.exe")

driver = webdriver.Chrome(options=options,service=s)

driver.get("http://localhost:3000/")

driver.find_element(by=By.XPATH, value='//*[@id=":r1:"]').send_keys("test@test.com")

driver.implicitly_wait(5)

driver.find_element(by=By.XPATH, value='//*[@id=":r3:"]').send_keys("1234567")

driver.implicitly_wait(5)

driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/form/button[1]').click()

driver.implicitly_wait(5)

# driver.quit()

# driver.find_element(by=By.XPATH, value='//*[@id=":r1:"]').send_keys("test@test.com")

# driver.find_element(By.ID, 'search').send_keys("Front End Developer")

# browser.driver.find_element(By.CSS_SELECTOR, 'input.search-submit').click()
