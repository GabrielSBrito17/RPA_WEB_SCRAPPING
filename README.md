# Projeto de RPA web scrapping e API

Projeto de Web Scrapping com Python utilizando o módulo Selenium para automações de rotinas e processos.

# Primeiros passos:

Extrair o arquivo ```Projeto_RPA``` dentro de uma pasta local em seu computador. Logo após, pode baixar o Python no link ```https://www.python.org/``` e instalar para reproduzir o projeto.

#  Módulos necessários:

Necessário ter instalado junto ao Python as seguintes bibliotecas:
```
Time, Pandas, Requests, BeautifulSoup, Selenium, Json, Os e Flaks
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

A nossa API irá criar um servidor local ``` http://127.0.0.1:5000 ``` a principio vai aparecer uma tela de "Erro", mas basta executa-lo da seguinte forma ``` http://127.0.0.1:5000/notebooks ``` que irá aparecer os dados do nosso ``` JSON ```.

# Filtrando dados na API:

Com a API rodando podemos utilizar filtro para selecionar os notebooks pela marca. Por exemplo ``` http://127.0.0.1:5000/notebooks/Lenovo ```e ele trás os dados referente aos notebooks da marca Lenovo.
