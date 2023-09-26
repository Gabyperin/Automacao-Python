### PYTHON POWER UP ###
# Passo a passo do projeto 
#Passo 1: Entra no sistema da empresa 
# (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
# Passo 2: FAZER LOGIN
# Passo 3: Importar a base de dados de produtos
# Passo 4: Cadastrar 1 produto
# passo 5: Repetir o cadastro para todos os produtos

import pyautogui 
import time

#pyautogui.click -> clicar com o mouse
#pyautogui.write -> escrever um texto
#pyautogui.press -> apertar 1 tecla
#pyautogui.hotkey -> atalho(combinação de teclas)


pyautogui.PAUSE = 1.5
  
#abrir o chrome 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entra no link 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#esperar o site carregar
time.sleep(3)
# Passo 2: fAZER LOGIN
pyautogui.click(x=401, y=328)
pyautogui.write("gabiap02@gmail.com")

pyautogui.press("tab") # -> passar para o campo de senha
pyautogui.write("gabiehabraba") 

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)


# Passo 3: Importar a base de dados de produtos
# pip install pandas numpy openpyxl
import pandas 
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=399, y=228)   
    codigo = tabela.loc[linha, "codigo"]
    #prencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"])) 
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    

    # Apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

# passo 5: Repetir o cadastro para todos os produtos
