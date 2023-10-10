import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    input_user_name = driver.find_element(By.ID, "user-name")
    input_user_name.clear()
    input_user_name.send_keys("standard_user")

    input_password = driver.find_element(By.ID, "password")
    input_password.clear()
    input_password.send_keys("secret_sauce")

    input_login_button = driver.find_element(By.ID, "login-button")
    input_login_button.submit()

    title_text = driver.find_element(By.CLASS_NAME, "title")

    assert title_text.text == "Products"

    driver.close()
