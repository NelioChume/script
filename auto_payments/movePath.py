import os
import shutil
from dotenv import load_dotenv
from auto_payments import logsConf

load_dotenv()
pasta_origem = os.getenv("PASTA_ORIGEM")
pasta_destino = os.getenv("PASTA_DESTINO")

def movepath():
    # Lista todos os arquivos da pasta de origem
    arquivos = os.listdir(pasta_origem)
    logsConf.logs().info("MovePath: Fazendo a leitura dos ficheiros")
    for arquivo in arquivos:
        if arquivo.endswith(".txt"):
            origem = os.path.join(pasta_origem, arquivo)
            destino = os.path.join(pasta_destino, arquivo)
            shutil.move(origem, destino)
            logsConf.logs().info(f'MovePath: Ficheiro {arquivo} movido de {origem} com sucesso para {destino}')