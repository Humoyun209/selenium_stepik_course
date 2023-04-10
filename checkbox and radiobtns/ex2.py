import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/get_attribute.html')

try:
    input = browser.find_element(By.ID, 'answer')
    img = browser.find_element(By.XPATH, "//img[@valuex]")
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    radio = browser.find_element(By.CSS_SELECTOR, "input#RobotsRule")
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')

    x_text = img.get_attribute('valuex')

    x_s = str(math.log(abs(12*math.sin(int(x_text)))))

    input.send_keys(x_s)
    checkbox.click()
    radio.click()
    button.click()


finally:
    time.sleep(5)