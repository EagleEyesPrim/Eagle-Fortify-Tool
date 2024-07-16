import random
import string
import os
import pyperclip
from colorama import Fore, init

init(autoreset=True)

try:
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("Eagle Fortify Tool")
except:
    pass

def generate_password(charset, length=12, require_all_types=False):
    if require_all_types:
        password = []
        password.append(random.choice(string.digits))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(')!@#$%^&*(-=_+:;\'./?><,~\\|'))
        while len(password) < length:
            password.append(random.choice(charset))
        random.shuffle(password)
        return ''.join(password)
    else:
        return ''.join(random.choice(charset) for _ in range(length))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    print(f"{Fore.CYAN}╔═══════════════════════════════════════════╗")
    print(f"{Fore.CYAN}║                                           ║")
    print(f"{Fore.CYAN}║             Eagle Fortify Tool            ║")
    print(f"{Fore.CYAN}║                                           ║")
    print(f"{Fore.CYAN}╚═══════════════════════════════════════════╝")

def display_tips():
    tips = [
        "Use a unique password for every account.",
        "Avoid using easily guessable information like your name or birthdate.",
        "Consider using a password manager to generate and store complex passwords.",
        "Enable two-factor authentication (2FA) on accounts that support it.",
        "Change your passwords regularly and avoid reusing them across different sites.",
        "Keep your operating system and software up to date with the latest patches.",
        "Be cautious of phishing attempts and suspicious links in emails or messages.",
        "Use HTTPS websites for sensitive transactions and avoid public Wi-Fi for confidential activities.",
        "Review your account activity regularly for any unauthorized access or suspicious behavior.",
        "Backup important data regularly to secure locations or cloud storage.",
        "Use a firewall and antivirus software to protect your devices from malware and unauthorized access.",
        "Avoid sharing personal information or passwords over the phone, email, or social media.",
        "Consider using biometric authentication (like fingerprint or face recognition) where available.",
        "Educate yourself about common cybersecurity threats and best practices for online safety.",
        "Limit the amount of personal information you share online and on social media platforms.",
        "Use strong and unique answers to security questions that are not easily guessable or publicly available.",
        "Avoid downloading software or apps from untrusted sources.",
        "Use a VPN (Virtual Private Network) when accessing public or unsecured networks.",
        "Regularly review privacy settings on social media and other online accounts.",
        "Use encryption for sensitive data such as financial information or personal documents.",
        "Be mindful of physical security for your devices, such as locking them when not in use."
    ]
    
    random.shuffle(tips)  # shuffle tips list

    # Select random 5 tips
    selected_tips = random.sample(tips, k=5)

    print(f"\n{Fore.LIGHTBLACK_EX}Security Tips:")
    for index, tip in enumerate(selected_tips, start=1):
        print(f"{Fore.LIGHTBLACK_EX}{index}. {tip}")

def analyze_password_strength(password):
    length = len(password)
    has_digit = any(char.isdigit() for char in password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_special = any(char in '!)@#$%^&*(-=_+:;\'./?><,~\\|' for char in password)

    if length >= 12 and has_digit and has_lower and has_upper and has_special:
        strength = f"{Fore.GREEN}Strong"
    elif length >= 8 and (has_digit or has_lower or has_upper or has_special):
        strength = f"{Fore.YELLOW}Moderate"
    else:
        strength = f"{Fore.RED}Weak"

    return strength

def print_box(content):
    lines = content.split('\n')
    width = max(len(line) for line in lines) + 4
    print(f"{Fore.CYAN}╔" + "═" * (width - 2) + "╗")
    for line in lines:
        print(f"{Fore.CYAN}║ " + line.ljust(width - 4) + " ║")
    print(f"{Fore.CYAN}╚" + "═" * (width - 2) + "╝")

def generate_custom_email_and_password(first_name, last_name, favorite_food, city, birthdate, email_domain):
    charset = string.digits + string.ascii_letters + ")!@#$%^&*(-=_+:;\'./?><,~\\|"
    require_all_types = True
    password_length = 16
    password = generate_password(charset, password_length, require_all_types)

    user_data = first_name + last_name + favorite_food + city + birthdate
    email_local_part = ''.join(random.sample(user_data, len(user_data)))
    email = f"{first_name.lower()}.{email_local_part[:8].lower()}@{email_domain}"

    return email, password

def main():
    try:
        while True:
            clear_screen()
            print_title()
            print(f"\nSelect the password operation:")
            print(f"{Fore.CYAN}[1] Generate a New Password")
            print(f"{Fore.CYAN}[2] Improve Existing Password")
            print(f"{Fore.CYAN}[3] Generate Custom Email and Password")
            print(f"{Fore.RED}[4] Exit")
            
            choice = input("Enter your choice [1/2/3/4]: ")
            
            if choice == '1':
                while True:
                    clear_screen()
                    print_title()
                    print(f"\nSelect the password generation algorithm:")
                    print(f"{Fore.CYAN}[1] Low Normal Algorithm (For simple accounts, temporary access)")
                    print(f"{Fore.CYAN}[2] Acceptable Algorithm (For general accounts, moderate security needs)")
                    print(f"{Fore.CYAN}[3] Security Algorithm (For high-security accounts, sensitive data)")
                    print(f"{Fore.LIGHTRED_EX}[4] Go Back")
                    
                    password_choice = input("Enter your choice [1/2/3/4]: ")
                    
                    if password_choice == '4':
                        break
                    
                    if password_choice == '1':
                        charset = "0123456789" + "888555222" + "ABCDEF" + "abcdef"
                        description = "Low Normal Algorithm is suitable for simple accounts \nand temporary access where security is not a major concern."
                        require_all_types = False
                        password_length = int(input("Enter the password length: "))
                        password = generate_password(charset, password_length, require_all_types)
                        
                    elif password_choice == '2':
                        charset = ")!@#$%^&*(-=_+:;\'./?><,~\\|" + string.ascii_letters
                        description = "Acceptable Algorithm is suitable for general accounts with moderate security needs, \nsuch as social media or non-sensitive email accounts."
                        require_all_types = input(f"Require at least one of each character type {Fore.LIGHTGREEN_EX}(y/n){Fore.RESET}: ").lower() == 'y'
                        password_length = int(input("Enter the password length: "))
                        password = generate_password(charset, password_length, require_all_types)
                        
                    elif password_choice == '3':
                        charset = string.digits + string.ascii_letters + ")!@#$%^&*(-=_+:;\'./?><,~\\|"
                        description = "Security Algorithm is suitable for high-security accounts and sensitive data, \nsuch as online banking or confidential business accounts."
                        require_all_types = input(f"Require at least one of each character type {Fore.LIGHTGREEN_EX}(y/n){Fore.RESET}: ").lower() == 'y'
                        while True:
                            password_length = int(input(f"Enter the password length {Fore.LIGHTGREEN_EX}(minimum 12){Fore.RESET}: "))
                            if password_length >= 12:
                                break
                            else:
                                print("Password length must be at least 12. Please try again.")
                        password = generate_password(charset, password_length, require_all_types)
                    else:
                        print("Invalid choice. Please try again.")
                        continue

                    result = f"\nGenerated Password:\n{password}\n\nStrength: {analyze_password_strength(password)}\n\n{description}"
                    print_box(result)

                    # Copy password to clipboard
                    pyperclip.copy(password)
                    print("\nPassword has been copied to clipboard.")
                    display_tips()

                    input("\nPress Enter to continue...")

            elif choice == '2':
                while True:
                    clear_screen()
                    print_title()
                    current_password = input("Enter your current password: ")
                    
                    print(f"\nSelect the password improvement algorithm:")
                    print(f"{Fore.CYAN}[1] Mix Character Positions")
                    print(f"{Fore.CYAN}[2] Add Special Characters")
                    print(f"{Fore.CYAN}[3] Expand and Modify Password")
                    print(f"{Fore.CYAN}[4] Add Random Prefix or Suffix")
                    print(f"{Fore.LIGHTRED_EX}[5] Go Back")
                    
                    improve_choice = input("Enter your choice [1/2/3/4/5]: ")
                    
                    if improve_choice == '5':
                        break
                    
                    if improve_choice == '1':
                        modified_password = list(current_password)
                        random.shuffle(modified_password)
                        password = ''.join(modified_password)
                        description = "Mixed Character Positions"
                        
                    elif improve_choice == '2':
                        additional_characters = ')!@#$%^&*(-=_+:;\'./?><,~\\|'
                        password = current_password + random.choice(additional_characters)
                        description = "Added Special Characters"
                        
                    elif improve_choice == '3':
                        password_length = random.randint(12, 24)
                        charset = string.digits + string.ascii_letters + ')!@#$%^&*(-=_+:;\'./?><,~\\|'
                        password = generate_password(charset, password_length, require_all_types=True)
                        description = "Expanded and Modified Password"

                    elif improve_choice == '4':
                        random_prefix = ''.join(random.choices(string.ascii_letters + string.digits + ')!@#$%^&*(-=_+:;\'./?><,~\\|', k=4))
                        random_suffix = ''.join(random.choices(string.ascii_letters + string.digits + ')!@#$%^&*(-=_+:;\'./?><,~\\|', k=4))
                        password = random_prefix + current_password + random_suffix
                        description = "Added Random Prefix or Suffix"

                    else:
                        print("Invalid choice. Please try again.")
                        continue
                    
                    result = f"\nImproved Password:\n{password}\n\nStrength: {analyze_password_strength(password)}\n\nDescription: {description}"
                    print_box(result)
                    
                    # Copy improved password to clipboard
                    pyperclip.copy(password)
                    print("\nImproved password has been copied to clipboard.")
                    display_tips()

                    input("\nPress Enter to continue...")

            elif choice == '3':
                clear_screen()
                print_title()

                def get_input(prompt, validation_func=None):
                    while True:
                        user_input = input(prompt)
                        if validation_func:
                            if validation_func(user_input):
                                return user_input
                            else:
                                print("Invalid input. Please try again.")
                        else:
                            return user_input

                def is_valid_date(date_str):
                    return len(date_str) == 8 and date_str.isdigit()

                first_name = get_input(f"{Fore.LIGHTYELLOW_EX}Enter your first name: {Fore.RESET}")
                last_name = get_input(f"{Fore.LIGHTYELLOW_EX}Enter your last name: {Fore.RESET}")
                favorite_food = get_input(f"{Fore.LIGHTYELLOW_EX}Enter your favorite food: {Fore.RESET}")
                city = get_input(f"{Fore.LIGHTYELLOW_EX}Enter your city: {Fore.RESET}")
                birthdate = get_input(f"{Fore.LIGHTYELLOW_EX}Enter your birthdate {Fore.LIGHTGREEN_EX}(DDMMYYYY){Fore.LIGHTYELLOW_EX}: {Fore.RESET}", is_valid_date)
                
                #################################################################
                #                             Domains                           #
                #################################################################
                print("\nSelect email domain:")
                print(f"{Fore.CYAN}[1] outlook.com")
                print(f"{Fore.CYAN}[2] gmail.com")
                print(f"{Fore.CYAN}[3] yahoo.com")
                print(f"{Fore.CYAN}[4] hotmail.com")
                print(f"{Fore.CYAN}[5] aol.com")
                print(f"{Fore.CYAN}[6] icloud.com")
                print(f"{Fore.CYAN}[7] protonmail.com")
                print(f"{Fore.CYAN}[8] zoho.com")
                print(f"{Fore.CYAN}[9] mail.com")
                print(f"{Fore.CYAN}[10] yandex.com")
                print(f"{Fore.CYAN}[11] live.com")
                print(f"{Fore.CYAN}[12] rocketmail.com")
                print(f"{Fore.CYAN}[13] mail.ru")
                print(f"{Fore.CYAN}[14] fastmail.com")
                print(f"{Fore.CYAN}[15] inbox.com")
                print(f"{Fore.CYAN}[16] me.com")
                print(f"{Fore.CYAN}[17] custom domain")
                email_domain_choice = input("Enter your choice [1-17]: ")

                if email_domain_choice == '1':
                    email_domain = "outlook.com"
                elif email_domain_choice == '2':
                    email_domain = "gmail.com"
                elif email_domain_choice == '3':
                    email_domain = "yahoo.com"
                elif email_domain_choice == '4':
                    email_domain = "hotmail.com"
                elif email_domain_choice == '5':
                    email_domain = "aol.com"
                elif email_domain_choice == '6':
                    email_domain = "icloud.com"
                elif email_domain_choice == '7':
                    email_domain = "protonmail.com"
                elif email_domain_choice == '8':
                    email_domain = "zoho.com"
                elif email_domain_choice == '9':
                    email_domain = "mail.com"
                elif email_domain_choice == '10':
                    email_domain = "yandex.com"
                elif email_domain_choice == '11':
                    email_domain = "live.com"
                elif email_domain_choice == '12':
                    email_domain = "rocketmail.com"
                elif email_domain_choice == '13':
                    email_domain = "mail.ru"
                elif email_domain_choice == '14':
                    email_domain = "fastmail.com"
                elif email_domain_choice == '15':
                    email_domain = "inbox.com"
                elif email_domain_choice == '16':
                    email_domain = "me.com"
                elif email_domain_choice == '17':
                    email_domain = input("Enter your custom domain: ")
                else:
                    print("Invalid choice. Using default domain 'example.com'.")
                    email_domain = "example.com"

                #################################################################

                email, password = generate_custom_email_and_password(first_name, last_name, favorite_food, city, birthdate, email_domain)
                result = f"\nGenerated Custom Email and Password:\n Email: {email}\n Password: {password}\n\n Strength: {analyze_password_strength(password)}"
                print_box(result)
                
                # Copy email and password to clipboard
                pyperclip.copy(f"Email: {email}\n Password: {password}")
                print("\nCustom email and password have been copied to clipboard.")
                display_tips()

                input("\nPress Enter to continue...")

            elif choice == '4':
                print("Exiting Eagle Fortify Tool. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

    except KeyboardInterrupt:
        print("\nTool interrupted. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
