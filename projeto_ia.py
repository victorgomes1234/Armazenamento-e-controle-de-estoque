# Importando a biblioteca sys para fazer o programa terminar assim que for acionado.
import sys

from tkinter import messagebox

# importando a biblioteca que faz a conexão do python com banco de dados MySQL.
import pymysql.cursors

# Estabelecendo a conexão com o banco de dados:
connection = pymysql.connect(host='localhost',
                              db='teste',
                              user='root',
                              password='_4Z00Z1EF9',
                              port=3307,
                              charset='utf8',
                              cursorclass=pymysql.cursors.DictCursor)


# Criando o cursor que é usado para executar comandos dentro do banco de dados atravez do python:
cursor = connection.cursor()

print('{:=^10}'.format("Bem vindo a entrada de mercadorias!"))

# Variavel que vai ser inserido o número da nota que vai ser dada a entrada no sistema.
nfe = input("Qual nota deve ser dada a entrada: ")

# Executando o cursor criado para selecionar a nota referida no variavel que puxa a NF.
cursor.execute(f"SELECT barcode, quantidade FROM nota_entrega WHERE nfe = {nfe}")

#Variavel que vai puxar todos os dados da tabela selecionada.
record = cursor.fetchall()

#Execução da conferencia de nota fiscal.
while len(record) == 0:
    print("Não encontrado")
    nfe = input("Qual nota deve ser dada a entrada: ")
    cursor.execute(f"SELECT barcode, quantidade FROM nota_entrega WHERE nfe = {nfe}")

else:
    print('Nota encontrada')

# Looping criado para verificação dos itens contidos na nota(quantidade e código de barras)
code = ''
while True:
    code = input('Qual o código do produto: ')
    if code == "Fim":
        break
    found = False
    for linha in record:
        if linha["barcode"] == code:
            found = True
            linha["quantidade"] -= 1
    if not found:
        print('Item não encontra, sistema encerrado, verifique a nota.')
        sys.exit()

for linha in record:
  if linha["quantidade"] != 0:
      print('Alguns itens não conferem com a nota, verifique.')
      sys.exit()

print('Nota correta. Liberado para entrega')
connection.commit()