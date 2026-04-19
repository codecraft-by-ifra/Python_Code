import requests
r = requests.get("https://jsonplaceholder.typicode.com/posts",timeout=10)
print(r.status_code)
posts = r.json()
print(posts)
print(f"Total length : {len(posts)}")


# for single post
r = requests.get("https://jsonplaceholder.typicode.com/posts", params={"id": 99})
print(r.status_code)
posts = r.json()
print(posts)
print(f"Total length : {len(posts)}")


# for error handling
url = "https://jsonplaceholder.typicode.com/postss"
try:
    r= requests.get(url, timeout=10)
    print(r.status_code)
    print(r.json())
except requests.exceptions.HTTPError as e:           # server error ho 4xx or 5xx
    print(f"HTTP error occurred: {e} ") 
except requests.exceptions.ConnectionError as e:     # wifi ya internet connection me problem ho
    print(f"Connection error occurred: {e} ")
except requests.exceptions.Timeout as e:             # request time out ho jaye
    print(f"Timeout error occurred: {e} ")
except requests.exceptions.RequestException as e:    # koi bhi aur error ho jaye
    print(f"An error occurred: {e} ")   