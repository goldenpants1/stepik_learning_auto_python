from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage1():
    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..testMainPage1")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..testMainPage1")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("нашли кнопку логина на странице 1")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("логин на странице 1")

class TestMainPage2():
    def setup_method(self):
        print("start browser for test... testMainPage2")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test... testMainPage2")
        self.browser.quit()

    def test_quest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("нашли кнопку логина на странице 2")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("перешли по ссылке на странице 2")