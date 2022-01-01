from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
from time import sleep


# Salvar um pôster do filme em questão
driver = webdriver.Chrome(executable_path="./chromedriver.exe")

driver.get("https://www.google.com.br")

driver.maximize_window()

busca = driver.find_element_by_name("q")
busca.send_keys("homem aranha")
busca.send_keys(Keys.ENTER)

sleep(40)

url = driver.find_element_by_xpath(
    '/html/body/div[7]/div/div[10]/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[1]/a/g-img/img').get_attribute("src")

local = r"C:\Users\Lucas\Documents\GitHub\filmes\poster\homem aranha.jpg"

urllib.request.urlretrieve(url, local)

driver.close()
