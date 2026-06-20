from jsonplaceholder_api_pytest.api.assertions.posts_assert import PostsAssert
from jsonplaceholder_api_pytest.data.post_data import PostData


def test_get_non_existent_post(posts_api):
    """
    Test-case 15: Get non-existent post (404).
    Check that requesting an ID that does not exist returns HTTP 404 Not Found.
    """
    invalid_post_id = PostData.non_existent_post_id()
    response = posts_api.get_single_post(post_id=invalid_post_id)

    (PostsAssert(response)
     .status_code_should_be(404)
     .should_have_empty_body())


def test_get_posts_by_invalid_query_parameter(posts_api):
    """
    Test-case 16: Get posts by invalid query parameter.
    Note: JSONPlaceholder treats unknown params by ignoring them or returning empty results.
    Check that it doesn't crash (returns 200).
    """
    invalid_params = PostData.invalid_query_params()
    response = posts_api.get_posts_by_custom_params(params=invalid_params)

    (PostsAssert(response)
     .status_code_should_be(200)
     .should_be_empty_list())


def test_post_request_with_invalid_data(posts_api):
    """
    Test-case 17: POST request with invalid data.
    Check how the server handles bad requests.
    Note: The server crashes with a 500 Internal Server Error and
    returns a raw text stack trace instead of a proper 400 Bad Request JSON response.
    """
    broken_payload = PostData.malformed_json_string()
    response = posts_api.create_post(payload=broken_payload)

    (PostsAssert(response)
     .status_code_should_be(500)
     .should_not_contain_stack_trace())


def test_post_request_with_empty_json_body(posts_api):
    """
    Test-case 18: POST request with an empty JSON body.
    Check that post with id = 101 is created.
    """
    empty_payload = PostData.empty_json_payload()
    response = posts_api.create_post(empty_payload)

    (PostsAssert(response)
     .status_code_should_be(201)
     .content_type_should_be_json()
     .should_have_field_value("id", 101))
