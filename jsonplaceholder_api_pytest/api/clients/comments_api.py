import requests


class CommentsApi:
    """
    API client for interacting with /comments endpoint.
    Provides wrapper methods to perform full CRUD operations on comments.
    """
    def __init__(self, base_url: str):
        self.url = f"{base_url}/comments"

    # Send GET request to get all comments
    def get_all_comments(self):
        return requests.get(self.url)
