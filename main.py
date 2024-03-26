from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time

options = webdriver.ChromeOptions()
# https://github.com/SeleniumHQ/selenium/issues/11637
prefs = {
    "download.default_directory": '/tmp/input/',
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
}
options.add_experimental_option(
    "prefs",
    prefs,
)
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--crash-dumps-dir=/tmp")
options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome(options=options)
driver.get('https://dados.gov.br/dados/conjuntos-dados/acessos---banda-larga-fixa')
time.sleep(15)
driver.maximize_window()
time.sleep(15)
driver.find_element(By.XPATH, '//*[@id="btnCollapse"]').click()
time.sleep(15)
driver.find_element(By.XPATH, '//*[@id="btnDownloadUrl"]').click()
time.sleep(180)