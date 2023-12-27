# Bibliotecas importadas
import sys
import time # para facilitar a observação do funcionamento do sistema
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import pandas as pd

MODE = "normal" # Modo de funcionamento do programa
if len(sys.argv) > 1: 
    if('-v' in sys.argv):
        MODE = "visualization"

# Configuração do Web driver
PATH_WEBDRIVER = f'.\\chromedriver.exe'
service = Service(PATH_WEBDRIVER)
options = webdriver.ChromeOptions()
options.add_argument("--deny-permission-prompts") # Evitar requisições de permissão
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Remoção de erro irrelevante no terminal
if MODE == "normal": options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service, options=options)

driver.set_window_size(1080,800) # Com o objetivo de clicar exatamente em qualquer dispositivo nos inputs

# Acessando site da receita
driver.get(r"https://www.restituicao.receita.fazenda.gov.br/#/")

# Leitura JSON
PATH_JSON = f'.\\data\\people.json'
data = pd.read_json(PATH_JSON)

# Consultas
try:
    print("\nIniciando verificacoes\n")
    
    for index in data.index: # Para cada indivído no JSON
        
        driver.refresh() # Recarrega a página sempre que se faz a consulta para um novo indivíduo
        
        CPF = data["CPF"][index]
        DATA_NASCIMENTO = str(data["DATA_NASCIMENTO"][index])
        ANO = int(data["EXERCICIO"][index])
    
        # Espera do carregamento completo da página
        formElement = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "flt-glass-pane"))
        )

        # CPF
        actions = ActionBuilder(driver)
        actions.pointer_action.move_to_location(540, 150).click() # CPF input coordenadas
        actions.perform()
        ActionChains(driver).send_keys(CPF).perform() # digita CPF
        # Data de nascimento
        actions.pointer_action.move_to_location(540, 250).click()
        actions.perform()
        ActionChains(driver).send_keys(DATA_NASCIMENTO.replace('/', '')).perform() # digita data de nascimento (sem os /, que são preenchidos automaticamente)
        # Ano de exercício
        actions.pointer_action.move_to_location(540, 350).click() # abre a droplist dos anos
        actions.perform()
        if(ANO > 2012 and ANO <= 2023):
            actions.pointer_action.move_to_location(540, 75 + 50*abs(2023-ANO)).click()
            actions.perform()
        elif(ANO >= 2008):
            actions.pointer_action.move_to_location(930, 600).click() # scroll
            actions.perform()
            actions.pointer_action.move_to_location(540, 390 + 50*abs(2012-ANO)).click()
            actions.perform()

        actions.pointer_action.move_to_location(540, 530).click()
        actions.perform()
        
        if MODE == "visualization": time.sleep(2) # para facilitar a visualização
        print(f"{CPF} verificado.")
        
except Exception as e:
    print(e)
    print("\nHouve algum erro durante a execucao do programa, tente novamente, e se o erro persistir, envie um comunicado a equipe de suporte\n")
    input("Pressione ENTER para finalizar o programa...\n")

# Encerra webdriver
print("\n\nFinalizando programa, em caso de travamento ctrl+c\n")
driver.quit()