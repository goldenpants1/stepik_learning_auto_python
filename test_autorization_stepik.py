import time
import pytest
import math
import creds
from selenium import webdriver
from selenium.webdriver.common.by import By

arrayLinks = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

@pytest.mark.parametrize('link', arrayLinks)
def test_autorization_stepk(browser, link):
    link = f"{link}"
    #link = "https://stepik.org/lesson/236895/step/1"
    #browser.implicitly_wait(10)
    browser.get(link)
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "nav#main-navbar>a:nth-of-type(2)").click()
    browser.find_element(By.CSS_SELECTOR, "input[name='login']").send_keys(creds.login)
    browser.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(creds.password)
    browser.find_element(By.CSS_SELECTOR, "form#login_form>button").click()#Кнопка "Войти"
    time.sleep(10)
    filed = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area.ember-view")
    #browser.find_element(By.CSS_SELECTOR, "button.again-btn.white").click()#Кнопка очистки поля(она не всегда есть)
    #browser.find_element(By.XPATH, "//button[text()='OK']").click()#Подтверждение очистки поля(поап)
    answer = math.log(int(time.time()))
    print(answer)
    filed.send_keys(answer)
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    time.sleep(5)
    x_element = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    assert x_element == "Correct!", f"Произошла ошибка, текст ошибки: {x_element}"
