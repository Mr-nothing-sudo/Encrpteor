from cryptography.fernet import Fernet

def generate_key():
    """Generate a key for encryption and decryption."""
    return Fernet.generate_key()

def encrypt_data(data, key):
    """Encrypt the data using the provided key."""
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    """Decrypt the data using the provided key."""
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data
