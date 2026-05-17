from jsonplaceholder_api_pytest.api.posts_api import PostsApi
from jsonplaceholder_api_pytest.api.posts_assert import PostsAssert


def test_get_all_posts(base_url):
    posts_api = PostsApi(base_url)
    response = posts_api.get_all_posts()
    (PostsAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_basic_schema())

# def test_get_all_comments(base_url):
#     payload = {}
#     headers = {}

#     response = requests.request("GET", base_url, headers=headers, data=payload)
#     response_time_ms = response.elapsed.total_seconds() * 1000

#     assert response.status_code == 200
#     assert response_time_ms < 500
