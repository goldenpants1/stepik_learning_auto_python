import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def registration(link):

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

def test_registration_function():
    link1 ="http://suninjuly.github.io/registration1.html"
    result1 = registration(link1)
    assert result1 == "Congratulations! You have successfully registered!", "Error, bro..."

def test_registration_function_2():
    link2 = "http://suninjuly.github.io/registration2.html"
    result2 = registration(link2)
    assert result2 == "Congratulations! You have successfully registered!", "Error, bro..."