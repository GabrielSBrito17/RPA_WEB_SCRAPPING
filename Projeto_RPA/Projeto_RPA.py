#Bibliotecas utilizadas no processo:
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
PATH = BASE_DIR + "\Projeto_RPA\chromedriver.exe"

# Obter conteúdo da URL e abertura do ChromeDriver:
url = "https://webscraper.io/"
option = Options()
option.headless = True
driver = webdriver.Chrome(PATH)
driver.get(url)
time.sleep(5)

#Processo de click's na página web de forma automatizada:
try:
    driver.find_element_by_xpath(
    "//html//body//header//div//div[2]//nav//ul//li[5]//a//p//font//font").click()
except:
     driver.find_element_by_xpath(
    "//html//body//header//div//div[1]//a//button").click()
time.sleep(2)
driver.find_element_by_xpath("//html//body//header//div//div[2]//nav//ul//li[5]//a//p").click()
time.sleep(2)
driver.find_element_by_xpath("//html//body//header//div//div[2]//nav//ul//li[5]//ul//li[4]//a").click()
time.sleep(2)
driver.find_element_by_xpath("//html//body//div[1]//div[3]//div[1]//div[1]//h2//a").click()
time.sleep(2)
driver.find_element_by_xpath("//html//body//div[1]//div[3]//div//div[1]//div//div//ul//li[2]//a").click()
time.sleep(2)
driver.find_element_by_xpath("//html//body//div[1]//div[3]//div//div[1]//div//div//ul//li[2]//ul//li[1]//a").click()
time.sleep(2)
element = driver.find_element_by_xpath("//html//body//div[1]//div[3]//div//div[2]//div")
html_content = element.get_attribute('outerHTML')

# parseando o conteúdo HTML:
soup = BeautifulSoup(html_content, 'html.parser')
item = soup.find_all(class_="col-sm-4 col-lg-4 col-md-4")

#Analisando o conteúdo extraída da página:
for i in item:
    print(i.text)

for i in item:
    filhas = i.findChildren("h4")
    print(filhas[0])
    pai = i.findChildren("a")
    print(pai[0])
    filho = i.findChildren("p")
    print(filho[0])
    print(filho[1])

preco, nome, descricao, reviews = [], [], [], []
for i in item:
    children = i.findChildren("h4")
    boy = i.findChildren("p")
    pai = i.findChildren("a")
    preco.append(children[0].text)
    nome.append(pai[0].text)
    descricao.append(boy[0].text)
    reviews.append(boy[1].text)

# Estruturando o conteúdo em um Data Frame utilizando o Pandas:
df = pd.DataFrame({'Nome': nome, 'Preco': preco, 'Descricao': descricao, 'Comentarios': reviews})
print(df)

#Fechamento da página:
driver.quit()

# Converter e salvar em um arquivo JSON:
js = df.to_json(orient= 'records')
fp = open('notebooks.json', 'w')
fp.write(js)
fp.close()
