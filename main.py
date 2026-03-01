import string
import art
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

print(art.logo)

def check_password_strength(password):
    has_upper = any(char in string.ascii_uppercase for char in password)
    has_lower = any(char in string.ascii_lowercase for char in password)
    has_digit = any(char in string.digits for char in password)
    has_special = any(char in string.punctuation for char in password)

    score = 0

    if len(password) >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"


def display_result(strength):
    if strength == "Weak":
        print(Fore.RED + "❌ Weak Password")
    elif strength == "Medium":
        print(Fore.YELLOW + "⚠️ Medium Password")
    else:
        print(Fore.GREEN + "✅ Strong Password")


def main():
    while True:
        password = input("\nEnter your password: ")
        strength = check_password_strength(password)
        display_result(strength)

        choice = input("\nDo you want to try again? (y/n): ").lower()
        if choice != 'y':
            print(Fore.CYAN + "\nThank you for using Password Strength Checker 🚀")
            break


if __name__ == "__main__":
    main()