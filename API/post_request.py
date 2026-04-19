import requests
new_post1 ={
    "title": "its my first post request",
    "body": "This is the body of my first post request",
     "userId": 100
}
r= requests.post("https://jsonplaceholder.typicode.com/posts", json = new_post1)
json = r.json()
print(r.status_code)
print (json)
print(json["title"])
print(json[ "userId"])


new_post2 ={
    "title": "its my 2nd post request",
    "body": "This is the body of my 2nd post request",
     "userId": 102
}
r= requests.post("https://jsonplaceholder.typicode.com/posts", json = new_post2)
json = r.json()
print(r.status_code)
print (json)
print(json["title"])
print(json[ "userId"])



def get_user_with_posts(user_id):
    # User ka data lao
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    ).json()
    
    # Uske posts lao
    posts = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"userId": user_id}
    ).json()
    
    print(f"User: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"Total posts: {len(posts)}")
    print("--- Posts ---")
    for post in posts[:3]:   # pehle 3 posts
        print(f"Title:- {post['title']}")

get_user_with_posts(1)


