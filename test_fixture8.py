import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()

class TestMainPage1():
    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("smoke test")

    @pytest.mark.regression # чтобы использовать запуск по маркерам надо написать -m и называние маркера(regression).
    #если в команде есть логика(сразу 2 маркера или более), то эта логика вместе с названеим должна выделяться в ковычки
    #Например, -m "regression or smoke", так будут и регрессион и смоук(да,в этом плане здесь И = ИЛИ)
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("regression test")

    @pytest.mark.skip #пропуск теста
    def test_guest_should_see_basket_link_on_the_main_page2(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("regression test")