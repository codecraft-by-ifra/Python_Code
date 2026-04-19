import requests
url = "https://jsonplaceholder.typicode.com"
print("="* 100)

# 1st call- get all posts

r= requests.get(url + "/posts", timeout=20)
print(r.status_code)
posts = r.json()
print(posts)
print("-"* 100)

# 2nd call- get post with id 99

r = requests.get(url + "/posts", params={"id": 99})
print(r.status_code)
post99 = r.json()
print(post99)
print("-"* 100)

# 3rd call- get all posts and print first 3 posts

r= requests.get(url+ "/posts", timeout=20)
posts = r.json()
for post in posts [:3]:
    print(post)
print("-"* 100)

# 4th call- get all users

r = requests.get(url + "/users", timeout=20 )
print(r.status_code)
users = r.json()
print(users)
print("-"* 100)

# 5th call- get all comments

r = requests.get(url + "/comments", timeout=20)
print(r.status_code)
comments = r.json()
print(comments)
print("-"* 100)

# 6th call- post request

new_post1 ={
    "title": "its my first post request",
    "body": "This is the body of my first post request",
     "userId": 100
}
r= requests.post(url + "/posts", json = new_post1)
json = r.json()
print(r.status_code)
print (json)
print("-"* 100)

# 7th call- put request
update_post99 ={
  "userId": 160,
  "id": 99,
  "title": "updated title of post 99",
  "body": "updated body of post 99"
}
r= requests.put(url + "/posts/99", json = update_post99)
json = r.json()
print(r.status_code)
print (json)
print("-"* 100)

# 8th call - delete request
r= requests.delete(url + "/users/99")
print(r.status_code)    
print("-"* 100)

# 9th call - error handling
try:
    r= requests.get(url + "/posts", timeout=20)
    r.raise_for_status
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
print("-"* 100)

# 10th call - get user with posts

def get_user_with_posts(user_id):
    user = requests.get(
        url + f"/users/{user_id}"
    ).json()
    

    posts = requests.get(
        url + "/posts",
        params={"userId": user_id}
    ).json()
    
    print(f"User: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"Total posts: {len(posts)}")
    print("--- Posts ---")
    for post in posts[:5]:   
        print(f"Title:- {post['title']}")
get_user_with_posts(1)
get_user_with_posts(2)
get_user_with_posts(3)
print("="* 100)