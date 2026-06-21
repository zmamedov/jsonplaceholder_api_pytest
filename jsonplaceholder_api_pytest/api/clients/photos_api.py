# File with logic of endpoint "photos"


import requests


class PhotosApi:
    """
    API client for interacting with /photos endpoint.
    """

    def __init__(self, base_url: str):
        """
        Initializes the client with the core endpoints.

        :param base_url: The base URL of the target API environment.
        """
        self.url = f"{base_url}/photos"

    def get_all_photos(self, page: int = None, limit: int = None):
        """
        GET /photos?_page={page}&_limit={limit}
        Retrieves a paginated list of photos.

        :param page: The page number to retrieve (e.g., 1).
        :param limit: The number of photos to return per page (e.g., 10).
        :return: A requests.Response object containing an array of photos.
        """
        return requests.get(f"{self.url}?_page={page}&_limit={limit}")
