import random
import requests

# Define the tokens
tokens = ['console', 'vil1', 'ours', '.com/', 'm', 'l', 't', 'b', 'k', 't', 'l', '.', 'e', 'a']

# Generate 5 strings
for _ in range(5):
    # Shuffle the tokens
    random.shuffle(tokens)
    # Join the shuffled tokens to form a string
    scrambled_string = ''.join(tokens)
    # Add "http://www." at the beginning and ".com" at the end
    domain = "http://www." + scrambled_string
    # Check if domain is valid
    if ".." in domain or domain.count(".") < 2:
        print(f"Generated string: {scrambled_string} - has invalid syntax.")
        continue
    # Write the generated string
    print(f"Generated string: {scrambled_string} - ", end="")
    # Send HTTP request to check domain status
    try:
        response = requests.get(domain)
        if response.status_code == 200:
            print(f"is ACTIVE.")
        else:
            print(f"returned status code: {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"is unreachable.")
