import time
import firebase_admin
from firebase_admin import credentials, firestore
from notify_run import Notify
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

# Inicializar Firebase Admin SDK
cred = credentials.Certificate('C:\\Users\\jpqca\\QuickChat\\Quick_Chat_Credentials.json')
app = firebase_admin.initialize_app(cred, name='quick----chat')
db = firestore.client(app=app)

# Inicializar Notify
notify = Notify(endpoint='https://notify.run/LAjAgK4f8VqMhT6BbNWf')

# Clave secreta para cifrado/descifrado
with open('C:\\Users\\jpqca\\QuickChat\\key_encryption.txt', 'rb') as key_file:
    key = key_file.read()

# Objeto Fernet para cifrar/descifrar
cipher_suite = Fernet(key)

# Función para enviar notificación
def send_notification(message):
    notify.send(message)

# Función para manejar los cambios en Firestore
def handle_firestore_changes(doc_snapshot):
    with open('mensajes_recibidos.txt', 'a') as file:
        for doc in doc_snapshot:
            data = doc.to_dict().get('text')
            if data:
                # Muestra una notificación
                send_notification("¡Nuevo Mensaje en QuickChat!")
                # Iterar sobre todos los mensajes en lugar de solo el último
                for encrypted_message in data:
                    # Descifrar el contenido
                    decrypted_message = decrypt(encrypted_message)
                    # Imprimir el contenido desencriptado en la terminal
                    print(decrypted_message)
                    # Guardar el nuevo mensaje desencriptado en el archivo de texto
                    file.write(decrypted_message + '\n')

# Función de desencriptación
def decrypt(encrypted_message):
    try:
        decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    except InvalidToken:
        print("Invalid token. The message could not be decrypted.")
        decrypted_message = None
    return decrypted_message

# Función para esperar cambios en Firestore y manejarlos
def listen_firestore_changes():
    doc_ref = db.collection('QuickChat').document('mensajes')

    # Espera por cambios en Firestore
    doc_watch = doc_ref.on_snapshot(lambda doc_snapshot, changes, read_time: handle_firestore_changes(doc_snapshot))

# Inicia el proceso de escucha de cambios en Firestore
listen_firestore_changes()

# Mantén el programa en ejecución
while True:
    time.sleep(1)  # Mantén el bucle principal ejecutándose
