import random
import string


print("\nWELCOME TO THE PASSWORD GENERATOR!\n")


class PasswordGenerator:
    @staticmethod
    def generate_password(length, complexity):
        characters = PasswordGenerator.get_characters(complexity)
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    @staticmethod
    def get_characters(complexity):
        if complexity == "low":
            return string.ascii_lowercase
        elif complexity == "medium":
            return string.ascii_letters + string.digits
        elif complexity == "high":
            return string.ascii_letters + string.digits + string.punctuation
        else:
            raise ValueError("Invalid complexity level. Please choose 'low', 'medium', or 'high'.")


def get_valid_length():
    while True:
        try:
            length = int(input("\nEnter the desired length of the password: "))
            return length
        except ValueError:
            print("Invalid input. Please enter a valid length as an integer.\n")


def get_valid_choice():
    while True:
        choice = input("\nDo you want to create another password? (yes/no): ").lower()
        if choice in ['yes', 'no']:
            return choice
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")


def main():
    try:
        while True:
            length = get_valid_length()
            while True:
                try:
                    complexity = input("Enter the desired complexity level (low/medium/high): ").lower()
                    PasswordGenerator.get_characters(complexity)  # Check complexity validity
                    break
                except ValueError:
                    print("Invalid complexity level. Please choose 'low', 'medium', or 'high'.")

            password = PasswordGenerator.generate_password(length, complexity)
            print(f"Generated Password: {password}")

            another_password = get_valid_choice()
            if another_password != 'yes':
                break

    except (ValueError, TypeError) as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
