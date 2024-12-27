import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestingCheats(unittest.TestCase):

    def registration(self, link):
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Евгений")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Смоктуновский")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("asdq@test.ru")
        browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

        # закрываем браузер после всех манипуляций
        browser.quit()

        return welcome_text

    def test_registration_function(self):
            link1 ="http://suninjuly.github.io/registration1.html"
            result1 = self.registration(link1)
            self.assertEqual(("Congratulations! You have successfully registered!"), result1)

    def test_registration_function_2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        result2 = self.registration(link2)
        self.assertEqual(("Congratulations! You have successfully registered!"), result2)

if __name__ == "__main__":
    unittest.main()