from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x_value_element = x_element.get_attribute("valuex")#get.attribute - функция получения значения атрибута.
    # Если атрибут есть, и у него есть значение, то в ответе будет это значение строкой.
    # Если атрибут есть, но нет значения, то в ответе будет "true", но строкой.
    # Если атрибута вообще не будет, то в ответе будет None - как значение(не строка)
    x = x_value_element
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    print(y)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)#вводим игрик в поле
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()#прожимаем чекбокс
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()#прожимаем радиобатон
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()#кнопка субмит
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()