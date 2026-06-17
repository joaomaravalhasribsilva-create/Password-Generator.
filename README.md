# Secure Password Generator

A lightweight command-line utility written in Python to generate random, highly secure passwords.

## 🛠️ How It Works
This project leverages Python's native `secrets` module rather than the standard `random` module. The `secrets` module generates cryptographically strong random numbers, ensuring the resulting passwords are secure enough for account protection.

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed on your system.

### Running the Script
1. Clone this repository or download the source files.
2. Open your terminal or command prompt in the project directory.
3. Run the script using:
   ```bash
   python passwordgenerator.py
   ```
4. Enter your desired password length when prompted.

## 🔒 Security Note
Passwords shorter than 8 characters are vulnerable. For optimal security, a minimum length of 12 to 16 characters is highly recommended.
