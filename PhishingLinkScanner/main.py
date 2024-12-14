#!/usr/bin/env python3
import PhishingLinkScanner as pls
import pyfiglet
from colorama import init, Fore, Style
import shutil
import time

def display_menu():
    print("\n=== Phishing URL Scanner ===")
    print("\n1️⃣  URL Validation 🔍")
    print("2️⃣  Expand Shortened URL 🔗")
    print("3️⃣  Analyze SSL Certificate 🔒")
    print("4️⃣  Exit 🚪")

    print("============================")
    
def main():
    
    # Dynamically adjust to terminal width
    terminal_width = shutil.get_terminal_size().columns
    ascii_art = pyfiglet.figlet_format("Phishing-Link-Scanner", font="rectangles",width=terminal_width)
    colored_ascii = f"{Fore.BLUE}{Style.BRIGHT}{ascii_art}"
    print(colored_ascii)

    
    linkedin_ss = "https://www.linkedin.com/in/sagar-shahi1221/"
    linkedin_bms = "https://www.linkedin.com/company/brainwave-matrix-solutions"
    
    
    link_ss = f"\033]8;;{linkedin_ss}\033\\@cybterrior\033]8;;\033\\"
    link_bms = f"\033]8;;{linkedin_bms}\033\\Brainwave Matrix Solutions\033]8;;\033\\"
    
    print(f"{Fore.RED}V-1.0\n")
    print(f"{Fore.GREEN}Created by {Style.BRIGHT}{link_ss}{Style.RESET_ALL}{Fore.GREEN} during an internship at {Style.BRIGHT}{link_bms}{Style.RESET_ALL}.\n")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            url = input("\nEnter the URL to validate: ")
            is_legit = True
            domain, parsed = pls.validate_and_parse_url(url)
            
            # If the domain is well structed then check in phishing domains and for typosquatting
            if domain:                
                if is_legit:
                    print(f"{Fore.BLUE}\nScanning for Typosquatting...🔍{Style.RESET_ALL}")
                    time.sleep(1)
                    typo_status,typo_output = pls.typo_check(domain)
                    print(typo_output)
                    if typo_status is False:
                        is_legit = True
                    else:
                        is_legit = False
                
                with open('ALL-phishing-domains.txt') as pd:
                    phishing_domains = [line.strip() for line in pd.readlines()]
                if is_legit:
                    print(f"{Fore.BLUE}\nScanning in the Phishing Domains list...🔍{Style.RESET_ALL}")
                    time.sleep(1)
                    for i in phishing_domains:
                        if domain in i:
                            print(f"{Fore.RED}🚨 Phishing Domain Detected 🚩{Style.RESET_ALL}: {i}")
                            is_legit = False
                            break
                
                    if is_legit:
                        print(f"{Fore.GREEN}✅ Not Found in the Phishing Domains list 🛑{Style.RESET_ALL}")

                with open('ALL-phishing-links.txt') as pl:
                    phishing_links = [line.strip() for line in pl.readlines()]
                if is_legit:
                    print(f"{Fore.BLUE}\nScanning in the Phishing Links list...🔍{Style.RESET_ALL}")
                    time.sleep(1)
                    for i in phishing_links:
                        if url in phishing_links:
                            print(f"{Fore.RED}🚨 Phishing Link Detected 🚩: {url}{Style.RESET_ALL}")
                            is_legit = False
                            break
                
                if is_legit:
                        print(f"{Fore.GREEN}✅ Not Found in the Phishing Links list 🛑{Style.RESET_ALL}")

                if is_legit:
                    print(f"{Fore.GREEN}\nValidated Domain ✅{Style.RESET_ALL}: {domain}")
                    print(f"Full URL Components 🔒: {parsed}")
            
            else:
                print(f"{Fore.RED}Error {Style.RESET_ALL}: {parsed}")

        elif choice == "2":
            short_url = input("\nEnter the shortened URL: ")
            expanded_url = pls.expand_shortened_url(short_url)
            print(f"{Fore.BLUE}\nExpanding the URL...🔍{Style.RESET_ALL}")
            time.sleep(1)
            print(f"Expanded URL 🚨: {expanded_url}")

        elif choice == "3":
            domain = input("\nEnter the domain (e.g., google.com): ")
            extracted = pls.tldextract.extract(domain)
            domain = extracted.domain+"."+extracted.suffix
            ssl_info = pls.analyze_ssl_certificate(domain)
            print(f"{Fore.BLUE}\nAnalyzing the SSL/TLS Certificate...🔍{Style.RESET_ALL}")
            time.sleep(1)
            if isinstance(ssl_info, dict):
                print(f"Issuer: {ssl_info['issuer']}")
                print(f"Valid From: {ssl_info['valid_from']}")
                print(f"Valid To: {ssl_info['valid_to']}")
                print(f"Is Expired: {ssl_info['expired']}")
            else:
                print(ssl_info)
        
        elif choice == "4":
            print(f"{Fore.BLUE}\nExiting the program ⬅️ . Stay safe! 🛡️{Style.RESET_ALL}")
            time.sleep(1)   
            break
        
        else:
            print(f"{Fore.RED}\nInvalid choice ❌. Please try again 🔁.{Style.RESET_ALL}    ")

if __name__ == "__main__":
    main()