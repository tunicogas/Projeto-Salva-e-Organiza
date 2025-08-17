import requests
import os
import shutil
from utils import pesquisa, imagembaixar, imagempequena, configura_driver, cria_pasta_tipos, organizador_de_arquivos
from settings import URLS, VARIAVEIS_GERAIS, XPATH, TIPOS

#* INICIO DO CODIGO
#* Nome da pasta onde a imagem será salva
pasta_destino = VARIAVEIS_GERAIS['pasta']
nome_arquivo = VARIAVEIS_GERAIS['nome_arquivo']

#*Criar a pasta se nao existir
os.makedirs(pasta_destino, exist_ok=True)

#* Caminho da pasta
caminho_completo = os.path.join(pasta_destino, nome_arquivo)

#* Configurar opções do navegador e inicia navegador
driver = configura_driver()
driver.get(URLS['url_google'])
pesquisa(driver, VARIAVEIS_GERAIS['pesquisa'], XPATH['input_pesquisa'])

#* click na imagem
imagempequena(driver, XPATH['input_imagem_pequena'] )
url_da_imagem = imagembaixar(driver, XPATH['input_imagem_baixar'])
print(f"\033[34mURL da imagem:\033[0m", url_da_imagem)

#* Baixar imagem e onde ira salvar a imagem => with open(caminho_completo, 'wb') as f:
response = requests.get(url_da_imagem)
with open(caminho_completo, 'wb') as f:
    f.write(response.content)
print(f"✅ Imagem salva como cachorro.jpg na pasta {caminho_completo}")

#*  Caminho da pasta onde os arquivos estão
pasta_base = os.path.join(os.getcwd(), VARIAVEIS_GERAIS['pasta'])
print(f'\033[33m{pasta_base}\033[33m')

#*  Criar pastars de destino se não existirem
cria_pasta_tipos(TIPOS, pasta_base)   

#*  Organizar os arquivos
organizador_de_arquivos(pasta_base, TIPOS)
driver.quit()