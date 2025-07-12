import random
import string
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Value must be greater than zero. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_yes_or_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['yes', 'no']:
            return choice
        else:
            print("Please enter 'Yes' for yes or 'No' for no.")

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_pool = ""

    if use_letters == 'yes':
        character_pool += string.ascii_letters
    if use_numbers == 'yes':
        character_pool += string.digits
    if use_symbols == 'yes':
        character_pool += string.punctuation

    if not character_pool:
        return "Error: No character set selected."

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password
def main():
    print("Welcome to the Random Password Generator!\n")
    # user preferences
    length = get_positive_integer("Enter the desired password length: ")
    use_letters = get_yes_or_no("Include letters? (Yes/NO): ")
    use_numbers = get_yes_or_no("Include numbers? (Yes/NO): ")
    use_symbols = get_yes_or_no("Include symbols? (Yes/NO): ")
    # Generate password
    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if "Error" in password:
        print(password)
    else:
        print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()