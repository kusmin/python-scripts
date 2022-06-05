import time
from re import T

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


# função para publicar
def publicar(numero_elementos, imagem, path):
    for i in range(numero_elementos):
        time.sleep(2)
        modal_escrever_publicacao = browser.find_element(By.XPATH, path)
        modal_escrever_publicacao.click()

        time.sleep(2)
        text_area = browser.find_element(By.CLASS_NAME, "textarea")
        text_area.clear()
        text_area.send_keys('Texto automarizado {}'.format(i))

        publicar = browser.find_element(By.XPATH, "//footer/button")
        publicar.click()
        
        

options = Options()

# options.add_argument("headless")
browser = webdriver.Chrome(
    options=options, executable_path='/home/renan/projetos/estudo/scriptPython/testandoMural/chromedriver')
browser.set_window_size(1200, 1000)
browser.get("http://happ2.weex.digital")



# Logar

time.sleep(5)

escolher_empresa = browser.find_element(By.CLASS_NAME,"select-input")
escolher_empresa = Select(escolher_empresa)
escolher_empresa.select_by_value("1")

escolher_campanha = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/form/div[2]/div/div/select")
escolher_campanha = Select(escolher_campanha)
escolher_campanha.select_by_visible_text("Mural 2022")

entrar = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/form/div[3]/button")
entrar.click()

time.sleep(2)

cadastro = browser.find_element(By.LINK_TEXT, "Já possuo cadastro")
cadastro.click()

time.sleep(2)

username = browser.find_element(By.NAME, "username")
username.clear()

username.send_keys("1234")

password = browser.find_element(By.NAME, "password")
password.clear()

password.send_keys("1234")

logar = browser.find_element(By.TAG_NAME, "button")
logar.click()

# Entrando no mural

time.sleep(2)
atividade = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div/button[3]/div[2]/div")
atividade.click()


time.sleep(2)
acessar = browser.find_element(By.XPATH, "//footer/button")
acessar.click()

# Curtir todas as publicações

time.sleep(2)
curtir = browser.find_elements(By.CLASS_NAME, "fa-heart")

print('{}'.format(len(curtir)))
for i in curtir:
    wait = WebDriverWait(browser, 10)
    browser.execute_script("arguments[0].scrollIntoView(true);", i)
    i.click()

# Escrever publicação

url_imagem = "/home/renan/Imagens/download.jpeg"
numero_elementos = 10

# publicar(numero_elementos, False, "/html/body/div[1]/div/div[3]/div/div/div[3]/button")

# Escrever Comentario

time.sleep(1)

commentarios = browser.find_element(By.CLASS_NAME, "btn-comentario")
commentarios.click()

# publicar(numero_elementos, False, '/html/body/div[1]/div/div[3]/div/div[1]/div/div[2]/footer/div/button')
