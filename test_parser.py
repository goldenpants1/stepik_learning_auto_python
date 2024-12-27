import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_ques_should_see_login(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

#pytest -s -v --browser_name=firefox test_parser.py
#pytest -s -v --browser_name=chrome test_parser.py
#по умолчанию сейчас будет открываться хром, это настройка из файла conftest