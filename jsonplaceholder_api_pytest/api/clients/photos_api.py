# File with logic of endpoint "photos"


import requests


class PhotosApi:
    def __init__(self, base_url: str):
        self.url = f"{base_url}/photos"

    # Send GET request to get all photos
    def get_all_photos(self):
        return requests.get(self.url)
    