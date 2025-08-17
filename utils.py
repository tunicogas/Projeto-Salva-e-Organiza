from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, os, shutil
from selenium.webdriver.common.by import By

def pesquisa(driver, pesquisa, campodepesquisa_xpath):
    pesquisar = (f'{pesquisa}')
    barra = driver.find_element(By.XPATH, rf'{campodepesquisa_xpath}')
    barra.send_keys(pesquisar)
    barra.submit()

def imagempequena(driver, imagem_xpath):
    time.sleep(2)
    primeira_imagem = driver.find_element(By.XPATH, rf'{imagem_xpath}' )
    primeira_imagem.click()

def imagembaixar(driver, imagem_xpath):
    time.sleep(2)
    imagem_grande = driver.find_element(By.XPATH, rf'{imagem_xpath}')
    url_da_imagem = imagem_grande.get_attribute('src')
    return url_da_imagem

def configura_driver():
    """
    Funcao que confirua e inicia o driver
    """
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  #*  Tela cheia
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def cria_pasta_tipos(tipos, pasta_base):
    #*  Criar pastars de destino se não existirem
    for pasta in tipos:
        destino = os.path.join(pasta_base, pasta)
        os.makedirs(destino, exist_ok=True)

def organizador_de_arquivos(pasta_base, TIPOS):
    #*  Organizar os arquivos
    for arquivo in os.listdir(pasta_base): #* lista todos os arquivos na pasta_base
        caminho_arquivo = os.path.join(pasta_base, arquivo)

        #* verifica se e uma pasta
        if os.path.isdir(caminho_arquivo): 
            continue

        #* Saber qual e o arquivo(ex .jpg/.pdf/.py)
        nome, ext = os.path.splitext(arquivo)
        ext = ext.lower()

        #* Verificar em qual categoria
        movido = False
        for pasta, extensoes in TIPOS.items():
            if ext in extensoes:
                shutil.move(caminho_arquivo, os.path.join(pasta_base, pasta, arquivo))
                movido = True    
                break

        #* Nao tem categoria
        if not movido:
            shutil.move(caminho_arquivo, os.path.join(pasta_base, 'Outros', arquivo))