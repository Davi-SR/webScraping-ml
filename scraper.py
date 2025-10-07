from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
from load import carregar_para_postgres


# Método de fazer requisição
def make_request(url, headers):
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        response = None
    else: 
        response = response.text
    return response   
    

# Método para pegar os preços da página
def get_page_data(dados_pagina):
    resultado_da_pagina = []
    card_produtos = dados_pagina.find_all('li', class_ = 'ui-search-layout__item')
    for card in card_produtos:
        titulo = card.find('h3', class_ = 'poly-component__title-wrapper')
        preco = card.find('span', class_ = 'andes-money-amount__fraction')
        products_info = {
            'titulo': titulo.text if titulo else 'N/A',
            'preco': preco.text if preco else 'N/A'
        }
        resultado_da_pagina.append(products_info)
    return resultado_da_pagina
    


# Iterar sobre todas as paginas para achar todos os precos

def iterar_paginas(url, headers):
    precos = []
    url_atual = url
    while(url_atual):
        html_pagina = make_request(url_atual, headers)
        if html_pagina:
            dados_pagina = BeautifulSoup(html_pagina, 'html.parser')
            todos_precos = get_page_data(dados_pagina)
            precos.extend(todos_precos)
            if url_atual:
                url_atual = get_next_page(dados_pagina)
            else: 
                url_atual = None
        else:
            url_atual = None
    return precos
 

# Metodo para pegar a proxima pagina
def get_next_page(dados_pagina):
    next_page = dados_pagina.find('a', title = 'Seguinte')
    if next_page:
        next_page = next_page.get('href')
    else:
        next_page = None
    return next_page


if __name__ == "__main__":
    url_de_partida = 'https://lista.mercadolivre.com.br/playstation-5'
    meus_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    dados_finais = iterar_paginas(url_de_partida, meus_headers)
    if dados_finais:
        print(f"\nScraping concluído! Total de {len(dados_finais)} produtos coletados.")
        df_produtos = pd.DataFrame(dados_finais)
        print("Amostra dos dados brutos:")
        print(df_produtos.head())
        
        # Salva em um CSV
        df_produtos.to_csv('mercadolivre_ps5.csv', index=False)
        print("\nDados salvos em 'mercadolivre_ps5.csv'")
        
    # 1. Limpeza da coluna preco
    df_produtos['preco_limpo'] = df_produtos['preco'].str.replace('.', '', regex=False)

    # 2. Conversão para número
    df_produtos['preco_numerico'] = pd.to_numeric(df_produtos['preco_limpo'], errors='coerce')

    # Salva o DataFrame LIMPO em um novo CSV
    df_produtos.to_csv('produtos_limpos_ml.csv', index=False)

    # Criar coluna com Data de carregamento dos produtos
    df_produtos['data_coleta'] = datetime.datetime.now()

    # Carregar dados para PostgreSQL
    carregar_para_postgres(df_produtos, 'anuncios_ps5')
