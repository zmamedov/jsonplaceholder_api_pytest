import requests


class AlbumsApi:
    """
    API client for interacting with /albums endpoint.
    """

    def __init__(self, base_url: str):
        """
        Initializes the client with the core endpoints.

        :param base_url: The base URL of the target API environment.
        """
        self.url = f"{base_url}/albums"

    def get_all_albums(self):
        """
        GET /albums
        Retrieves a complete list of all available albums.

        :return: A requests.Response object containing an array of albums.
        """
        return requests.get(self.url)
