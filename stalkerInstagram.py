from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(
    '/home/renan/projetos/estudo/scriptPython/chromedriver')
browser.get('https://www.instagram.com/')

browser.find_element_by_name("username").send_keys("kusmin0000@gmail.com")

browser.find_element_by_name("password").send_keys("karpov142857")

browser.find_element_by_name("password").send_keys(Keys.RETURN)

browser.find_element_by_class_name("cq2ai").click()
browser.get('https://www.instagram.com/pycodebr')

browser.get_screenshot_as_file('perfil.png')
