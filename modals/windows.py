import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

try:
    button = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    num = int(x.text)

    input = browser.find_element(By.ID, 'answer')
    btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    s = str(math.log(abs(12 * math.sin(num))))

    input.send_keys(s)
    btn.click()
finally:
    time.sleep(3)
    browser.quit()