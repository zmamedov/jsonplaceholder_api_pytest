# File with logic of endpoint "todos"


import requests


class TodosApi:
    def __init__(self, base_url):
        self.url = f"{base_url}/todos"

    # Send GET request to get all todos
    def get_all_todos(self):
        return requests.get(self.url)
