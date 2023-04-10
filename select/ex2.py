import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/execute_script.html')\

try:
    x = browser.find_element(By.ID, 'input_value')
    res = math.log(abs(12 * math.sin(int(x.text))))

    btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    input = browser.find_element(By.ID, 'answer')
    check = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")

    input.send_keys(str(res))
    browser.execute_script("return arguments[0].scrollIntoView(true)", btn)
    check.click()
    radio.click()
    btn.click()

finally:
    time.sleep(10)
    browser.quit()