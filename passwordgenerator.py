import secrets
import string


def generate_password(length):
    # 1. Define available character groups
    letters = string.ascii_letters  # Contains "abcdef...XYZ"
    digits = string.digits  # Contains "0123456789"
    symbols = string.punctuation  # Contains "!@#$%..."

    # 2. Combine all characters into one single string
    all_characters = letters + digits + symbols

    # 3. Select random characters cryptographically
    password = "".join(
        secrets.choice(all_characters) for _ in range(length)
    )

    return password


# --- User Interaction ---
print("--- SECURE PASSWORD GENERATOR ---")

try:
    # Ask for length and convert to integer
    desired_length = int(input("Enter password length (e.g., 12): "))

    # Enforce a minimum safety standard
    if desired_length < 8:
        print("Warning: Passwords shorter than 8 characters are not secure!")

    # Generate and display the password
    final_password = generate_password(desired_length)
    print(f"Your secure password is: {final_password}")

except ValueError:
    print("Error: Please enter a valid number.")