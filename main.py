import getpass
from encryption import encrypt_data, decrypt_data
from data_handler import erase_data

def main():
    password = "securepassword"  # This should be securely stored and hashed in a real application
    attempts = 3

    while attempts > 0:
        user_input = getpass.getpass("Enter password: ")
        if user_input == password:
            print("Access granted.")
            # Proceed with data access and encryption/decryption
            break
        else:
            attempts -= 1
            print(f"Incorrect password. You have {attempts} attempts left.")
            if attempts == 0:
                print("All attempts failed. Erasing data...")
                erase_data()  # Call the function to erase data
                break

if __name__ == "__main__":
    main()
