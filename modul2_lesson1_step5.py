from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
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