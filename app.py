#site exemplo do projeto: https://www.terabyteshop.com.br/pc-gamer

from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Chrome()
driver.get('https://www.terabyteshop.com.br/pc-gamer')

titulos = driver.find_elements(By.XPATH, "//a[@class='prod-name']")
precos = driver.find_elements(By.XPATH, "//div[@class='prod-new-price']")

workbook = openpyxl.Workbook()
workbook.create_sheet('produtos')
sheet_produtos = workbook['produtos']
sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preço'


for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text,preco.text])

workbook.save('produtos.xlsx')