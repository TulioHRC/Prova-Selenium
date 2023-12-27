# Bibliotecas importadas
import os
import time # para facilitar a observação do funcionamento do sistema
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import pandas as pd

# Configuração do Web driver
PATH_WEBDRIVER = f'{os.getcwd()}\\chromedriver.exe'
service = webdriver.ChromeService(PATH_WEBDRIVER) # Para definição do local exato do webdriver
driver = webdriver.Chrome(service=service)
driver.set_window_size(1080,800) # Com o objetivo de clicar exatamente em qualquer dispositivo nos inputs

# Passo 1 - Acessando site da receita
driver.get(r"https://www.restituicao.receita.fazenda.gov.br/#/")

# Passo 2 - Leitura JSON
PATH_JSON = f'{os.getcwd()}\\data\\people.json'
data = pd.read_json(PATH_JSON)

# Passo 3 - Consulta
try: # Espera do carregamento completo da página
    formElement = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "flt-glass-pane"))
    )

    actions = ActionBuilder(driver)
    actions.pointer_action.move_to_location(540, 150).click() # CPF input coordenadas
    actions.perform()
    ActionChains(driver).send_keys("14311111152").perform()
    input()
    
except Exception as e:
    print("\nErro ao tentar encontrar os elementos HTML em 30 segundos de espera:\n")
    print(e)

# Encerra webdriver
driver.quit()