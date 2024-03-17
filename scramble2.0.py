import itertools
import signal
import os
import requests

tokens = ['tumblr', 'console', 'vil1', 'leak', '.com/']

def check_url(domain):
    try:
        response = requests.get(domain, timeout=10)
        print(f"active domain: {domain}")
        return domain, response.status_code == 200
    except requests.RequestException as e:
        print(f"No Response: {domain}")
        return domain, False
    
def main():
    active_urls = set()

    # Load active URLs from a file if it exists
    if os.path.exists("active_urls.txt"):
        with open("active_urls.txt", "r") as file:
            active_urls.update(file.read().splitlines())

    # Generate permutations from all tokens
    for perm in itertools.permutations(tokens):
        if '.com/' in perm:
            scrambled_string = ''.join(perm)
            domain = "http://www." + scrambled_string
            if '..' not in domain:  # Exclude permutations with consecutive dots
                try:
                    domain_result = check_url(domain)
                    if domain_result[1]:
                        active_urls.add(domain_result[0])
                        # Write the valid URL to the file immediately
                        with open("active_urls.txt", "a") as file:
                            file.write(domain_result[0] + '\n')
                except Exception as e:
                    print(f"Error occurred for domain {domain}: {e}")

    print("Active URLs:", active_urls)

def signal_handler(sig, frame):
    print("Program terminated by signal")
    exit()

if __name__ == '__main__':
    # Register signal handler for termination signals
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Run the main function
    main()
