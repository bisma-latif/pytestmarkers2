from pytest import mark
from selenium import webdriver


@mark.entertainment
def test_entertainment_func_as_expected():
    browser = webdriver.Chrome('../seleniumSession/chromedriver/chromedriver.exe')
    browser.get("https://www.google.com")
    assert True
