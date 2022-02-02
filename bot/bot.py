import configparser
import string
import requests
import random

def configFile():
    config = configparser.RawConfigParser()
    config.read_file(open('config.ini'))
    confDict = {
        'number_of_users' : int(config['DEFAULT']['number_of_users']),
        'max_posts_per_user' : int(config['DEFAULT']['max_posts_per_user']),
        'max_likes_per_user' : int(config['DEFAULT']['max_likes_per_user'])
    }
    return confDict

def registerUsers(confDict):
    users = list()
    for x in range(confDict["number_of_users"]):
        user = {
            "username" : ''.join(random.sample(string.ascii_lowercase,8)),
            "email" : ''.join(random.sample(string.ascii_lowercase,8))+"@gmail.com",
            "password" : ''.join(random.sample(string.ascii_lowercase,8))
        }
        requests.post('http://127.0.0.1:8000/api/register/', data=user)
        
        users.append(user)
    print("Users created")
    return users

def loginUsers(users):
    for user in users:
        login = {"username":user["username"], "password":user["password"]}
        r = requests.post('http://127.0.0.1:8000/api/login/', data=login)
        user["token"] = r.json()['token']
    return users

def createPosts(users):
    posts = list()
    
    for user in users:
        for p in range(confDict["max_posts_per_user"]):
            post = {
                "title" : ''.join(random.sample(string.ascii_lowercase,8)),
                "content" : 'content sample'
            }
            r = requests.post('http://127.0.0.1:8000/api/createPost/',data=post,headers={'Authorization':'Bearer '+user['token']})
            post["id"] = r.json()['id']
            posts.append(post)
    print("Posts created")
    return posts

def likePosts(users):
    for user in users:
        for l in range(confDict["max_likes_per_user"]):
            postid = str(posts[random.randint(0,len(posts))]["id"])
            r = requests.post('http://127.0.0.1:8000/api/likePost/'+postid+'/', headers={'Authorization':'Bearer '+user['token']})
            
    print("Posts liked")

if __name__ == '__main__':
    confDict = configFile()
    users = registerUsers(confDict)
    users = loginUsers(users)
    posts = createPosts(users)
    likePosts(users)
    print(users)
    print(posts)
    