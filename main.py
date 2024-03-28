from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
import zipfile
from zipfile import ZipFile
import os

def download(path):
    if not os.path.exists(path):
        os.mkdir(path)
    options = webdriver.ChromeOptions()
    # https://github.com/SeleniumHQ/selenium/issues/11637
    prefs = {
        "download.default_directory": path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }
    options.add_experimental_option(
        "prefs",
        prefs,
    )
    options.add_argument("--headless=new")
    options.add_argument("--test-type")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-first-run")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--start-maximized")
    options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    )
    driver = webdriver.Chrome(options=options)
    driver.get('https://dados.gov.br/dados/conjuntos-dados/acessos---banda-larga-fixa')

    driver.maximize_window()
    print('primeiro passo...')
    WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '/html/body/div/section/div/div[3]/div[2]/div[3]/div[2]/header/button')
                )
            ).click()

    print('segundo passo...')
    WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '/html/body/div/section/div/div[3]/div[2]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div/button')
                )
            ).click()
    print('time...')
    time.sleep(150)
    print(os.listdir('/tmp/input/'))
def descompactar_arquivo():
    download(path = '/tmp/input/')
    # Obtenha o nome do arquivo ZIP baixado
    zip_file_path = os.path.join('/tmp/input/', 'acessos_banda_larga_fixa.zip')
    time.sleep(150)
    print(os.listdir('/tmp/input/'))
    try:
        with ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall('/tmp/input/')
                
    except Exception as e:
            print(f"Erro ao baixar ou extrair o arquivo ZIP: {str(e)}")


    os.remove(zip_file_path)
    return print(os.listdir('/tmp/input/'))

descompactar_arquivo()