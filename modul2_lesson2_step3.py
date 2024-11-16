from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

#link = "https://suninjuly.github.io/selects1.html"
link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    number_1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    number_2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    def calc(number_1, number_2):
        return str(int(number_1) + int(number_2))
    c = calc(number_1,number_2)
    print(c)
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(c))
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()