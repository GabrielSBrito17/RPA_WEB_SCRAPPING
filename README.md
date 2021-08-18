# Projeto de RPA web scrapping e API

Projeto de Web Scrapping com Python utilizando o módulo Selenium para automações de rotinas e processos.

# Primeiros passos:

Extrair o arquivo ```Projeto_RPA``` dentro de uma pasta local em seu computador. Logo após, pode baixar o Python no link ```https://www.python.org/``` e instalar para reproduzir o projeto.

#  Módulos necessários:

Necessário ter instalado junto ao Python as seguintes bibliotecas:
```
Time, Pandas, Requests, BeautifulSoup, Selenium, Json, Os e Flask.
```
# Instalando os módulos:
Para instalar os módulos, basta acessar o terminal Python e executar o comando pip install "nome do módulo".

Abaixo temos os comandos prontos para serem utilizados:

```pip install time
pip install pandas
pip install requests
pip install BeautifulSoup
pip install selenium
pip install json
pip install os
pip install flask
```
# Executando o "Robô":

Após instalação dos módulos, abrir o arquivo ```Projeto_RPA.py``` e executar dentro de uma IDE Python. ( Utilizei o Visual Studio CODE )

# Explicação de funcionamento do "Robô":

O "Robô" abre a página web ```https://webscraper.io/``` e sai em busca do comando onde fica os dados referente aos "Notebooks". Coleta as informações na página e armazena dentro de um arquivo ``` JSON ```que será criado após a execução do "Robô" na pasta de destino onde está o arquivo ```Projeto_RPA.py```

# Executando o ``` JSON ``` em uma API RESTful:

Após o nosso "Robô" criar o arquivo ``` notebooks.json ```, iremos executar o arquivo ```API.py``` dentro da nosa IDE.

# Dados da API:

A nossa API irá criar um servidor local ``` http://127.0.0.1:5000 ``` a principio vai aparecer uma tela de "Erro", mas basta executa-lo da seguinte forma ``` http://127.0.0.1:5000/notebooks ``` que irá aparecer os dados do nosso ``` JSON ```:

```
{
    "Comentarios": "14 reviews", 
    "Descricao": "Asus VivoBook X441NA-GA190 Chocolate Black, 14\", Celeron N3450, 4GB, 128GB SSD, Endless OS, ENG kbd", 
    "Nome": "Asus VivoBook X4...", 
    "Preco": "$295.99"
  }, 
  {
    "Comentarios": "8 reviews", 
    "Descricao": "Prestigio SmartBook 133S Dark Grey, 13.3\" FHD IPS, Celeron N3350 1.1GHz, 4GB, 32GB, Windows 10 Pro + Office 365 1 gadam", 
    "Nome": "Prestigio SmartB...", 
    "Preco": "$299.00"
  }, 
  {
    "Comentarios": "12 reviews", 
    "Descricao": "Prestigio SmartBook 133S Gold, 13.3\" FHD IPS, Celeron N3350 1.1GHz, 4GB, 32GB, Windows 10 Pro + Office 365 1 gadam", 
    "Nome": "Prestigio SmartB...", 
    "Preco": "$299.00"
  }, 
  {
    "Comentarios": "2 reviews", 
    "Descricao": "15.6\", Pentium N3520 2.16GHz, 4GB, 500GB, Linux", 
    "Nome": "Aspire E1-510", 
    "Preco": "$306.99"
  }, 
  {
    "Comentarios": "5 reviews", 
    "Descricao": "Lenovo V110-15IAP, 15.6\" HD, Celeron N3350 1.1GHz, 4GB, 128GB SSD, Windows 10 Home", 
    "Nome": "Lenovo V110-15IA...", 
    "Preco": "$321.94"
  }, 
  {
    "Comentarios": "6 reviews", 
    "Descricao": "Asus VivoBook 15 X540NA-GQ008T Chocolate Black, 15.6\" HD, Pentium N4200, 4GB, 500GB, Windows 10 Home, En kbd", 
    "Nome": "Lenovo V110-15IA...", 
    "Preco": "$356.49"
  }, 

```

# Filtrando dados na API:

Com a API rodando podemos utilizar filtro para selecionar os notebooks pela marca. Por exemplo ``` http://127.0.0.1:5000/notebooks/Lenovo ```e ele trás os dados referente aos notebooks da marca Lenovo:

```

{
    "Comentarios": "5 reviews", 
    "Descricao": "Lenovo V110-15IAP, 15.6\" HD, Celeron N3350 1.1GHz, 4GB, 128GB SSD, Windows 10 Home", 
    "Nome": "Lenovo V110-15IA...", 
    "Preco": "$321.94"
  }, 
  {
    "Comentarios": "12 reviews", 
    "Descricao": "Lenovo ThinkPad E31-80, 13.3\" HD, Celeron 3855U 1.6GHz, 4GB, 128GB SSD, Windows 10 Home", 
    "Nome": "Lenovo ThinkPad...", 
    "Preco": "$404.23"
  }, 
  {
    "Comentarios": "9 reviews", 
    "Descricao": "Lenovo V110-15ISK, 15.6\" HD, Core i3-6006U, 8GB, 128GB SSD, Windows 10 Home", 
    "Nome": "Lenovo V110-15IS...", 
    "Preco": "$409.63"
  }, 

```
