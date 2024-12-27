import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default= "chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: '--language=en' or '--language=ru'")

@pytest.fixture(scope="function")
def browser(request):
    # для выбора языка вообще
    user_language = request.config.getoption("language")
    # для выбора языка в браузере (Хром)
    options = Options()
    options.add_experimental_option('prefs', {'intil.accept_languages': user_language})
    # для выбора языка в браузере (Фаерфокс)
    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intil.accept_languages", user_language)
    # Для выбора браузера
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test...")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test...")
        browser = webdriver.Firefox(options=options_firefox)
    yield browser
    print("\nquit browser...")
    browser.quit()