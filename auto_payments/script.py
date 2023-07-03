import logsConf as logsConf
import movePath as movePath
import ficheiro as ficheiro
import operacoes as operacoes

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
