import mysql.connector
from dotenv import load_dotenv
import os
import logsConf as logsConf

load_dotenv()

# Lendo as variáveis de ambiente do arquivo .env
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

# Fazendo a conexão com a base de dados
def connect():
    try:
        conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE)
        #logsConf.logs().info('Connect DB: Conexão estabelecida com a Base de Dados')
        print('Connect DB: Conexão estabelecida com a Base de Dados')
        return conn
    except mysql.connector.Error as erro:
        #logsConf.logs().critical(f'Connect DB: Falha na conexão da Base de Dados: {erro}')
        print(f'Connect DB: Falha na conexão da Base de Dados: {erro}')
