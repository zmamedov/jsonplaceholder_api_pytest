# File with logic of endpoint "albums"


import requests


class AlbumsApi:
    def __init__(self, base_url):
        self.url = f"{base_url}/albums"

    # Send GET request to get all albums
    def get_all_albums(self):
        return requests.get(self.url)
