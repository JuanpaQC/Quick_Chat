import time
import firebase_admin
from firebase_admin import credentials, firestore
from cryptography.fernet import Fernet
from notify_run import Notify

# Inicializar la app de Firebase
cred = credentials.Certificate('C:\\Users\\jpqca\\QuickChat\\Quick_Chat_Credentials.json')
app = firebase_admin.initialize_app(cred, name='quick-chat')
db = firestore.client(app=app)

# Generar una clave para el cifrado
key = Fernet.generate_key()
cipher_suite = Fernet(key)

#meter la key de encriptacion en un archivo
with open('key_encryption.txt', 'wb') as key_file:
    key_file.write(key)

# Función para cifrar los datos
def encrypt_data(data):
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Función para subir datos cifrados a Firebase
def upload_data(data):
    doc_ref = db.collection('QuickChat').document('mensajes')
    doc_ref.update({'text': firestore.ArrayUnion([data])})

# Ruta al archivo de texto
file_path = 'C:\\Users\\jpqca\\Downloads\\TestMASM\\TestMASM\\mensajes_limpios.txt'

# Seguir la última posición leída del archivo
last_position = 0

# Monitorear continuamente el archivo en busca de cambios
while True:
    with open(file_path, 'r') as f:
        # Establecer el puntero del archivo a la última posición leída
        f.seek(last_position)

        # Leer el nuevo contenido del archivo a partir de la última posición
        new_data = f.readlines()

        if new_data:
            # Subir cada nueva línea a Firebase después de encriptarla
            for line in new_data:
                data = line.strip()
                if data:  # Verificar si hay datos para subir
                    encrypted_data = encrypt_data(data)
                    upload_data(encrypted_data)

            # Actualizar la última posición leída a la posición actual
            last_position = f.tell()

    # Dormir durante 3 segundos antes de volver a verificar
    time.sleep(1)
