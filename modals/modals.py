import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

try:
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    num = int(x.text)

    input = browser.find_element(By.ID, 'answer')
    btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    s = str(math.log(abs(12 * math.sin(num))))

    input.send_keys(s)
    btn.click()

finally:
    time.sleep(5)
    browser.quit()
