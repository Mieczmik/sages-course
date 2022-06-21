from selenium import webdriver
from selenium.webdriver.common import by
import pytest
import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.logger import log
from webdriver_manager.utils import ChromeType, os_name, OSType

URL = 'https://github.com/mikulskibartosz/sages_data_sources/tree/rozwiazania/input_data/markdown'

@pytest.fixture(scope='function')
def driver():
    binary_location = {
        OSType.LINUX: "/usr/bin/brave-browser",
        OSType.MAC: "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
        OSType.WIN: f"{os.getenv('LOCALAPPDATA')}\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
    }[os_name()]
    log(binary_location)
    option = webdriver.ChromeOptions()
    option.binary_location = binary_location
    driver_path = ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()
    driver = webdriver.Chrome(driver_path, options=option)

    yield driver
    driver.quit()


def test_check_if_driver_works(driver):
    """To jest test sprawdzający czy Selenium zostało poprawnie zainstalowane."""
    driver.get(URL)
    assert driver.current_url == URL


def test_load_page_using_selenium(driver):
    """Wczytaj stronę której adres znajduje się w zmiennej URL przy użyciu biblioteki selenium.
    Użyj selenium do wczytania tytułu strony.

    Podpowiedź: webdriver.Safari() jest wbudowany w selenium i nie wymaga dodatkowej instalacji.
    Ale trzeba mieć zainstalowane Safari w systemie.
    """
    driver.get(URL)
    title = driver.title
    print(title)
    assert 'mikulskibartosz/sages_data_sources' in title


def test_load_table_header_using_selenium(driver):
    """Wczytaj stronę której adres znajduje się w zmiennej URL przy użyciu biblioteki selenium.
    Wczytaj nagłówki tabeli znajdujacej się na stronie (tej samej której używaliśmy w testach beautifulsoup)
    """
    # driver.get(URL)
    # table = driver.find_elements(by=by.By.XPATH, value='//article/table')
    # html = table[0].get_attribute('innerHTML')
    # html = f'<table>{html}</table>'
    # header_titles = list(pd.read_html(html)[0])

    driver.get(URL)
    headers = driver.find_elements(by=by.By.XPATH, value='//article/table/thead/tr/th')
    header_titles = [header.text for header in headers]
    print(header_titles)
    assert header_titles == ['kolumna_A', 'kolumna_B', 'kolumna_C']


def test_load_table_as_dataframe_using_selenium(driver):
    """Wczytaj stronę której adres znajduje się w zmiennej URL przy użyciu biblioteki selenium.
    Wczytaj tabelę znajdujacą się na stronie jako Pandas DataFrame (tej samej której używaliśmy w testach beautifulsoup)
    """
    driver.get(URL)
    table = driver.find_elements(by=by.By.XPATH, value='//article/table')
    html = table[0].get_attribute('innerHTML')
    html = f'<table>{html}</table>'
    df = pd.read_html(html)[0]



    print(df)
    assert df.equals(pd.DataFrame({
        'kolumna_A': ['A1', 'B1', 'C1', 'D1'],
        'kolumna_B': ['A2', 'B2', 'C2', 'D2'],
        'kolumna_C': ['A3', 'B3', 'C3', 'D3'],
    }))


def test_follow_links_in_selenium(driver):
    """Wczytaj stronę której adres znajduje się w zmiennej URL przy użyciu biblioteki selenium.
    Przejdź do strony page1 i wczytaj jej tytuł"""
    driver.get(URL)
    #driver.find_element(by=by.By.LINK_TEXT, value='page1').click()
    driver.find_element(by=by.By.XPATH, value='//*[@id="repo-content-pjax-container"]/div/div/div[4]/div[3]/div/div[3]/div[2]/span/a').click()
    time.sleep(2)
    title = driver.title
    print(title)
    assert 'page1' in title
