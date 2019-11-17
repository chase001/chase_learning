import pytest
from selenium import webdriver


@pytest.mark.nondestructive
def test_nondestructive(selenium):
    driver = webdriver.Chrome(r"/Users/yinyuting/node_modules/chromedriver/lib/chromedriver/chromedriver")
    # selenium.get('http://www.baidu.com')
