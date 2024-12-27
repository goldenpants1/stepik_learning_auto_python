import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('language', ["ru", "en-gb"])#Если параметров больше одного, то надо просто больше таких записей
#делать, т.е. @pytest... два раза писать, если 2 параметра, и т.д.. Так же можно это делать сразу для целого класса
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")