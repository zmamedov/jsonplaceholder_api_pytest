import os
import pytest
from dotenv import load_dotenv

from jsonplaceholder_api_pytest.api.comments_api import CommentsApi
from jsonplaceholder_api_pytest.api.posts_api import PostsApi
from jsonplaceholder_api_pytest.api.photos_api import PhotosApi
from jsonplaceholder_api_pytest.api.albums_api import AlbumsApi
from jsonplaceholder_api_pytest.api.todos_api import TodosApi
from jsonplaceholder_api_pytest.api.users_api import UsersApi


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


@pytest.fixture(scope="session")
def photos_api(base_url):
    return PhotosApi(base_url)


@pytest.fixture(scope="session")
def albums_api(base_url):
    return AlbumsApi(base_url)


@pytest.fixture(scope="session")
def todos_api(base_url):
    return TodosApi(base_url)


@pytest.fixture(scope="session")
def users_api(base_url):
    return UsersApi(base_url)
