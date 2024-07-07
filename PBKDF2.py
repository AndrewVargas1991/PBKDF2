import hashlib

interacoes = 100000
comprimento_chave = 32
senha = input('Digite sua senha: ').encode('utf-8')
sal = input('Digite seu sal: ').encode('utf-8')

# Se quiser gerar o sal de maneira aleatória, descomente as linhas abaixo
#   e salve o sal para usar futuramente
# sal = os.urandom(16)

# Você pode substituir a string 'sha256' pelos hashes 'sha1', 'sha224', 'sha384', 'sha512'
hash_com_sal = hashlib.pbkdf2_hmac('sha256', senha, sal, interacoes, comprimento_chave)
print(f'PBKDF2 de SHA256: {hash_com_sal.hex()}')

input('\nAperte ENTER para sair...')
