"""
Example encrypt and descrypt: Example of using the ByteDarkLock library
This example shows how to use the ByteDarkLock library to encrypt and decrypt data.
"""

# Import the ByteDarkLock class from the BDL module
from BDL import ByteDarkLock

# Create an instance of the ByteDarkLock class
bdl = ByteDarkLock.ByteDarkLock()

# Define the example message
Hello_world = "¡Hello world!"

# Generate an encryption key using the generate_key method
bdl.generate_key(
    key_id="Hello world",
    mode="fernet",
    ttl=15000,
    use_hmac=True
)

# Encrypt the message using the encrypt method
token = bdl.encrypt(
    data=Hello_world,
    key_id="Hello world"
)

# Decrypt the encrypted message using the decrypt method
plain = bdl.decrypt(
    token=token,
    key_id="Hello world"
)

# Print the decrypted message
print(plain)
