import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

nome_empresa_pesquisar = input(
    'Informe o nome da empresa a pesquisar as notas ficais: ')
browser = webdriver.Chrome(
    '/home/renan/projetos/estudo/scriptPython/chromedriver')

browser.get("https://nfstock.alterdata.com.br/")

input_usuario = browser.find_element_by_class_name("logincliente")
input_usuario.send_keys("17591262000170")

input_senha = browser.find_element_by_class_name("senhacliente")
input_senha.send_keys("Exata@175")

btn_login = browser.find_element_by_xpath("//input[@type='submit']")
btn_login.click()


link_nfe = browser.find_element_by_xpath(
    "//*[@id='menuLateral']/div[3]/div[1]/strong")
link_nfe.click()
# time.sleep(1)

link_nota_recebidas = browser.find_element_by_xpath(
    "//*[@id='collapseNfe']/div/ul/li[1]/a")

link_nota_recebidas.click()

# time.sleep(1)


qtd_pdf = browser.find_element_by_xpath(
    "//*[@id='paginacao-avancada']/ul/li/form/select/option[6]")
qtd_pdf.click()

form_data = browser.find_element_by_id("DataDe")
form_data.clear()

nome_fornecedor = browser.find_element_by_id("NomeEmitente")
nome_fornecedor.send_keys("{}".format(nome_empresa_pesquisar))

buscar_notas = browser.find_element_by_id("Buscar")
buscar_notas.click()

selecionar_todos = browser.find_element_by_id("selecionarTodos")
selecionar_todos.click()

baixar_todos = browser.find_element_by_id("botaoBaixarSelecionados")
baixar_todos.click()


alert = browser.switch_to_window

print(alert)
