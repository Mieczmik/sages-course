import pandas as pd
from bs4 import BeautifulSoup
import requests
from lxml import etree

URL = 'https://github.com/mikulskibartosz/sages_data_sources/tree/rozwiazania/input_data/markdown'

def test_load_page_title():
    """Wczytaj stronę której adres znajduje się w zmiennej URL przy użyciu biblioteki requests.
    Użyj beautifulsoup do wczytania tytułu strony.
    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    print(title)
    assert 'mikulskibartosz/sages_data_sources' in title

def test_load_table_as_dataframe():
    """Wczytaj stronę ze zmiennej URL.
    Na stronie znajduje się tabelka. Wczytaj ją jako dataframe.
    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    tree = etree.HTML(str(soup))
    table = tree.xpath(".//article/table")
    table_html = etree.tostring(table[0])
    df = pd.read_html(table_html)[0]

    # response = requests.get(URL)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # article = soup.find('article')
    # table = article.find('table')
    # df = pd.read_html(table.prettify())[0]
    # print(df)

    assert df.equals(pd.DataFrame({
        'kolumna_A': ['A1', 'B1', 'C1', 'D1'],
        'kolumna_B': ['A2', 'B2', 'C2', 'D2'],
        'kolumna_C': ['A3', 'B3', 'C3', 'D3'],
    }))

def test_load_multiple_pages():
    """Wczytaj stronę ze zmiennej URL.
    Na stronie znajdują się dwa linki page1 oraz page2. Wczytaj obie strony do których prowadzą te linki.
    Każda z tych stron zawiera tabelkę. Wczytaj obie tabelki i złącz ich zawartość w jeden DataFrame.

    Podpowiedź:
    Użyj reset_index() aby numerowanie wierszy było spójne z oczekiwanym wynikiem.
    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    URLS = [
        'https://github.com' + link.get('href')
        for link in links
        if 'page1' in link.get('href') or 'page2' in link.get('href')
    ]

    dfs = []
    for link in URLS:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        tree = etree.HTML(str(soup))
        table = tree.xpath(".//article/table")
        table_html = etree.tostring(table[0])
        df = pd.read_html(table_html)[0]
        dfs.append(df)


    df = pd.concat(dfs, ignore_index=True)

    print(df)

    assert df.equals(pd.DataFrame({
        'kolumna_A': ['A1', 'B1', 'C1', 'D1'],
        'kolumna_B': ['A2', 'B2', 'C2', 'D2'],
        'kolumna_C': ['Test1', 'Test2', 'Test3', 'Test4'],
    }))
