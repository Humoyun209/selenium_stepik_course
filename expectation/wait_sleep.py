from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")

button = browser.find_element(By.ID, "button")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text