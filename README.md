# PyLogger

PyLogger is a simple and powerful Python keylogger capable of logging keystrokes, mouse clicks, taking screenshots, and more. The tool will send the logs to your email at specified intervals (default is every minute) and also save encrypted keystrokes on the victim's computer.

## Installation

- Run it: `python PyLogger.py`

## Steps to Run

1. Place both the keylogger and decryption scripts in the same directory.
2. Run the keylogger script to start capturing keystrokes.
3. Run the decryption script to decrypt and view the captured keystrokes.

## Detailed Explanation

### Keylogger Script (`PyLogger.py`)

1. **Configuration:**

   - Set your Gmail credentials and recipient email address.
   - Define the interval for sending emails (default is 60 seconds).

2. **Paths:**

   - All files (encryption key, log file) are stored in the same directory as the keylogger script.

3. **Encryption Key Generation:**

   - Generates an encryption key using the `cryptography` library and saves it to a file named `encryption_key.key`.

4. **Log File Creation:**

   - Ensures the log file (`Logfile.txt`) exists in the directory.

5. **Adding to Startup:**

   - Adds the keylogger script to the startup registry key to ensure it runs on system startup.

6. **Hiding the Console Window:**

   - Uses `win32console` and `win32gui` to hide the console window.

7. **Keystroke and Mouse Event Capturing:**

   - Uses the `pynput` library to capture keyboard and mouse events.
   - Encrypts captured data and appends it to the log file.

8. **Email Sending:**

   - Sends the encrypted log file to the specified email address at defined intervals using the `smtplib` library.

9. **Event Listeners:**
   - Initializes and starts listeners for keyboard and mouse events.

### Decryption Script (`decrypt_log.py`)

1. **Paths:**

   - Defines paths for the encryption key file (`encryption_key.key`), encrypted log file (`Logfile.txt`), and the decrypted log file (`DecryptedLogfile.txt`).

2. **Reading the Encryption Key:**

   - Reads the encryption key from the file.

3. **Initializing the Cipher Suite:**

   - Initializes the cipher suite using the retrieved encryption key.

4. **Decrypting the Log File:**

   - Reads the encrypted log file line by line, decrypts each line, and writes the original keystrokes to `DecryptedLogfile.txt`.

5. **Output:**
   - Prints the path of the decrypted log file.

### Encryption Technique

- **Encryption Library:** `cryptography`
- **Method:** AES encryption using the `Fernet` symmetric encryption algorithm.
- **Process:**
  - Generate a unique encryption key.
  - Encrypt keystroke data before saving it to the log file.
  - Decrypt the log file using the saved encryption key to retrieve original keystrokes.

## Architecture Overview

1. **Keystroke Capturing:**

   - Using the `pynput` library to capture keystrokes and mouse events.

2. **Encryption:**

   - Utilizing the `cryptography` library to securely encrypt the keystrokes before saving them to a log file.

3. **Log File Management:**

   - Storing the encrypted log file locally in the same directory as the keylogger script.

4. **Email Sending:**
   - Sending the encrypted log file to a predefined email address at specified intervals using the `smtplib` library.

## Security and Ethical Considerations

- Ensure you have explicit permission from the computer owner before installing or running such software.
- Unauthorized access to someone's computer is illegal and unethical.
- Handle the decrypted data responsibly and securely.
