import requests


class CommentsApi:
    """
    API client for interacting with /comments endpoint.
    Provides wrapper methods to perform full CRUD operations on comments.
    """

    def __init__(self, base_url: str):
        """
        Initializes the client with the core endpoints.

        :param base_url: The base URL of the target API environment.
        """
        self.url = f"{base_url}/comments"

    def get_all_comments(self, page: int = None, limit: int = None):
        """
        GET /comments?_page={page}&_limit={limit}
        Retrieves a paginated list of comments.

        :param page: The page number to retrieve (e.g., 1).
        :param limit: The number of comments to return per page (e.g., 10).
        :return: A requests.Response object containing an array of comments.
        """
        return requests.get(f"{self.url}?_page={page}&_limit={limit}")
