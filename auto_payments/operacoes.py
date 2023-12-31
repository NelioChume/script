import logsConf as logsConf
import ficheiro as ficheiro
import sqlQuerys as sqlQuerys


def operacoes():
    detalhes = ficheiro.read_detalhe()
    for detalhe in detalhes:
        referencia = detalhe['referencia']
        datePayment = detalhe['data']
        valuePayd = detalhe['valor']

    # referencia = 02311881175
        idExtra = sqlQuerys.selecttIdExtraPayment(referencia)
        idSchoolar = sqlQuerys.selectIdSchoolaryear(referencia)
        idMonthly = sqlQuerys.selecttIdMonthlypayment(referencia)
        if (idMonthly != None):
            print(f"Eh do Monthlypayment e o Id eh: {idMonthly} e a Referencia eh: {referencia} ")
            logsConf.logs().info(f'OperSQLs: Referencia-{referencia} encontrada na tabela MonthyPayment id-{idMonthly}')
            sqlQuerys.insertPayment(datePayment, valuePayd, idMonthly)
            sqlQuerys.updateMonthlypayment(datePayment, referencia)
            logsConf.logs().info('Insercao e Update feita')
        elif (idExtra != None):
            print(f"Eh do ExtraPayment e o Id eh: {idExtra} e a Referencia eh: {referencia}")
            logsConf.logs().info(f'OperSQLs: Referencia-{referencia} encontrada na tabela ExtraPayment id-{idExtra}')
            sqlQuerys.insertService2payment(valuePayd, idExtra)
            sqlQuerys.updateExtrapaymente(referencia)
            logsConf.logs().info('Insercao e Update feita')
        elif (idSchoolar != None):
            print(f"Eh do SchoolaryYear e o Id eh: {idSchoolar} e a Referencia eh: {referencia}")
            logsConf.logs().info(f'OperSQLs: Referencia-{referencia} encontrada na tabela SchoolaryYear id-{idSchoolar}')
            sqlQuerys.insertPaymentSchoolaryear(valuePayd, idSchoolar)
            sqlQuerys.updateSchoolaryear(datePayment, referencia)
            logsConf.logs().info('Insercao e Update feita')
        else:
            print(f"Referencia {referencia} nao encontrada.")
            logsConf.logs().info(f'OperSQLs: Referencia-{referencia} nao encontrada')
            sqlQuerys.insertNotFound(valuePayd, datePayment, referencia)
            logsConf.logs().info('Insercao feita na tabela NotFound')
