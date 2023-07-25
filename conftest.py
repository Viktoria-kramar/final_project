import pytest
from selenium import webdriver


# фикстура для запуска тестов через интерпретатор
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)

    yield driver

    driver.quit()
