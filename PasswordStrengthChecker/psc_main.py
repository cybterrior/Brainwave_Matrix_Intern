#!/usr/bin/env python3
import re
from colorama import Fore, Style, init
import pyfiglet
import shutil

def password_strength_checker(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Check for password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Make your password at least 8 characters long.")

    # Check for character complexity
    if re.search(r'[A-Z]', password):  # At least one uppercase letter
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):  # At least one lowercase letter
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'\d', password):  # At least one digit
        score += 1
    else:
        feedback.append("Include at least one numeric digit.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # At least one special character
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Check for uniqueness (no obvious patterns like '123', 'aaaa', etc.)
    if re.search(r'(.)\1{2,}', password):  # Repeated characters
        feedback.append("Avoid repeated characters like 'aaa' or '111'.")
    else:
        score += 1

    # Final assessment
    if score >= 7:
        strength = f"{Fore.GREEN}Strong{Style.RESET_ALL}"
    elif 4 <= score < 7:
        strength = f"{Fore.YELLOW}Moderate{Style.RESET_ALL}"
    else:
        strength = f"{Fore.RED}Weak{Style.RESET_ALL}"

    # Display results
    print(f"Password Strength: {strength}\n")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    else:
        print(Fore.BLUE + "✅ Your password is strong enough."+Style.RESET_ALL)


def main():
    tool_name = "Password-Strength-Checker"
    terminal_width = shutil.get_terminal_size().columns
    ascii_art = pyfiglet.figlet_format(tool_name, font="slant",width=terminal_width)
    colored_ascii = f"{Fore.BLUE}{Style.BRIGHT}{ascii_art}"
    print(colored_ascii)

    linkedin_ss = "https://www.linkedin.com/in/sagar-shahi1221/"
    linkedin_bms = "https://www.linkedin.com/company/brainwave-matrix-solutions"
    
    
    link_ss = f"\033]8;;{linkedin_ss}\033\\@cybterrior\033]8;;\033\\"
    link_bms = f"\033]8;;{linkedin_bms}\033\\Brainwave Matrix Solutions\033]8;;\033\\"
    
    print(f"{Fore.RED}V-1.0\n")
    print(f"{Fore.GREEN}Created by {Style.BRIGHT}{link_ss}{Style.RESET_ALL}{Fore.GREEN} during an internship at {Style.BRIGHT}{link_bms}{Style.RESET_ALL}.\n")
    
    while True:
        user_password = input(Fore.GREEN + "\n🔑 Enter your password to check its strength (or press 'q' to quit): " + Style.RESET_ALL)
        
        if user_password.lower() == 'q':
            print(Fore.CYAN + "Goodbye! 👋")
            break

        password_strength_checker(user_password)


# Example usage
if __name__ == "__main__":
    main()