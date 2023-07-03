import conexao as conexao

conn = conexao.connect()
cursor = conn.cursor()
def selecttIdMonthlypayment(referencia):
    cursor.execute("SELECT `id` FROM `monthlypayment` WHERE `monthlypayment`.`referencia` = %s;", (referencia,))
    result = cursor.fetchall()
    for row in result:
        idRefencia = int(row[0])
        return idRefencia
def selecttIdExtraPayment(referencia):
    cursor.execute("SELECT `id` FROM `extrapayments` WHERE `extrapayments`.`referencia` = %s;", (referencia,))
    result = cursor.fetchall()
    for row in result:
        idRefencia = int(row[0])
        return idRefencia
def selectIdSchoolaryear(referencia):
    cursor.execute("SELECT `id` FROM `schoolaryear` WHERE `schoolaryear`.`referencia` = %s;", (referencia,))
    result = cursor.fetchall()
    for row in result:
        idRefencia = int(row[0])
        return idRefencia
def updateMonthlypayment(data, referencia):
    # Executando Update
    cursor.execute("UPDATE `monthlypayment` SET `payd`= 1, `payd_date`= %s WHERE `referencia` = %s;", (data, referencia))
    conn.commit()
def updateExtrapaymente(referencia):
    cursor.execute("UPDATE `extrapayments` SET `status`= 1 WHERE `referencia` = %s;", (referencia,))
    conn.commit()
def updateSchoolaryear(data, referencia):
    cursor.execute("UPDATE `schoolaryear` SET `payd`= 1, `paydDate`= %s WHERE `referencia` = %s;", (data, referencia))
    conn.commit()
def insertPayment(datePayment, valuePayd, monthlyId):
    insert = "INSERT INTO `payment`(`id`, `valuePayd`, `datePayment`, `obs`, `method_payment`, `monthlypayment_id`, `userName`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    value = ('', valuePayd, datePayment, 's/obs', 'Deposito', monthlyId, 'system')
    cursor.execute(insert, value)
    conn.commit()
def insertService2payment(valuePayd, extrapaymentsId):
    insert = "INSERT INTO `services2payment`(`id`, `valuePayd`, `obs`, `method_payment`, `extrapayments_id`) VALUES (%s,%s,%s,%s,%s)"
    value = ('', valuePayd, 's/obs', 'Deposito', extrapaymentsId)
    cursor.execute(insert, value)
    conn.commit()
def insertPaymentSchoolaryear(valuePayd, schoolarYearId):
    insert = "INSERT INTO `paymentschoolaryear`(`id`, `valuePayd`, `obs`, `method_payment`, `schoolarYear_id`, `userName`) VALUES (%s,%s,%s,%s,%s,%s)"
    value = ('', valuePayd, 's/obs', 'Deposito', schoolarYearId, 'system')
    cursor.execute(insert, value)
    conn.commit()
def insertNotFound(valuePayd, datePayment, referencia):
    entidade = 80005
    insert = "INSERT INTO `notfoundpayments`(`id`, `entidade`, `referencia`, `valor`, `data_pagamento`, `nome_ficheiro`) VALUES (%s,%s,%s,%s,%s,%s)"
    value = ('', entidade, referencia, valuePayd, datePayment, 'detalhe')
    cursor.execute(insert, value)
    conn.commit()