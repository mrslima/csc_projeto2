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

def Upload(file, conn):
    try:
        f = open(file,'r')
    except:
        print('erro abertura arquivo')
	
    try: 
        count = 0
        while True:
            line = f.readline()
            data = conn.send(bytes(line,'utf-8'))
            if not data:
                break 	  
        f.close()
    except:
        f.close()
        conn.send(bytes('A PORTA DE DADOS NÃO ESTA ABERTA\n','utf-8'))

     #Abrir o arquivo em modo leitura
     #Ler uma linha do arquivo de cada vez
     #Transmitir a linha para o servidor (converta a linha para bytes com encode())
     #Após transmitir a última linha fechar o arquivo
     

#--------------------------------------------------------------------


#socket do processo client principal
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

def upload_handshake(diretorio,arquivo,s):
 
 	#socket do canal de transferencia do cliente
	s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
	    s2.bind(('', 9998))
	    s2.listen(1)

	except:
	    print('# erro de bind')
	    sys.exit()

	# Envia ordem de upload ao servidor // socket do processo principal do cliente
	s.send(bytes('upload({}{})\n'.format(diretorio,arquivo), 'utf-8'))

	# Aguarda a conexão para criar o canal de dados // conn -> socket do canal de transferencia da parte do server
	conn, addr = s2.accept()
	print('Servidor {} fez a conexao'.format(addr))
	
	# Chama a função que transfere o arquivo pelo canal de dados
	Upload(arquivo,conn) 

	conn.close()
	
	s2.close()

	print('O arquivo foi transferido')
	
	input('Digite <ENTER> para encerrar') 
	
	

upload_handshake(diretorio,arquivo,s);



