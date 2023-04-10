import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        name = browser.find_element(By.CSS_SELECTOR, '.first_block  .first')
        family = browser.find_element(By.CSS_SELECTOR, '.first_block  .second')
        email = browser.find_element(By.CSS_SELECTOR, '.first_block  .third')

        name.send_keys('Ivanxuja')
        family.send_keys('Ivanbek')
        email.send_keys('Ivanali')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        name = browser.find_element(By.CSS_SELECTOR, '.first_block  .first')
        family = browser.find_element(By.CSS_SELECTOR, '.first_block  .second')
        email = browser.find_element(By.CSS_SELECTOR, '.first_block  .third')

        name.send_keys('Ivanxuja')
        family.send_keys('Ivanbek')
        email.send_keys('Ivanali')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


if __name__ == '__main__':
    unittest.main()