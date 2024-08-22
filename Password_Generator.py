import random
import string

def generate_password(length,uppercase,lowercase,numbers,symbols):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type.")
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter desired password length: "))
        uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
        lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
        numbers = input("Include numbers? (y/n): ").lower() == "y"
        symbols = input("Include symbols? (y/n): ").lower() == "y"

        password = generate_password(length,uppercase,lowercase,numbers,symbols)
        if password:
            print(f"Generated password: {password}")
        else:
            print("Password generation failed. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for password length.")

if __name__ == "__main__":
    main()
