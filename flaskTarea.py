import bcrypt
from pymongo import MongoClient

# Conexión a MongoDB Atlas
# Se establece una conexión a la base de datos en la nube usando MongoClient.
client = MongoClient("mongodb+srv://crisjaimegn:B8lP83yUltr9KElm@cluster0.1gqta.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Selección de la base de datos y la colección.
db = client['secure_db']  # Nombre de la base de datos.
users_collection = db['users']  # Colección que almacenará los datos de los usuarios.

# Función para registrar usuarios
def register_user(username, password):
    """
    Registra un nuevo usuario en la base de datos.
    :param username: Nombre del usuario.
    :param password: Contraseña del usuario (sin hash).
    """
    # Verificar si el usuario ya existe en la base de datos.
    if users_collection.find_one({"username": username}):
        print(f"Error: El usuario '{username}' ya existe.")
        return False

    # Hashear la contraseña usando bcrypt.
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # Insertar el nuevo usuario con su contraseña cifrada en la colección.
    users_collection.insert_one({
        "username": username,
        "password_hash": hashed_password
    })

    print(f"Usuario '{username}' registrado con éxito.")
    return True

# Función para autenticar usuarios
def authenticate_user(username, password):
    """
    Autentica un usuario verificando sus credenciales.
    :param username: Nombre del usuario.
    :param password: Contraseña del usuario (sin hash).
    """
    # Buscar al usuario en la base de datos.
    user = users_collection.find_one({"username": username})

    # Verificar que el usuario exista y que la contraseña ingresada coincida con el hash almacenado.
    if user and bcrypt.checkpw(password.encode(), user['password_hash']):
        print(f"Inicio de sesión exitoso para el usuario '{username}'.")
        return True
    else:
        print(f"Error: Credenciales inválidas para el usuario '{username}'.")
        return False

# Menú principal
def main():
    """
    Función principal que implementa un menú interactivo para registro e inicio de sesión.
    """
    while True:
        # Mostrar las opciones del menú.
        print("\n=== Sistema de Registro y Login ===")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        # Solicitar al usuario que elija una opción.
        choice = input("Seleccione una opción: ")

        if choice == "1":
            # Registrar un nuevo usuario.
            username = input("Ingrese un nombre de usuario: ").strip()
            password = input("Ingrese una contraseña: ").strip()
            register_user(username, password)

        elif choice == "2":
            # Iniciar sesión con un usuario existente.
            username = input("Ingrese su nombre de usuario: ").strip()
            password = input("Ingrese su contraseña: ").strip()
            authenticate_user(username, password)

        elif choice == "3":
            # Salir del sistema.
            print("Saliendo del sistema. ¡Adiós!")
            break

        else:
            # Manejar opciones inválidas.
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutar el programa principal
if __name__ == "__main__":
    # Se ejecuta la función principal solo si el archivo se ejecuta directamente.
    main()
