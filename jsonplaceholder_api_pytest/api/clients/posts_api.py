import requests


class PostsApi:
    """
    API client for interacting with /posts endpoint.
    Provides wrapper methods to perform full CRUD operations on posts.
    """
    def __init__(self, base_url: str):
        """
        Initializes the client with the core endpoints.

        :param base_url: The base URL of the target API environment.
        """
        self.url = f"{base_url}/posts"

    def get_all_posts(self):
        """
        GET /posts
        Retrieves a complete list of all available posts.

        :return: A requests.Response object containing an array of posts.
        """
        return requests.get(self.url)
    
    def get_single_post(self, post_id: int):
        """
        GET /posts/{id}
        Retrieves detailed information for a specific post by its unique ID.

        :param post_id: The unique identifier of the post (e.g., 1).
        :return: A requests.Response object with post data or an error payload.
        """
        return requests.get(f"{self.url}/{post_id}")
    