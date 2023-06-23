from auto_payments.conexao_bd import conexao
from datetime import datetime
from auto_payments.operacoes_file import ficheiro
from auto_payments.move_file import movePath

def insert_header():
    sql = "INSERT INTO header_bmeps (header_id, header_number, company_id, profile_id, header_date, file_id) VALUES (%s, %s, %s, %s, %s, %s)"

    header_number = ficheiro.read_header('numero_header')
    company_id = ficheiro.read_header('id_empresa')
    profile_id = ficheiro.read_header('id_perfil')
    header_date = ficheiro.read_header('data')
    file_id = ficheiro.read_header('id_ficheiro')

    val = ('', header_number, company_id, profile_id, header_date, file_id)
    conn = conexao.connect()
    cursor = conn.cursor()
    cursor.execute(sql, val)
    conn.commit()
    print("Header inserido com sucesso")

def insert_detalhe():
    detalhes = ficheiro.read_detalhe()
    for detalhe in detalhes:
        sql = "INSERT INTO detalhe_bmeps (detalhe_id, reference_number, payment_value, data, transacao_id) VALUES (%s, %s, %s, %s, %s)"
        ano = detalhe['ano']
        mes = detalhe['mes']
        dia = detalhe['dia']
        hora = detalhe['hora']
        minuto = detalhe['minuto']
        segundo = detalhe['segundo']
        # Criando um objeto datetime com a data e hora desejadas YYYY-MM-DD HH:MM:SS
        data = datetime(int(ano), int(mes), int(dia), int(hora), int(minuto), int(segundo))
        reference_number = detalhe['referencia']
        payment_value = detalhe['valor']
        transacao_id = detalhe['id_transaccao']

        # Executa o comando SQL com os valores correspondentes
        valores = ('', reference_number, payment_value, data, transacao_id)
        conn = conexao.connect()
        cursor = conn.cursor()
        cursor.execute(sql, valores)
        conn.commit()
    print("Detalhes inserido com sucesso!")

def insert_trailer():
    sql = "INSERT INTO trailer_bmeps (trailer_id, trailer_number, number_registro, total_payment, total_comissao) VALUES (%s, %s, %s, %s, %s)"
    trailer_number = ficheiro.read_trailer('numero_trailer')
    number_registro = ficheiro.read_trailer('total_registro')
    total_payment = ficheiro.read_trailer('total_pagamento')
    total_comissao = ficheiro.read_trailer('total_comissoes')

    val = ('', trailer_number, number_registro, total_payment, total_comissao)
    conn = conexao.connect()
    cursor = conn.cursor()
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    conn.close()
    print("Trailer inserido com sucesso")

if __name__ == "__main__":
    # insert_header()
    # print("---------------")
    # insert_detalhe()
    # print("--------------")
    # insert_trailer()
    ficheiro.open_file()

    movePath.movepath()
