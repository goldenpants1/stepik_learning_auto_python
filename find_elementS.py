# подготовка для теста
# открываем страницу первого товара
# данный сайт не существует, этот код приведен только для примера
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get("https://fake-shop.com/book1.html")

# добавляем товар в корзину
browser.find_element(By.CSS_SELECTOR, ".add").click()


# открываем страницу второго товара
browser.get("https://fake-shop.com/book2.html")

# добавляем товар в корзину
add_button = browser.find_element(By.CSS_SELECTOR, ".add")
add_button.click()

# тестовый сценарий
# открываем корзину
browser.get("https://fake-shop.com/basket.html")

# ищем все добавленные товары
goods = browser.find_elements(By.CSS_SELECTOR, ".good")

# проверяем, что количество товаров равно 2
assert len(goods) == 2

#!Важно. Обратите внимание на важную разницу в результатах, которые возвращают методы find_element и find_elements.
#Если первый метод не смог найти элемент на странице,
# то он вызовет ошибку NoSuchElementException, которая прервёт выполнение вашего кода.
#Второй же метод всегда возвращает валидный результат: если ничего не было найдено, то он вернёт пустой список и ваша
#программа перейдет к выполнению следующего шага в коде.
