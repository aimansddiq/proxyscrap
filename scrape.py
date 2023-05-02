import urllib.request
import requests
import os

folder_name = "proxies"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print("Folder created: ", folder_name)

timeout = 10000 #put your own timeout here

proxytype = ["http","https","socks4","socks5"]
for x in proxytype:
    proxies = requests.get('https://api.proxyscrape.com?request=amountproxies&proxytype={}'.format(x))
    url = 'https://api.proxyscrape.com?request=getproxies&proxytype={}&timeout={}'.format(x,timeout)
    print('Scraping '+ proxies.text +'\t' + x + ' proxies...')
    urllib.request.urlretrieve(url, 'proxies/{}.txt'.format(x))