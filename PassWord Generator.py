import random
import string

def generate_password(length):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Prompt the user to enter the desired password length
password_length = int(input("Enter the desired password length: "))
print("Generated Password:", generate_password(password_length))
