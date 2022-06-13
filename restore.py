from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import selenium.common.exceptions as selex
from selenium.webdriver.common.by import By
import datetime
import os

headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={headers}')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://re-store.ru/apple-iphone/'
driver.get(url=url)

items = driver.find_elements(By.CLASS_NAME, "product-card.catalog__item.product-card--buy")

data = []

for item in items:
    item_data = {}

    item_href = item.find_element(By.CLASS_NAME, "product-card__link")
    item_a = item_href.get_attribute('href')
    item_pn = item_a.split('/')[-2]
    item_hint = item.find_element(By.CLASS_NAME, 'product-card__hint').text
    item_price = item.find_element(By.CLASS_NAME, "product-card__price").text
    item_name = item.find_element(By.CLASS_NAME, "product-card__name").text

    item_data[item_pn] = [item_a, item_name, item_price, item_hint]

    data.append(item_data)

with open(f'data.txt', 'a', encoding='utf-8') as file:
    for item in data:
        file.write(f'{item}\n')
    file.close()