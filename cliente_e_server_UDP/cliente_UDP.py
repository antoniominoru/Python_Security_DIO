import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente socket criado com sucesso!!")

host = 'localhost'
porta = 5433
mensagem = 'Olá Servidor firmeza?\n'

try:
    s.sendto(mensagem.encode(), (host, 5432))
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('cliente: ' + dados)
finally:
    print('cliente fechando a conexão!!')
    s.close()