# 📊 Pipeline de Dados e Web Scraping do Mercado Livre

Este projeto é um pipeline de dados ETL completo que extrai, em tempo real, dados de anúncios do Mercado Livre através de Web Scraping, processa e limpa essas informações, e as carrega em um banco de dados PostgreSQL para futuras análises.

## 📜 Descrição

O objetivo deste projeto foi construir uma solução de engenharia de dados do zero, simulando um cenário real onde os dados não estão disponíveis via API. O pipeline é capaz de:

1.  Navegar pelas páginas de resultados de uma busca específica no Mercado Livre.
2.  Extrair informações relevantes de cada anúncio (título e preço).
3.  Estruturar, limpar e transformar os dados brutos em um formato analítico e numérico usando a biblioteca Pandas.
4.  Carregar os dados tratados em um banco de dados relacional (PostgreSQL), prontos para serem consumidos por ferramentas de BI ou outras aplicações.

## ✨ Funcionalidades

- **Web Scraping Multi-Página:** O robô navega automaticamente pela paginação do site, coletando dados de todas as páginas de resultados.
- **Extração Robusta de Dados:** Utiliza `BeautifulSoup` para parsear o HTML e extrair os dados de interesse, mesmo com a complexidade da estrutura do site.
- **Limpeza e Transformação:** Processamento dos dados com `Pandas` para converter preços em formato de texto (ex: "R$ 4.899") para um formato numérico e limpo.
- **Persistência de Dados:** Carrega os dados limpos em um banco de dados PostgreSQL, incluindo uma coluna `data_coleta` para rastreabilidade temporal.
- **Práticas de Segurança:** Gerenciamento de credenciais do banco de dados de forma segura, utilizando variáveis de ambiente com um arquivo `.env`.

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias e bibliotecas:

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Requests-232F3E?style=for-the-badge&logo=requests&logoColor=white" />
  <img src="https://img.shields.io/badge/Beautiful_Soup-000000?style=for-the-badge&logo=-&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-B22222?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
</p>

## 🚀 Como Executar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

**1. Pré-requisitos:**
* Ter o Python 3.x instalado.
* Ter um servidor PostgreSQL instalado e rodando.

**2. Clone o Repositório:**
```bash
git clone [URL-DO-SEU-REPOSITÓRIO-AQUI]
cd [NOME-DA-PASTA-DO-PROJETO]
````

**3. Crie e Ative o Ambiente Virtual:**

````Bash

# Crie o ambiente
python -m venv venv

# Ative o ambiente (Linux/Mac)
source venv/bin/activate

# Ative o ambiente (Windows)
.\venv\Scripts\activate

````
**4. Instale as Dependências:**
````Bash
pip install pandas requests beautifulsoup4 sqlalchemy psycopg2-binary python-dotenv
````
**5. Configure as Variáveis de Ambiente:**

Crie um arquivo chamado .env na raiz do projeto.

Adicione a sua string de conexão do PostgreSQL a ele:
````Bash
DATABASE_URL="postgresql://seu_usuario:sua_senha@localhost:5432/seu_banco"
````

**6. Prepare o Banco de Dados:**

Conecte-se ao seu PostgreSQL.

Crie o banco de dados (se não existir).

Crie a tabela para receber os dados. Exemplo:
````Bash
CREATE TABLE anuncios_ps5 (
    id SERIAL PRIMARY KEY,
    titulo TEXT,
    preco INTEGER,
    data_coleta TIMESTAMP
);
````
**7. Execute o Scraper:**
````Bash
python scraper.py
````
Ao final da execução, os dados estarão na sua tabela do PostgreSQL e um arquivo CSV de backup será gerado.

## 📁 Estrutura do Projeto
.
├── scraper.py         # Script principal que orquestra todo o processo de ETL
├── load.py            # Módulo com a função de carga para o PostgreSQL
├── .env               # Arquivo local com as credenciais (ignorado pelo Git)
├── .gitignore         # Arquivo que especifica o que o Git deve ignorar
├── requirements.txt   # Lista de dependências Python do projeto
└── README.md          # Esta documentação


Desenvolvido com entusiasmo por Davi Silva Ramos.
