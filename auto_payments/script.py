from auto_payments.operacoes_file import ficheiro
from auto_payments.operacoes_sql import operacoes
from auto_payments.move_file import movePath
from auto_payments.logs_Config import logsConf

if __name__ == "__main__":
    ficheiro.open_file()
    logsConf.logs().info('--------------------------------------------------')
    print("leitura e criaccao do ficheiro")
    operacoes.operacoes()
    logsConf.logs().info('___________________________________________________')
    print("Fazendo as operacoes")
    movePath.movepath()
    logsConf.logs().info('-- -- -- -- -- -- -- --- -- -- -- -- -- -- --- --- -- --')
    print("Ficheiro removido com sucesso")
