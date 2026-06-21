import requests


class UsersApi:
    """
    API client for interacting with /users endpoint.
    """
    
    def __init__(self, base_url: str):
        """
        Initializes the client with the core endpoints.

        :param base_url: The base URL of the target API environment.
        """
        self.url = f"{base_url}/users"

    def get_all_users(self):
        """
        GET /users
        Retrieves a complete list of all available users.

        :return: A requests.Response object containing an array of users.
        """
        return requests.get(self.url)
