from pytest import mark
from selenium import webdriver


@mark.body
class bodyTests:

    @mark.ui
    def test_body_func_as_expected(self):
        browser = webdriver.Chrome('../seleniumSession/chromedriver/chromedriver.exe')
        browser.get("https://www.google.com")
        assert True

    def test_body2_func_as_expected(self):
        browser = webdriver.Chrome('../seleniumSession/chromedriver/chromedriver.exe')
        browser.get("https://www.google.com")
        assert True

    def test_body3_func_as_expected(self):
        browser = webdriver.Chrome('../seleniumSession/chromedriver/chromedriver.exe')
        browser.get("https://www.google.com")
        assert True
