from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from enviar_email import enviar_email

chrome_options = Options()
chrome_options.add_argument('--headless')

service = Service(ChromeDriverManager().install())


def web_scraping(produto, nome_usuario, email_usuario):
    navegador = webdriver.Chrome(service=service,  options=chrome_options)

    navegador.get(f"https://www.amazon.com.br/s?k={produto}")

    itens = navegador.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

    dados_produtos = []

    for item in itens:
        try:
            nome_produto = item.find_element(By.XPATH, ".//h2/a/span").text.strip()

            preco_produto = item.find_element(By.XPATH, ".//span[@class='a-price-whole']").text.strip()

            dados_produtos.append({'Nome do Produto': nome_produto, 'Preço do Produto': preco_produto})

        except Exception as e:
            print("Erro ao extrair dados do produto:", e)

    df_produtos = pd.DataFrame(dados_produtos).sort_values(by='Nome do Produto')

    df_produtos['Preço do Produto'] = df_produtos['Preço do Produto'].apply(lambda x: f'R${x}')

    df_produtos.to_csv('Tabela de preços.csv', index=False, sep=';', encoding='utf-8-sig', header=True)
    
    enviar_email(nome_usuario, email_usuario)
   

    navegador.quit()
    