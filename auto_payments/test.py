import ficheiro
import sqlQuerys

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
        sqlQuerys.insertPayment(datePayment, valuePayd, idMonthly)
        sqlQuerys.updateMonthlypayment(datePayment, referencia)
    elif (idExtra != None):
        print(f"Eh do ExtraPayment e o Id eh: {idExtra} e a Referencia eh: {referencia}")
        sqlQuerys.insertService2payment(valuePayd, idExtra)
        sqlQuerys.updateExtrapaymente(referencia)
    elif (idSchoolar != None):
        print(f"Eh do SchoolaryYear e o Id eh: {idSchoolar} e a Referencia eh: {referencia}")
        sqlQuerys.insertPaymentSchoolaryear(valuePayd, idSchoolar)
        sqlQuerys.updateSchoolaryear(datePayment, referencia)
    else:
        print(f"Referencia {referencia} nao encontrada.")
        sqlQuerys.insertNotFound(valuePayd, datePayment, referencia)

# referencia = 2295721110
#
# idExtra = sqlQuerys.selecttIdExtraPayment(referencia)
# idRef = sqlQuerys.selectIdSchoolaryear(referencia)
# idMonthly = sqlQuerys.selecttIdMonthlypayment(referencia)
# if (idRef != None):
#     print(f"Eh do SchoolaryYear e o Id eh: {idRef} e a Referencia eh: {referencia}")
# elif (idExtra != None):
#     print(f"Eh do ExtraPayment e o Id eh: {idExtra} e a Referencia eh: {referencia}")
# elif (idMonthly != None):
#     print(f"Eh do Monthlypayment e o Id eh: {idMonthly} e a Referencia eh: {referencia} ")
# else:
#     print(f"Referencia {referencia} nao encontrada.")

# conn = conexao.connect()
# cursor = conn.cursor()
#
# detalhes = ficheiro.read_detalhe()
# referencias_encontradas = []
# for detalhe in detalhes:
#     ref = int(detalhe['referencia'])
#     cursor.execute("SELECT `monthlypayment`.`id` FROM `monthlypayment` WHERE `monthlypayment`.`referencia` = %s;", (ref,))
#     result = cursor.fetchall()
#     for row in result:
#         referencia = int(row[0])
#         print(referencia)
#             # referencias_encontradas.append(referencia)
#
# # cursor.execute("SELECT `referencia` FROM `extrapayments` WHERE `extrapayments`.`referencia` = 21766080508;")
# # result = cursor.fetchall()
# # for x in result:
# #     ref = x[0].rstrip('\n')
# #     ref_int = int(ref)
# #     print("sd")