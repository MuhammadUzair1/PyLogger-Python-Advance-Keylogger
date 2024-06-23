from cryptography.fernet import Fernet
import os

# Define paths
current_dir = os.path.dirname(os.path.realpath(__file__))
key_file_path = os.path.join(current_dir, "encryption_key.key")
log_file_path = os.path.join(current_dir, "Logfile.txt")
decrypted_log_file_path = os.path.join(current_dir, "DecryptedLogfile.txt")

# Read the encryption key
with open(key_file_path, 'rb') as key_file:
    key = key_file.read()

# Initialize the cipher suite
cipher_suite = Fernet(key)

# Read and decrypt the log file
def decrypt_log():
    try:
        with open(log_file_path, 'rb') as log_file:
            encrypted_data = log_file.readlines()

        with open(decrypted_log_file_path, 'w') as decrypted_log_file:
            for encrypted_line in encrypted_data:
                decrypted_line = cipher_suite.decrypt(encrypted_line.strip())
                decrypted_log_file.write(decrypted_line.decode('utf-8') + "\n")

        print(f"Decrypted log file saved at {decrypted_log_file_path}")

    except Exception as e:
        print(f"Error decrypting log file: {e}")

# Decrypt and save the logs
decrypt_log()
