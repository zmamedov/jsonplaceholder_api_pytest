import requests

url = "https://jsonplaceholder.typicode.com/posts"


def test_get_all_posts():
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response_time_ms = response.elapsed.total_seconds() * 1000

    assert response.status_code == 200
    assert response_time_ms < 500
