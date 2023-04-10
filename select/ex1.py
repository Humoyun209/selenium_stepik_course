import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')


try:
    select = browser.find_element(By.TAG_NAME, 'select')
    btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    num1 = browser.find_element(By.ID, 'num1')
    num2 = browser.find_element(By.ID, 'num2')
    s = int(num2.text) + int(num1.text)
    select.click()

    options = browser.find_elements(By.TAG_NAME, 'option')
    for option in options:
        val = option.get_attribute('value')
        if val.isdigit() and int(val) == s:
            option.click()
            btn.click()

finally:
    time.sleep(10)