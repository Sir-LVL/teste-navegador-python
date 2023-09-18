from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

cachorro_quente = webdriver.Firefox()
cachorro_quente.maximize_window()
cachorro_quente.get('https://store.steampowered.com')

time.sleep(3)

clic = cachorro_quente.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div[2]/div[3]/div[2]/div/div/a[2]')
clic.click()

abas = cachorro_quente.window_handles
cachorro_quente.switch_to.window(abas[-1])

ema = cachorro_quente.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div/div[1]/div[2]/form/div/div/div[2]/div/input')
ema.send_keys('tuegay@gmail.com')
confema = cachorro_quente.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div/div[1]/div[2]/form/div/div/div[3]/div/input')
confema.send_keys('tuegay@gmail.com')

pais = cachorro_quente.find_element(By.XPATH, '/html/body/div[1]/div[7]/div[6]/div/div[1]/div[2]/form/div/div/div[4]/div[1]/div/select')
origem = Select(pais)
origem.select_by_visible_text('China')