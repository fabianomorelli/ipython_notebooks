# Repositório de Exemplos de aplicações de Python em Jupyter Notebook 

Este repositório está sendo densenvolvido para deixar registrado soluções que podem ser reaproveitadas para auxiliar
outras pessoas no aprendizado da linguagem Python.

Cada caso é independente e autocontido podendo ser utilizado individualmente.

## Descrição dos diretórios

### cruzamento_espacial_bdg_csv
Exemplo que apresenta o processo de ingestão dos dados no Banco de Dados Geográficos de focos do satélite GOES-16, a partir de um arquivo CSV.

### exemplo_geopandas
- exemplos_geopandas\Analise Pontos em Poligonos.ipynb

Este exemplo ilustra como apresentar dados resumidos de um geodataframe em um mapa com geopandas. Utiliza como dados de entrada, arquivos no formato CSV que estão sendo lidos diretamente de um endereço internet em um dataframe a partir da biblioteca pandas. Também foi utilizado um shapefile da divisão política dos estados basileiros em um geodataframe criado a partir do GeoPandas.

- exemplos_geopandas\exemplos_geopandas.ipynb

Exemplo de cruzamento espacial utilizando dois shapefiles, que mostra como filtrar os pontos que estão contidos em polígono.

- exemplos_geopandas\script_cruzamento_csv_shapefile.ipynb

Exemplo de cruzamento espacial utilizando um arquivo csv eu um shapefiles, para mostrar como filtrar os pontos que estão contidos em polígono.
Este mesmo script foi convertido em um script python exemplos_geopandas\script_cruzamento_csv_shapefile.py

### manipulacao_datas
- manipulacao_datas\aula1.ipynb

Notas das primeira versão da aula de *Manipulação de Datas utilizandos a biblioteca datetime* da disciplina de Programação do INPE.

### vision_general_geoinformatica
Notas de uma oficina sobre a utilização de python em pesquisas científicas.

- vision_general_geoinformatica\clase_01.ipynb

Introdução a variáveis, tipos de dados, operações matemáticas.

- vision_general_geoinformatica\clase_02.ipynb
Controle de fluxo

- vision_general_geoinformatica\clase_03.ipynb
Uso de datas

- vision_general_geoinformatica\clase_04.ipynb
Introdução ao Numpy

- vision_general_geoinformatica\clase_05.ipynb

Bibliotecas do sistema operacional, criação de diretórios, listagem de arquivos.

### processamento_raios
- processamento_raios\exemplo Seaborn.ipynb

Exemplo de estudo do uso do Seaborn na geracao de graficos

- processamento_raios\exemplo02_geopandas.ipynb

Outros métodos para fazer a leitura de um arquivo csv e converter para geopandas com vários detalhes de cruzamentos.