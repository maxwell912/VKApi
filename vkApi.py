import requests

from models import User, Album

root = "https://api.vk.com/method/"
access_token = "e1fabf6be1fabf6be1fabf6b61e1889d1dee1fae1fabf6bbf3259d59ef27c5881c05958"
count = 10
payload = {"count": count,
           "v": "5.103",
           "access_token": access_token}


def request(f):
    def func(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except KeyError:
            return "Bad request"
    return func


@request
def get_user_friends(user_id):
    c = {"user_id": user_id,
         "order": 'name',
         "fields": "online"}
    res = requests.get(root + "friends.get", params={**payload, **c})

    data = res.json()
    res = ''
    for friend in [User.from_dict(user_dict) for user_dict in data['response']['items']]:
        res += str(friend) + '\n'
    return res


@request
def get_user_albums(user_id):
    c = {"owner_id": user_id}
    res = requests.get(root + "photos.getAlbums", params={**payload, **c})

    data = res.json()
    albums = data['response']['items']
    res = ''
    for album in [Album.from_dict(album_dict) for album_dict in albums]:
        res += str(album) + '\n'
    return res


@request
def get_user_music(user_id):
    c = {"user_id": user_id,
         "fields": "music"}
    res = requests.get(root + "users.get", params={**payload, **c})

    data = res.json()
    return data['response'][0]['music']


def run():
    print("Enter user id. Example: 6492")
    user_id = input()
    try:
        int(user_id)
    except ValueError:
        print("Wrong id")
        return
    while True:
        print("Enter user command")
        print("Available: exit, friends, albums, music")

        command = input()
        if command == "exit":
            break
        elif command == "friends":
            print(get_user_friends(user_id))
        elif command == "albums":
            print(get_user_albums(user_id))
        elif command == "music":
            print(get_user_music(user_id))


if __name__ == '__main__':
    while True:
        print("Enter command")
        print("Available: exit, user, help")
        command = input()
        if command == "exit":
            break
        elif command == "user":
            run()
        elif command == "help":
            print("Медведев Иван КН203")
