import requests


class PostsApi:
    def __init__(self, base_url):
        self.url = f"{base_url}/posts"

    def get_all_posts(self):
        return requests.get(self.url)
    
    def get_single_post(self, post_id):
        return requests.get(f"{self.url}/{post_id}")
    