import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
try:
    x = int(browser.find_element(By.ID, 'input_value').text)
    s = math.log(abs(12 * math.sin(x)))
    inp = browser.find_element(By.ID, 'answer')
    inp.send_keys(str(s))

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    check = browser.find_element(By.XPATH, "//label[@for='robotCheckbox']")
    rad = browser.find_element(By.XPATH, "//label[@for='robotsRule']")
    check.click()
    rad.click()
    button.click()

finally:
    time.sleep(20)
    browser.quit()