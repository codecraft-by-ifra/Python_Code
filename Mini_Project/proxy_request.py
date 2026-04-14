import requests

proxies = {
    "http": "http://xevfapjb:1muy9iwu8wx8@p.webshare.io:80",
     "http": "http://xevfapjb-rotate:1muy9iwu8wx8@p.webshare.io:80"
}

try:
    r = requests.get(
        "https://api64.ipify.org?format=json",
        proxies=proxies,
        timeout=10
    )
    print("Proxy IP:", r.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)