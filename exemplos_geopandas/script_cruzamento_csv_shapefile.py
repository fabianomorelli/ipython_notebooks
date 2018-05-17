
# coding: utf-8
# Declara a importacao das bibliotecas a serem utilizadas
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

# carrega o shapefile que está no mesmo diretorio do programa atual
# este arquivo eh o limite politico do brasil
brasil = gpd.read_file("./brasil_world_countries.shp")

# declara uma variavel com o caminho completo para o arquivo de interesse
firms_file_csv = "./fire_nrt_M6_10073.csv"

# faz a leitura do csv convertendo ele para um DataFrame
firms_modis_c6 = pd.read_csv(firms_file_csv)

# Prepara um novo atributo do tipo geometry utilizando a funcao Point do shapely para depois criar um geopandas
# esta variavel row eh soh pra ajudar a entender que ele vai pegar pra cada linha o atributo entre chaves
geometry = firms_modis_c6.apply(lambda row: Point(row['longitude'], row['latitude']), axis=1)

# cria uma variavel com referencia ao sistema de projecao cartografica
crs = {'init': 'epsg:4326'}

# cria um geodataframe com o dataframe anteriro
# neste caso usando o mesmo nome mais pode ser outro qualquer
firms_modis_c6 = gpd.GeoDataFrame(firms_modis_c6, crs=crs, geometry=geometry)

# executa o cruzamento espacial entre os pontos e os poligonos do shapefile
firms_modis_c6_brasil = gpd.sjoin(firms_modis_c6, brasil, how='inner', op='within')

# grava o novo dataFrame em um arquivo csv
firms_modis_c6_brasil.to_csv("./focos_filtrados_todos_atributos.csv")

# remove os atributos indesejados e grava em um csv
# note que o nome das colunas indesejadas esta indicado no comando drop
colunas_apagar = ['brightness', 'scan', 'track','instrument', 'confidence', 'version',
       'bright_t31', 'frp', 'daynight', 'geometry', 'index_right', 'id']

firms_modis_c6_brasil.drop(columns=colunas_apagar).to_csv("./focos_filtrados_poucos_atributos.csv")

# salva o dataframe completo para um arquivo shapefile
firms_modis_c6_brasil.to_file("./firms_modis_c6_brasil.shp")

print("final do processamento")
