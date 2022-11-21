import socket
import sys
import time
import os

def upload_file(diretorio,arquivo,s):
	s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:

	    s2.bind(('', 9998))

	    s2.listen(1)

	except:

	    print('# erro de bind')

	    sys.exit()

	# Envia ordem de upload aoservidor
	s.send(bytes('upload({}{})\n'.format(diretorio,arquivo), 'utf-8'))

	# Aguarda a conexão para criar o canal de dados
	conn, addr = s2.accept()
	print('Servidor {} fez a conexao'.format(addr))
	
	# Chama a função que transfereo arquivo pelo canal de dados

	#Upload(arquivo, conn) escreve no arquivo

	conn.close()

	s2.close()

	print('O arquivo foi transferido')

	input('Digite <ENTER> para encerrar')


