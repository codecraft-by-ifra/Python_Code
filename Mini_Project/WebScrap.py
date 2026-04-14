import requests
import os

url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKUVN5Z0FQAQ?hl=en-PK&gl=PK&ceid=PK%3Aen"

proxies = {
    "http": "http://xevfapjb-rotate:1muy9iwu8wx8@p.webshare.io:80",
    "http": "http://xevfapjb-rotate:1muy9iwu8wx8@p.webshare.io:80"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def Fetch_SaveToFile(url, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    try:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=15)
        response.raise_for_status()

        with open(path, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"✅ Data successfully saved to {path}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")

Fetch_SaveToFile(url, "Scrapdata/data.html")