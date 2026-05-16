from jsonplaceholder-api-pytest.api.posts_api import PostsApi


def test_get_all_posts(base_url):
    posts_api = PostsApi(base_url)
    response = posts_api.get_all_posts()

    assert response.status_code == 200
    # response_time_ms = response.elapsed.total_seconds() * 1000
    # assert response_time_ms < 500
    # assert "application/json" in response.headers["Content-Type"]

    # # Проверка структуры данных ответа
    # posts = response.json()
    # assert isinstance(posts, list)
    # assert len(posts) > 0

    # # Проверка обязательных полей на примере первого поста
    # first_post = posts
    # assert "id" in first_post
    # assert "title" in first_post
    # assert isinstance(first_post["id"], int)


# def test_get_all_comments(base_url):
#     payload = {}
#     headers = {}

#     response = requests.request("GET", base_url, headers=headers, data=payload)
#     response_time_ms = response.elapsed.total_seconds() * 1000

#     assert response.status_code == 200
#     assert response_time_ms < 500
