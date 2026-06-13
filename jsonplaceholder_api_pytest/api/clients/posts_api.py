import requests
import random
from faker import Faker


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

    def create_post(self, payload: dict):
        """
        POST /posts
        Creates a new post with the specified payload.

        :param payload: The data of the post.
        :return: A requests.Response object with the newly created post data.
        """
        return requests.post(self.url, json=payload)
    
    def update_post(self, post_id: int, payload: dict):
        """
        PUT /posts/{id}
        Updates an existing post with the specified payload.

        :param post_id: The unique identifier of the post (e.g., 1).
        :param payload: The data to update the post with.
        :return: A requests.Response object with the updated post data.
        """
        return requests.put(f"{self.url}/{post_id}", json=payload)

    def partial_update_post(self, post_id: int, payload: dict):
        """
        PATCH /posts/{id}
        Partial updating of an existing post with the specified payload.

        :param post_id: The unique identifier of the post (e.g., 1).
        :param payload: The data to update the post with.
        :return: A requests.Response object with the updated post data.
        """
        return requests.patch(f"{self.url}/{post_id}", json=payload)
    
    def delete_post(self, post_id: int):
        """
        DELETE /posts/{id}
        Deletes an existing post by its unique ID.

        :param post_id: The unique identifier of the post (e.g., 1).
        :return: An empty requests.Response object.
        """
        return requests.delete(f"{self.url}/{post_id}")

    def get_single_post(self, post_id: int):
        """
        GET /posts/{id}
        Retrieves detailed information for a specific post by its unique ID.

        :param post_id: The unique identifier of the post (e.g., 1).
        :return: A requests.Response object with post data or an error payload.
        """
        return requests.get(f"{self.url}/{post_id}")

    def get_nested_comments(self, post_id: int):
        """
        GET /posts/{id}/comments
        Retrieves all comments nested under a specific post.

        :param post_id: The unique identifier of the post (e.g., 1).
        :return: A requests.Response object containing an array of comments.
        """
        return requests.get(f"{self.url}/{post_id}/comments")

    def get_all_posts_by_user(self, user_id: int):
        """
        GET /posts?userId={id}
        Retrieves all posts created by a specific user.

        :param user_id: The unique identifier of the user (e.g., 1).
        :return: A requests.Response object containing an array of posts.
        """
        return requests.get(f"{self.url}?userId={user_id}")

    def get_posts_paginated(self, page: int, limit: int):
        """
        GET /posts?_page={page}&_limit={limit}
        Retrieves a paginated list of posts.

        :param page: The page number to retrieve (e.g., 1).
        :param limit: The number of posts to return per page (e.g., 10).
        :return: A requests.Response object containing an array of posts.
        """
        return requests.get(f"{self.url}?_page={page}&_limit={limit}")

    @staticmethod
    def generate_random_post_payload():
        """
        Generates a random post payload for testing purposes.

        :return: A dictionary containing the post data.
        """
        fake = Faker()

        return {
            "title": fake.sentence(nb_words=4),
            "body": fake.paragraph(nb_sentences=3),
            "userId": random.randint(1, 10)
        }
    
    def get_posts_by_custom_params(self, params: dict):
        """
        GET /posts?param={param_values}
        Retrieves posts by custom query-parameters.

        :param params: A dictionary containing the query-parameters.
        :return: A requests.Response object containing an array of posts or an error payload.
        """
        return requests.get(self.url, params=params)
