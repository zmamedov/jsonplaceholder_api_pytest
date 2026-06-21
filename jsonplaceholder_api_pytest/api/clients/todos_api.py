import requests


class TodosApi:
    """
    API client for interacting with /todos endpoint.
    """

    def __init__(self, base_url: str):
        """
        Initializes the client with the core endpoints.

        :param base_url: The base URL of the target API environment.
        """
        self.url = f"{base_url}/todos"

    def get_all_todos(self):
        """
        GET /todos
        Retrieves a complete list of all available todos.

        :return: A requests.Response object containing an array of todos.
        """
        return requests.get(self.url)
