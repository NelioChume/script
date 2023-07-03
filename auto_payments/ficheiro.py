import json
import datetime
import os
from dotenv import load_dotenv
import logsConf as logsConf

load_dotenv()

nome_arquivo = os.getenv("FILE_PATH")
logsConf.logs().info(f'Ficheiro Oper: Arquivo de Leitura {nome_arquivo}')
def open_file():
    header = {}
    detalhes = []
    trailer = {}
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                if linha[0] == '0':
                    dataHeader = f"{linha[10:14]}-{linha[8:10]}-{linha[6:8]}"
                    header = {
                        "numero_header": linha.strip(),
                        "id_empresa": linha[1:4],
                        "id_perfil": linha[4:6],
                        "data": dataHeader,
                        "id_ficheiro": linha[14:19]
                    }
                elif linha[0] == '1':
                    dataDetalhe = f"{linha[48:52]}-{linha[46:48]}-{linha[44:46]}"
                    horaDetalhe = f"{linha[52:54]}:{linha[54:56]}:{linha[56:58]}"
                    detalhes.append({
                        "numero_detalhe": linha.strip(),
                        "referencia": linha[1:12],
                        "valor": linha[28:44],
                        "data": dataDetalhe,
                        "hora": horaDetalhe,
                        "id_transaccao": linha[58:65]
                    })
                else:
                    trailer = {
                        "numero_trailer": linha.strip(),
                        "total_registro": linha[1:8],
                        "total_pagamento": linha[8:24],
                        "total_comissoes": linha[24:40]
                    }

        json_fich = {
            "file": {
                "header": header,
                "details": detalhes,
                "trailer": trailer
            }
        }
        json_str = json.dumps(json_fich, indent=2)
        # Obter a data e hora atual
        now = datetime.datetime.now()
        dia = now.day
        mes = now.month
        ano = now.year
        hora = now.hour
        minuto = now.minute
        segundo = now.second

        nome_saida = f"{dia}-{mes}-{ano}-{hora}h{minuto}m{segundo}s.txt"
        with open(nome_saida, 'w') as arquivo_saida:
            arquivo_saida.write(json_str)
            logsConf.logs().info("Ficheiro de saida feito com sucesso")
        return json_str
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
        logsConf.logs().critical("Arquivo de leitura nao encontrado")
def read_header(chave):
    header = {}
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            if linha[0] == '0':
                dataHeader = f"{linha[10:14]}-{linha[8:10]}-{linha[6:8]}"
                header = {
                    "numero_header": linha.strip(),
                    "id_empresa": linha[1:4],
                    "id_perfil": linha[4:6],
                    "data": dataHeader,
                    "id_ficheiro": linha[14:19]
                }
    json_fich = {
        "file": {
            "header": header
        }
    }
    header = json.dumps(json_fich['file']['header'], indent=2)
    return json.loads(header)[f'{chave}']

def read_detalhe():
    detalhes = []

    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            if linha[0] == '1':
                dataDetalhe = f"{linha[48:52]}-{linha[46:48]}-{linha[44:46]}"
                # horaDetalhe = f"{linha[52:54]}:{linha[54:56]}:{linha[56:58]}"
                detalhes.append({
                    "numero_detalhe": linha.strip(),
                    "referencia": linha[1:12],
                    "valor": linha[28:44],
                    "data": dataDetalhe,
                    "hora": linha[52:54],
                    "minuto": linha[54:56],
                    "segundo": linha[56:58],
                    "id_transaccao": linha[58:65]
                })
    json_fich = {
        "file": {
            "details": detalhes
        }
    }
    detalhe = json.dumps(json_fich['file']['details'], indent=2)
    return json.loads(detalhe)

def read_trailer(chave):
    trailer = {}
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            if linha[0] == '9':
                trailer = {
                    "numero_trailer": linha.strip(),
                    "total_registro": linha[1:8],
                    "total_pagamento": linha[8:24],
                    "total_comissoes": linha[24:40]
                }

    json_fich = {
        "file": {
            "trailer": trailer
        }
    }
    header = json.dumps(json_fich['file']['trailer'], indent=2)
    return json.loads(header)[f'{chave}']
