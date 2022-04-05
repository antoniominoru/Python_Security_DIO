import hashlib

arq1 = 'a.txt'
arq2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(arq1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arq2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arq1} é diferente do arquivo: {arq2}')
    print('O hash do arquivo a.txt é: ' + hash1.hexdigest())
    print('O hash do arquivo b.txt é: ' + hash2.hexdigest())
else:
    print(f'O arquivo: {arq1} é igual do arquivo: {arq2}')
    print('O hash do arquivo a.txt é: ' + hash1.hexdigest())
    print('O hash do arquivo b.txt é: ' + hash2.hexdigest())