# PyLogger

PyLoggy is simple and powerful Python keylogger that is able to log keystrokes, log mouse clicks, take screenshots and more! The tool will send the logs to your email every minute(you can change this) and also save encrypted keystrokes on victims computer.

### Installation

- Run it: `python PyLoggy.py`

### Steps to Run

- Place both the keylogger and decryption scripts in the same directory.
- Run the keylogger script to start capturing keystrokes.
- Run the decryption script to decrypt and view the captured keystrokes.

### Architecture Overview

1. **Keystroke Capturing:** Using the pynput library to capture keystrokes and mouse events.
2. **Encryption:** Utilizing the cryptography library to securely encrypt the keystrokes before saving them to a log file.
3. **Log File Management:** Storing the encrypted log file locally.
4. **Email Sending:** Sending the encrypted log file to a predefined email address at specified intervals.

### Security and Ethical Considerations

- Ensure you have explicit permission from the computer owner before installing or running such software.
- Unauthorized access to someone's computer is illegal and unethical.
- Handle the decrypted data responsibly and securely.
