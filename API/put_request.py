import requests
r = requests.get("https://jsonplaceholder.typicode.com/posts/99")
print(r.status_code)
posts = r.json()
print(posts)
print(posts["title"])
print(posts[ "userId"])
print(".............................")

update_post99 ={
  "userId": 160,
  "id": 99,
  "title": "updated title of post 99",
  "body": "updated body of post 99"
}
r= requests.put("https://jsonplaceholder.typicode.com/posts/99", json = update_post99)
json = r.json()
print(r.status_code)
print (json)
print(json["title"])
print(json[ "userId"])
print(".............................")


#delete request

r= requests.delete("https://jsonplaceholder.typicode.com/posts/99")
print(r.status_code)


