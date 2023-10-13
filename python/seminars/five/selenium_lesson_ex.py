import time

from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.google.com/")
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("GeekBrains")
    elem.submit()
    time.sleep(3)
    driver.quit()
