import os
import shutil
from dotenv import load_dotenv

load_dotenv()
pasta_origem = os.getenv("PASTA_ORIGEM")
pasta_destino = os.getenv("PASTA_DESTINO")

arquivos = os.listdir(pasta_origem)  # Lista todos os arquivos da pasta de origem
# for arquivo in arquivos:
#     if arquivo
print(arquivos)