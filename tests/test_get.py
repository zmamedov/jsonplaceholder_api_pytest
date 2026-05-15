import requests


def test_get_all_posts(base_url):
    payload = {}
    headers = {}

    response = requests.request("GET", base_url, headers=headers, data=payload)
    response_time_ms = response.elapsed.total_seconds() * 1000

    assert response.status_code == 200
    assert response_time_ms < 500


def test_get_all_comments(base_url):
    payload = {}
    headers = {}

    response = requests.request("GET", base_url, headers=headers, data=payload)
    response_time_ms = response.elapsed.total_seconds() * 1000

    assert response.status_code == 200
    assert response_time_ms < 500
