import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_quest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_quest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")

#pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py