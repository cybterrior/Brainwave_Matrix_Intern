# 1. URL Validation and Parsing
# """
from urllib.parse import urlparse

def validate_and_parse_url(url):
    try:
        # Parse the URL to extract components
        parsed_url = urlparse(url)
        
        # Validate URL structure by checking scheme and domain (netloc)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError("Invalid URL format")
        
        # Normalize domain (e.g., remove www and convert to lowercase)
        domain = parsed_url.netloc.lower()

        return domain, parsed_url  # Return the domain and parsed components
    except Exception as e:
        return None, str(e)

"""
# Example usage
url = input("Enter the URL: ")
domain, parsed = validate_and_parse_url(url)
if domain:
    print(f"Validated Domain: {domain}")
else:
    print(f"Error: {parsed}")

# This approach ensures that only valid URLs proceed to the next steps and that the domain is consistently formatted.
"""

# 2. Shortened URL Expansion
# """
import requests

def expand_shortened_url(url):
    try:
        # Send a HEAD request to follow redirects and get the final URL
        response = requests.head(url, allow_redirects=True, timeout=10)
        return response.url  # Return the expanded URL
    except requests.RequestException as e:
        return f"Error expanding URL: {e}"
    
"""
# Example usage
short_url = input("Enter the shortened URL: ")
expanded_url = expand_shortened_url(short_url)
print(f"Expanded URL: {expanded_url}")
"""

# 3. SSL Certificate Analysis
# """
# To check whether the site is trustworthy or not by checking the validity (e.g., expiration date) and issuer of the SSL certificate
import ssl
import socket
from datetime import datetime

def analyze_ssl_certificate(domain):
    try:
        # Create a secure SSL context
        context = ssl.create_default_context()
        
        # Connect to the server using SSL
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()  # Get the SSL certificate
        
        # Extract certificate details
        issuer = cert.get("issuer", [])
        valid_from = datetime.strptime(cert["notBefore"], "%b %d %H:%M:%S %Y %Z")
        valid_to = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
        
        # Check if the certificate is expired
        return {
            "issuer": issuer,
            "valid_from": valid_from,
            "valid_to": valid_to,
            "expired": valid_to < datetime.now()
        }
    except Exception as e:
        return f"SSL analysis failed: {e}"

"""
# Example usage
domain = input("Enter the domain: ")
if domain:
    # ssl_info = analyze_ssl_certificate(domain)
    # print(f"SSL Info: {ssl_info}")
    
    ssl_info = analyze_ssl_certificate(domain)
    if isinstance(ssl_info, dict):
        print(f"Issuer: {ssl_info['issuer']}")
        print(f"Valid From: {ssl_info['valid_from']}")
        print(f"Valid To: {ssl_info['valid_to']}")
        print(f"Is Expired: {ssl_info['expired']}")
    else:
        print(ssl_info)
        print("Untrustworthy SSL certificate")

else:
    print("Domain Error")
"""

# 4. Homoglyph Attack/Typosquatting

import Levenshtein as lv
import tldextract
from colorama import Fore,Style

domains_for_typo = [
    'facebook.com', 'google.com', 'paypal.com', 'amazon.com', 'bankofamerica.com',
    'twitter.com', 'instagram.com', 'linkedin.com', 'microsoft.com', 'apple.com',
    'netflix.com', 'yahoo.com', 'bing.com', 'adobe.com', 'dropbox.com',
    'github.com', 'salesforce.com', 'uber.com', 'airbnb.com', 'spotify.com',
    'ebay.com', 'alibaba.com', 'walmart.com', 'target.com', 'bestbuy.com',
    'chase.com', 'citibank.com', 'wellsfargo.com', 'hulu.com', 'tiktok.com',
    'reddit.com', 'pinterest.com', 'quora.com', 'medium.com', 'whatsapp.com',
    'wechat.com', 'snapchat.com', 'tumblr.com', 'vimeo.com', 'dailymotion.com'
]

def typo_check(domain):
    extracted = tldextract.extract(domain)
    sld_tld = extracted.domain+"."+extracted.suffix
    
    # Check for similarity with legitimate domains
    for legit_domain in domains_for_typo:
        similarity = lv.ratio(sld_tld, legit_domain)
        if sld_tld.lower() == legit_domain:
            return False,f"{Fore.GREEN}✅🔒No Homoglyph Pattern Found In The Domain🔒✅{Style.RESET_ALL}: {sld_tld}"
        elif lv.distance(sld_tld,legit_domain)<5:
            return True,f"⚠️🚩 {Fore.RED}Misspelled URL{Style.RESET_ALL}: {sld_tld} - Similar to {legit_domain} 🚩⚠️"
    
    # Step 3: If not malicious or similar to legitimate, it's off the list
    return False,f"{Fore.BLACK}🔍🚫 No Homoglyph Found for: {sld_tld} 🚫🔍{Style.RESET_ALL}"

"""
# # Input from user
# url_check = input("Enter the domain: ")
# print(typo_check(url_check))
"""

# 5. Scanning for Phishing Domains
# 6. Scanning for Phishing Links

# 7. User-Friendly Interface
