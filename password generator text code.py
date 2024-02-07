import random
import string

def generate_password(length=12):
    # Combine lowercase, uppercase, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least one character from each category
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    # Generate the rest of the password
    for _ in range(length - 4):
        password += random.choice(characters)

    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Example: Generate a password with default length (12 characters)
generated_password = generate_password()
print("Generated Password:", generated_password)
