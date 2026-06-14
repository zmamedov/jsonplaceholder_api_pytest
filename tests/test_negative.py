from jsonplaceholder_api_pytest.api.assertions.posts_assert import PostsAssert


def test_get_non_existent_post(posts_api):
    """
    Test-case 15: Get non-existent post (404).
    Check that requesting an ID that does not exist returns HTTP 404 Not Found.
    """
    invalid_post_id = 2222
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
    invalid_params = {"userId": "invalid_value"}
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
    broken_payload = '{"title": "Broken JSON, "body": "Missing quote"}'
    response = posts_api.create_post(payload=broken_payload)

    (PostsAssert(response)
     .status_code_should_be(500)
     .should_not_contain_stack_trace())


def test_post_request_with_empty_json_body(posts_api):
    """
    Test-case 18: POST request with an empty JSON body.
    Check that post with id = 101 is created.
    """
    response = posts_api.create_post(payload={})

    (PostsAssert(response)
     .status_code_should_be(201)
     .content_type_should_be_json()
     .should_have_field_value("id", 101))
