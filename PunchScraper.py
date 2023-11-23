import requests

def make_http_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for any HTTP error
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error 202 - PunchScraper", e)
        return None

def save_data_to_file(data, filename):
    try:
        with open(filename, 'a') as file:
            file.write(data + "\n")
        print("Working 303 - PunchScraper")
    except IOError as e:
        print("Error 101 - PunchScraper", e)

# List of URLs
urls = [
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/fahimscirex/proxybd/master/proxylist/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
    "https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt",
    "https://raw.githubusercontent.com/yoannchb-pro/https-proxies/main/proxies.txt",
    "https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/all.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt",
    "https://raw.githubusercontent.com/iptotal/free-proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
    "https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/http.txt",
    "https://raw.githubusercontent.com/gugun0977/my-proxy-list/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/proxies.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt",
    "https://raw.githubusercontent.com/cryptotyler/ProxyList-Scraping/master/http.txt",
    "https://raw.githubusercontent.com/caliwyr/Proxy-List/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/Bardiafa/Proxy-Leecher/main/good.txt"
]

# Output filename
filename = "PunchScraped.txt"

# Process each URL
for url in urls:
    data = make_http_request(url)
    if data is not None:
        save_data_to_file(data, filename)
