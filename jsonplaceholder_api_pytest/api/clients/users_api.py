# File with logic of endpoint "users"


import requests


class UsersApi:
    def __init__(self, base_url):
        self.url = f"{base_url}/users"

    # Send GET request to get all users
    def get_all_users(self):
        return requests.get(self.url)
