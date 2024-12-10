# Sistema de Registro y Autenticación de Usuarios con MongoDB y Python

Este proyecto es un sistema básico de registro y autenticación de usuarios, desarrollado en Python. Utiliza **MongoDB Atlas** como base de datos para almacenar de manera segura los datos de los usuarios, incluyendo las contraseñas encriptadas mediante `bcrypt`.

## Características

- **Registro de usuarios**: Permite registrar nuevos usuarios almacenando sus credenciales de manera segura.
- **Autenticación de usuarios**: Verifica las credenciales ingresadas contra la base de datos.
- **Cifrado de contraseñas**: Usa `bcrypt` para garantizar la seguridad de las contraseñas.
- **Conexión con MongoDB Atlas**: Se conecta a una base de datos MongoDB en la nube para almacenar los datos.

## Requisitos Previos

Antes de ejecutar el código, asegúrate de tener lo siguiente:

1. **Python 3.7 o superior** instalado.
2. Las siguientes bibliotecas instaladas:
   - `pymongo`: Para interactuar con MongoDB.
   - `bcrypt`: Para el hash y verificación de contraseñas.
   - Puedes instalarlas ejecutando:
     ```bash
     pip install pymongo bcrypt
     ```
3. Una cuenta en [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) con un clúster configurado y accesible desde tu dirección IP.

## Configuración
1. Actualizar la conexión de MongoDB:
 ```Python
 client = MongoClient("mongodb+srv://<usuario>:<contraseña>@<cluster>.mongodb.net/?retryWrites=true&w=majority&appName=<nombre-app>")
```
- Usa tus credenciales y detalles del clúster.

## Uso del Sistema

### Opciones en el Menú
1. Registrar usuario:
    - Ingresa un nombre de usuario único.
    - Ingresa una contraseña que será cifrada antes de almacenarse.
2. Iniciar sesión:
    - Ingresa tu nombre de usuario y contraseña.\
    - El sistema verificará las credenciales y permitirá el acceso si son correctas.
3. Salir:
    - Cierra el programa.

### Estructura del Código
1. Conexión a MongoDB:
    - Se conecta a MongoDB Atlas usando la biblioteca `pymongo`.
2. Funciones principales: 
    - `register_user(username, password)`: Crea un nuevo usuario y almacena su contraseña en formato hash.
    - `authenticate_user(username, password)`: Verifica las credenciales del usuario ingresado.
3. Menú interactivo:
    - Proporciona opciones para registrar usuarios, iniciar sesión o salir.

### Seguridad
- **Contraseñas cifradas**: `bcrypt` se usa para generar hashes únicos por contraseña.
- **Verificación segura**: Los hashes se verifican sin exponer las contraseñas originales.
- **Base de datos remota**: Los datos se almacenan en MongoDB Atlas, que ofrece cifrado en tránsito y en reposo.

### Notas Importantes
- Asegúrate de agregar tu dirección IP en la configuración de Network Access de MongoDB Atlas para permitir el acceso.
- Considera usar variables de entorno para almacenar credenciales de conexión, en lugar de incluirlas directamente en el código.