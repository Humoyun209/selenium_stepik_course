import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

current = os.path.abspath(os.path.dirname(__file__))
file_join = os.path.join(current, 'file.txt')


try:
    name = browser.find_element(By.NAME, 'firstname')
    lastname = browser.find_element(By.NAME, 'lastname')
    email = browser.find_element(By.NAME, 'email')
    file = browser.find_element(By.ID, 'file')
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    name.send_keys('IvanAli')
    lastname.send_keys('IvanXujaev')
    email.send_keys('Ivan@mail.ru')
    file.send_keys(file_join)
    button.click()
finally:
    time.sleep(5)
    browser,quit()


