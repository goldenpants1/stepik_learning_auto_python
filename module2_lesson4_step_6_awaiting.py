from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
#browser.implicitly_wait(5)
# staleness_of(element) - штука, которая наоборот ждёт когда исчезнет какой-то элемент, анимация, например
browser.get("https://suninjuly.github.io/cats.html")

browser.find_element(By.ID, "button")
