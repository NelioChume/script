# Script de Propinas para o SIGEA!

Este Script permite verificação  de forma automática de propinas mensais e o armazenamento de pagamentos não confirmados de acordo com a lista de estudantes existente na base de dados. Essa verificacao eh feita mediante a a referencia que ehh fornecida em um ficheiro **.txt** pelo Banco BCI.  

# Instalação (No Ubuntu Server)

 - **Clonar o repositório:**
	` sudo git clone https://github.com/NelioChume/script.git`
	1.1. **Adicione previlegios directorio criado:** 
	`sudo chmod 777 /script`
	`cd script`
	`sudo mkdir output`
	`sudo chmod 777 /output`
	`sudo apt install python3-pip`
	
 - **Instalação das bibliotecas (python):**
	`pip install python-dotenv`
	`pip install DateTime`
	`pip install wheel`
	`pip install mysql.connector`
	`pip install mysql-connector-python`
	`pip install pylint --log LOG_FILE`
	**Add permissao para a criacao do LOG**
	`sudo chmod +w /home/test/script/auto_payments`
	
## Instalação do Mysql no Ubuntu Server e criação da BD
	sudo apt install mysql-server -y
	sudo systemctl start mysql.service
	sudo service mysql status
Output:
		` mysql.service - MySQL Community Server
Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
 Active: active (running) since Mon 2023-07-10 13:08:49 UTC; 19min ago
  Main PID: 23415 (mysqld)
Status: "Server is operational"`
 - **Criação e configuracao da Base de Dados e atribuicao de previlegios:**
 `sudo mysql -u root`
 `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';`
 `ALTER USER 'root'@'localhost' IDENTIFIED WITH auth_socket;`
 **Alterando os dados do Plugin:**
 mysql> `select user,host,plugin from mysql.user;`
 mysql> `update mysql.user set plugin='mysql_native_password' where host='localhost';`
 mysql> `flush privileges;`
 
 **Criando a Base de Dados**
 mysql> `create database sigea;`
 mysql> `use sigea;`
 
 **Criacao de Tabelas mysql>**
- `CREATE TABLE `extrapayments` (
  `id` int(11) NOT NULL,
  `code` int(11) NOT NULL,
  `amountpaid` varchar(20) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `obs` text NOT NULL,
  `student_id` int(11) NOT NULL,
  `services_id` int(11) NOT NULL,
  `quantidade` int(11) DEFAULT NULL,
  `entidade` varchar(50) NOT NULL,
  `referencia` varchar(50) NOT NULL,
  `situacao` varchar(200) NOT NULL DEFAULT 'Solicitado',
  `payment_method` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;`

- `CREATE TABLE `monthlypayment` (
  `id` int(11) NOT NULL,
  `month_code` int(11) NOT NULL,
  `value` double NOT NULL,
  `multa` double NOT NULL,
  `payd` tinyint(4) NOT NULL DEFAULT 0,
  `schoolaryear_id` int(11) NOT NULL,
  `month` varchar(50) NOT NULL,
  `payd_date` date DEFAULT NULL,
  `paymentLimitDate` date NOT NULL,
  `entidade` varchar(50) NOT NULL,
  `referencia` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;`

- `CREATE TABLE `notfoundpayments` (
  `id` int(11) NOT NULL,
  `entidade` varchar(50) DEFAULT NULL,
  `referencia` varchar(50) NOT NULL,
  `valor` double NOT NULL,
  `data_pagamento` timestamp NULL DEFAULT NULL,
  `nome_ficheiro` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;`

- `CREATE TABLE `payment` (
  `id` int(11) NOT NULL,
  `valuePayd` double(10,2) DEFAULT NULL,
  `datePayment` date DEFAULT NULL,
  `obs` text DEFAULT NULL,
  `method_payment` varchar(200) DEFAULT NULL,
  `monthlypayment_id` int(11) NOT NULL,
  `userName` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;`

- `CREATE TABLE `paymentschoolaryear` (
  `id` int(11) NOT NULL,
  `valuePayd` double(10,2) DEFAULT NULL,
  `obs` text CHARACTER SET latin1 DEFAULT NULL,
  `method_payment` varchar(200) DEFAULT NULL,
  `schoolarYear_id` int(11) NOT NULL,
  `userName` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;`

- `CREATE TABLE `schoolaryear` (
  `id` int(11) NOT NULL,
  `admission_id` int(11) DEFAULT NULL,
  `designation` int(11) NOT NULL,
  `level_id` int(11) NOT NULL,
  `student_id` int(11) DEFAULT NULL,
  `stream` varchar(20) NOT NULL,
  `divida` double(10,2) NOT NULL,
  `entidade` varchar(50) NOT NULL,
  `referencia` varchar(50) NOT NULL,
  `valordapropinadescontado` double(10,2) NOT NULL,
  `valordainscricao` double(10,2) DEFAULT NULL,
  `proveniencia` varchar(50) NOT NULL,
  `escola_anterior` varchar(50) NOT NULL,
  `estado` enum('Activo','Transferido','Viagem','Pagamento','Desistiu') DEFAULT NULL,
  `dataCancelamento` date DEFAULT NULL,
  `payd` tinyint(4) NOT NULL DEFAULT 0,
  `paydDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;`

- `CREATE TABLE `services2payment` (
  `id` int(11) NOT NULL,
  `valuePayd` double(10,2) DEFAULT NULL,
  `obs` text DEFAULT NULL,
  `method_payment` varchar(200) DEFAULT NULL,
  `extrapayments_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
`
- `ALTER TABLE `extrapayments` MODIFY COLUMN `id` INT AUTO_INCREMENT PRIMARY KEY;`
-  `ALTER TABLE `monthlypayment` MODIFY COLUMN `id` INT AUTO_INCREMENT PRIMARY KEY;`
-  `ALTER TABLE `notfoundpayments` MODIFY COLUMN `id` INT AUTO_INCREMENT PRIMARY KEY;`
-  `ALTER TABLE `payment` MODIFY COLUMN `id` INT AUTO_INCREMENT PRIMARY KEY;`
- `ALTER TABLE `paymentschoolaryear` MODIFY COLUMN `id` INT AUTO_INCREMENT PRIMARY KEY;`
- `ALTER TABLE `schoolaryear` MODIFY COLUMN `id` INT AUTO_INCREMENT PRIMARY KEY;`
- `ALTER TABLE `services2payment` MODIFY COLUMN `id` INT AUTO_INCREMENT PRIMARY KEY;`
- `ALTER TABLE `extrapayments`
 ADD KEY `fk_extrapayments_services` (`services_id`),
  ADD KEY `fk_extrapayments_student` (`student_id`);`
- `ALTER TABLE `monthlypayment`
 ADD KEY `fk_schoolaryear` (`schoolaryear_id`);`
 - `ALTER TABLE `services2payment`
 ADD KEY `fk_extraPayment` (`extrapayments_id`);`
 - `ALTER TABLE `payment`
  ADD CONSTRAINT `FK_monthlypayment` FOREIGN KEY (`monthlypayment_id`) REFERENCES `monthlypayment` (`id`);`
- `exit;`

**IMPORTANTE**
Não se esqueça de alterar os caminhos do ficheiro `.env` especificando o caminho da pasta `output`, o caminho da pasta `auto_payments` e o caminho do ficheiro `.txt`fornecido pelo banco BCI, `Exemplo_Ficheiro_BMEPS.TXT`. 

- Rodar do Script
Feito todas as configuracoes, execute o comando:
`sudo python3 script.py`
Resultado esperado:
`
	
Connect DB: Conexão estabelecida com a Base de Dados
leitura e criaccao do ficheiro
Referencia 01875081156 nao encontrada.
Referencia 01963381106 nao encontrada.
Referencia 02175151173 nao encontrada.
Referencia 02201241178 nao encontrada.
Referencia 02201351124 nao encontrada.
Referencia 02227331110 nao encontrada.
Referencia 02258191192 nao encontrada.
Referencia 02265591113 nao encontrada.
Referencia 02278981171 nao encontrada.
Referencia 02280931122 nao encontrada.
Referencia 02295721110 nao encontrada.
Referencia 02311881175 nao encontrada.
Referencia 02311891156 nao encontrada.
Referencia 02328321129 nao encontrada.
Fazendo as operacoes
Ficheiro removido com sucesso

Verifique a pasta `output` e confirme a existencia de ficheiros `.txt` com as especificações `dd-mm-aaa-hh:mm:ss.txt` 