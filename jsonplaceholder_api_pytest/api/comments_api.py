# File with logic of endpoint "comments"


import requests


class CommentsApi:
    def __init__(self, base_url):
        self.url = f"{base_url}/comments"

    # Send GET request to get all comments
    def get_all_comments(self):
        return requests.get(self.url)
