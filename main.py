import requests
import random
import string
import json

def generate_random_username():
    length = random.randint(1, 25)
    characters = string.ascii_lowercase + string.digits + "._"
    return ''.join(random.choice(characters) for _ in range(length))

def check_minecraft_username(username, premium_data, not_data):
    base_url = "https://api.mojang.com/users/profiles/minecraft/"
    response = requests.get(base_url + username)

    if response.status_code == 200:
        data = response.json()
        if 'name' in data:
            result = {
                "name": data["name"],
                "skin": f"https://mc-heads.net/skin/{username}",
                "head": f"https://mc-heads.net/avatar/{username}"
            }
            premium_data[username] = result
            save_to_json(premium_data, "premium.json")
            return True
    not_data[username] = "Not Exists"
    save_to_json(not_data, "Not.json")
    return False

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    num_usernames = 10000 # 10000 ~ 2h
    premium_data = {}
    not_data = {}

    for _ in range(num_usernames):
        random_username = generate_random_username()
        check_minecraft_username(random_username, premium_data, not_data)
