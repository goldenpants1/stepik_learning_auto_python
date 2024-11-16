from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math

link = "https://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    browser.switch_to.alert.accept()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    print(y)
    browser.find_element(By.ID, "answer").send_keys(y)
    #browser.find_element(By.ID, "robotCheckbox").click()
    #rule_robot = browser.find_element(By.ID, "robotsRule")
    #browser.execute_script("return arguments[0].scrollIntoView(true)", rule_robot)
    #rule_robot.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true)", submit_button)
    submit_button.click()
    print(browser.switch_to.alert.text.split()[-1])#выводит число-ответ из модалки при успехе задания


    # browser.execute_script("alert('Robots at work');")
    # пример
    # browser.execute_script("document.title='Script executing';")
    # пример 2
    # browser.execute_script("document.title='Script executing';alert('Robots at work');")
    # Пример выполнение сразу нескольких инструкций
    # "return arguments[0].scrollIntoView(true);"
    # пример. как можно проскролить страницу
    # browser.execute_script("window.scrollBy(0, 100);")
    # пример, как можно проскролить страницу на определённое кол-во пикселей
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()