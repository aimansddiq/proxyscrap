from tqdm import tqdm
import requests
import os

timeout = 1
website_to_test = "https://www.example.com"
# Read the contents of the https.txt file
proxytypes = ["https","http","socks4","socks5"]
for proxytype in proxytypes:
    print(f"Testing {proxytype} proxies...")
    proxies = []
    if os.path.exists(f'proxies/{proxytype}.txt'):
        with open(f'proxies/{proxytype}.txt', 'r') as f:
            proxies = [line.strip() for line in f.readlines()]

    # clear existing file, to avoid duplication or outdated working proxies
    working_proxies = []
    with open(f'proxies/working_{proxytype}_proxies.txt', 'w') as f:
        f.write("")
    for proxy in tqdm(proxies):
        try:
            response = requests.get(website_to_test, proxies={'https': proxy}, timeout=timeout)
            if response.status_code == 200:
                working_proxies.append(proxy)
                with open(f'proxies/working_{proxytype}_proxies.txt', 'a') as f:
                    f.write(f"{proxy}\n")
        except requests.exceptions.RequestException as e:
            pass
    print(f"Found {len(working_proxies)} working {proxytype} proxies")