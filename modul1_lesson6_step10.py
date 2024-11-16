from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    #link = "http://suninjuly.github.io/registration1.html"
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
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()