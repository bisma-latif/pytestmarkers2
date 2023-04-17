from pytest import mark
from selenium import webdriver


browser = webdriver.Chrome('../seleniumSession/chromedriver/chromedriver.exe')
browser.get("https://www.google.com")


@mark.ui
def test_engine_func_as_expected():
    # browser.get("https://www.google.com")
    assert True
