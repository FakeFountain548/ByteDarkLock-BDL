"""
Ejemplo cifrado y decifrado: Ejemplo de uso de la librería ByteDarkLock
Este ejemplo muestra cómo usar la librería ByteDarkLock para cifrar y descifrar datos.
"""
# Importar la clase ByteDarkLock desde el módulo BDL
from BDL import ByteDarkLock

# Crear una instancia de la clase ByteDarkLock
bdl = ByteDarkLock.ByteDarkLock()

#Define el ejemplo de mensaje
Hola_mundo = "¡Hola_mundo!"

# Generar una clave de cifrado utilizando el método generate_key
bdl.generate_key(
    key_id="Hola mundo",
    mode="fernet",
    ttl=15000,
    use_hmac=True
)

# Cifrar el mensaje utilizando el método encrypt
token = bdl.encrypt(
    data=Hola_mundo,
    key_id="Hola mundo"
)

#descifra el mensaje cifrado utilizando el método decrypt
plain = bdl.decrypt(
    token=token,
    key_id="Hola mundo"
)

#imprime el mensaje descifrado
print(plain)
