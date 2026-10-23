from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver



@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    web = webdriver.Chrome(options=options)
    web.maximize_window()
    web.implicitly_wait(5)
    yield web
    web.close()