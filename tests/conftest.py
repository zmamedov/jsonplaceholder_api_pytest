import os
import pytest
from dotenv import load_dotenv

from jsonplaceholder_api_pytest.api.comments_api import CommentsApi
from jsonplaceholder_api_pytest.api.posts_api import PostsApi

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")


@pytest.fixture(scope="session")
def posts_api(base_url):
    return PostsApi(base_url)


@pytest.fixture(scope="session")
def comments_api(base_url):
    return CommentsApi(base_url)
