import os
import pyaes

## abrir o arquivo criptografado
file_name = input("Digite o nome do arquivo a ser criptografado: ")
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key_input = input("Digite a chave de criptografia: ")
key = key_input.encode('utf-8')[:16]
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = input("Digite o novo nome do arquivo: ")
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
