import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

try:
    button = browser.find_element(By.CSS_SELECTOR, 'button#book')
    txt = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, 'h5#price'), '$100'
    ))
    button.click()

    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    num = int(x.text)

    input = browser.find_element(By.ID, 'answer')
    btn = browser.find_element(By.CSS_SELECTOR, 'button#solve')
    s = str(math.log(abs(12 * math.sin(num))))

    input.send_keys(s)
    btn.click()
finally:
    time.sleep(5)
    browser.quit()
