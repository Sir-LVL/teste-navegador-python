from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
#É necessário instalar a biblioteca selenium
navegador = webdriver.Firefox()
navegador.maximize_window()
navegador.get('https://store.steampowered.com')

time.sleep(3)

clic = navegador.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div[2]/div[3]/div[2]/div/div/a[2]')
clic.click()

abas = navegador.window_handles
navegador.switch_to.window(abas[-1])

ema = navegador.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div/div[1]/div[2]/form/div/div/div[2]/div/input')
ema.send_keys('teste@gmail.com')
confema = navegador.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div/div[1]/div[2]/form/div/div/div[3]/div/input')
confema.send_keys('teste@gmail.com')

pais = navegador.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div/div[1]/div[2]/form/div/div/div[4]/div[1]/div/select')
origem = Select(pais)
origem.select_by_visible_text('China')
