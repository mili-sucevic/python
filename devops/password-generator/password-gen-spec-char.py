import secrets

def generate_password() -> str:
    length = int(input("Enter the password length: "))
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':\",./<>?"
    password = ""
    for i in range(length):
        password += secrets.choice(alphabet)
    return password

print(generate_password())

