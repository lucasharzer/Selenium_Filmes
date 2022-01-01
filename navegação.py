from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
from time import sleep


driver = webdriver.Chrome(executable_path="./chromedriver.exe")

# Abrir o site https://www.google.com.br/
driver.get("https://www.google.com.br/")

driver.implicitly_wait(1)
sleep(1)

driver.maximize_window()

# Filmes a serem pesquisados
filmes = ('homem aranha', 'matrix', 'turma da monica lições')

for filme in filmes:

    print(f"Para o filme \033[1;35m{filme}\033[m:")

    # Buscar o filme no campo de busca
    busca = driver.find_element_by_name('q')

    busca.send_keys(filme)
    busca.send_keys(Keys.ENTER)

    # Capturar as informações:

    # - Nome
    if filme == 'turma da monica lições':
        nome = driver.find_element_by_xpath(
            '/html/body/div[7]/div/div[11]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/h2/span').text
    else:
        nome = driver.find_element_by_xpath(
            '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div[2]/div/div[5]/div/div/div/span[2]').text

    # - Adicionais
    if filme == 'homem aranha':
        adicionais = driver.find_element_by_xpath(
            '/html/body/div[7]/div/div[10]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/span').text
    elif filme == "matrix":
        adicionais = driver.find_element_by_xpath(
            '/html/body/div[7]/div/div[11]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/span').text 
    else:
        adicionais = driver.find_element_by_xpath(
            '/html/body/div[7]/div/div[11]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/span').text      

    ad = adicionais.split(" ")

    if filme == "turma da monica lições":
        del(ad[2])

        classificação = ad[0]
        ano = 2021
        genero = ad[1]
        duração_hora = ad[2]
        duração_minutos = ad[3]
    else:

        del(ad[2])
        del(ad[3])

        classificação = ad[0]
        ano = ad[1]
        genero = ad[2]
        duração_hora = ad[3]
        duração_minutos = ad[4]

    # - Diretor
    diretor = driver.find_element_by_xpath(
        '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div[2]/div/div[4]/div/div/div/span[2]/a').text

    # - Avaliação
    if filme == "turma da monica lições":
        avaliação = 'indisponivel' 
    else:
        avaliação = driver.find_element_by_xpath(
            '//*[@id="kp-wp-tab-overview"]/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/div[1]').text

    # Exibir Resultados
    resultados = f'''
    Nome: \033[1;34m{nome}\033[m
    Classificação: \033[1;34m{classificação}\033[m
    Ano: \033[1;34m{ano}\033[m
    Gênero: \033[1;34m{genero}\033[m
    Duração: \033[1;34m{duração_hora}{duração_minutos}\033[m
    Diretor: \033[1;34m{diretor}\033[m
    Avaliação: \033[1;34m{avaliação}\033[m
    '''

    print(resultados)

    sleep(2)
    driver.back()

driver.minimize_window()

print("\033[1;32mProcesso concluído com sucesso.\033[m")

sleep(2)
driver.close()