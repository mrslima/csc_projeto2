import socket
import sys
import time
import os
import conectividade 

from pprint import pprint


HOST = '127.0.0.1'          # IP do servidor

PORT = 9999               #Porta do servidor

diretorio = '/home/camilyalbres/somativa2/server/'

pydir = os.path.dirname(os.path.realpath(__file__))
print('Diretorio do script: ', pydir)
os.chdir(pydir)

# Coloque a função de Upload aqui
'''
def Upload(file, conn):

     Abrir o arquivo em modo leitura

     Ler uma linha do arquivo de cada vez

     Transmitir a linha para o servidor (converta a linha para bytes com encode())

     Após transmitir a última linha fechar o arquivo
	'''
#--------------------------------------------------------------------

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
except:
    print('# erro de conexao')
    sys.exit()

s.send(bytes('os.listdir(/home/camilyalbres/somativa2/server/)', 'utf-8'))

resposta = s.recv(2048).decode()


if diretorio not in resposta:
    print('Diretorio nao encontrado')
    #print(diretorio)
    
    s.send(bytes('os.makedirs({})\n'.format(diretorio),'utf-8'))
    print("Criando diretorio no server folder")
    time.sleep(2)
    print(s.recv(2048).decode())
 
else:
    print('Conteudo do diretorio:')
    try:
        print(f'{os.listdir(diretorio)}')
    except:
        print("Erro!")


arquivo = input('Digite o nome do arquivo para transferir: ')

isDir = os.path.exists(arquivo) 

if isDir == False:
	print('O arquivo especificado não existe')
	sys.exit()

conectividade.upload_file(diretorio,arquivo,s);



'''
 def upload_file(diretorio,arquivo,s):
	s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:

	    s2.bind(('', 9998))

	    s2.listen(1)

	except:

	    print('# erro de bind')

	    sys.exit()

	# Envia ordem de upload ao servidor
	s.send(bytes('upload({}{})\n'.format(diretorio,arquivo), 'utf-8'))

	# Aguarda a conexão para criar o canal de dados
	conn, addr = s2.accept()
	print('Servidor {} fez a conexao'.format(addr))
	# Chama a função que transfereo arquivo pelo canal de dados
	Upload(arquivo, conn) 

	conn.close()

	s2.close()

	print('O arquivo foi transferido')

	input('Digite <ENTER> para encerrar') 
	'''





