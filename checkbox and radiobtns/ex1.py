import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://suninjuly.github.io/math.html')

try:
    input = browser.find_element(By.ID, 'answer')
    x = browser.find_element(By.XPATH, "//span[@class='nowrap' and @id='input_value']")
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    radio = browser.find_element(By.CSS_SELECTOR, "input#peopleRule")
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    check = radio.get_attribute('checked')

    input_str = str(math.log(abs(12*math.sin(int(x.text)))))

    input.send_keys(input_str)
    checkbox.click()
    radio.click()
    button.click()

    print(check)

finally:
    time.sleep(10)
    browser.quit()