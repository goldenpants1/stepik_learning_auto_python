from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(10)
# staleness_of(element) - штука, которая наоборот ждёт когда исчезнет какой-то элемент, анимация, например
browser.get("https://suninjuly.github.io/explicit_wait2.html")
try:
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, "book").click()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    print(y)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "solve").click()
    print(browser.switch_to.alert.text.split()[-1])

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()