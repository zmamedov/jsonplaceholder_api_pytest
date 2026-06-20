from jsonplaceholder_api_pytest.api.assertions.comments_assert import CommentsAssert
from jsonplaceholder_api_pytest.api.assertions.posts_assert import PostsAssert
from jsonplaceholder_api_pytest.data.post_data import PostData


def test_get_single_post_by_valid_id(posts_api):
    """
    Test-case 7: Get a single post by valid ID.
    Check response, Pydantic model and field values.
    """
    target_post_id = PostData.existing_post_id()
    response = posts_api.get_single_post(post_id=target_post_id)

    (PostsAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_post_schema()
     .should_have_field_value("id", target_post_id))


def test_get_nested_resources_of_post(posts_api):
    """
    Test-case 8: Get nested resources of a post.
    Check that comments belong to the specific post, they are valid list and count = 5.
    """
    target_post_id = 1
    expected_comments_count = 5
    response = posts_api.get_nested_comments(post_id=target_post_id)

    (CommentsAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_comments_list_schema()
     .all_comments_should_belong_to_post(target_post_id)
     .should_have_length(expected_comments_count))


def test_get_all_posts_by_user_id(posts_api):
    """
    Test-case 9: Get all posts by user ID.
    Check that posts belong to the specific user and they are valid list.
    """
    target_user_id = 10
    response = posts_api.get_all_posts_by_user(user_id=target_user_id)

    (PostsAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_posts_list_schema()
     .all_posts_should_belong_to_user(target_user_id))


def test_get_posts_with_pagination(posts_api):
    """
    Test-case 10: Get posts with pagination.
    Check that response contains posts from a specific pagination page, they are valid list and count = 5.
    """
    target_page = 2
    limit = 5
    response = posts_api.get_posts_paginated(page=target_page, limit=limit)

    (PostsAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_posts_list_schema()
     .should_have_length(limit)
     .x_total_count_should_be_present())


def test_create_new_post(posts_api):
    """
    Test-case 11: Create new post.
    Check that a post is successfully created and it is correct.
    """
    payload = PostData.generate_random_post_payload()
    response = posts_api.create_post(payload=payload)

    (PostsAssert(response)
     .status_code_should_be(201)
     .content_type_should_be_json()
     .should_match_post_schema()
     .should_have_field_value("title", payload["title"])
     .should_have_field_value("body", payload["body"])
     .should_have_field_value("userId", payload["userId"]))


def test_update_post(posts_api):
    """
    Test-case 12: Update post.
    Check that specified data in a post is updated.
    """
    target_post_id = PostData.existing_post_id()
    payload = PostData.full_update_payload(post_id=target_post_id)
    response = posts_api.update_post(post_id=target_post_id, payload=payload)

    (PostsAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_post_schema()
     .should_have_field_value("title", payload["title"])
     .should_have_field_value("body", payload["body"])
     .should_have_field_value("userId", payload["userId"])
     .should_have_field_value("id", target_post_id))


def test_update_body_of_post_patch(posts_api):
    """
    Test-case 13: Update body of post (PATCH).
    Check that a post's body is changed, other fields aren't changed.
    """
    target_post_id = PostData.existing_post_id()
    payload = PostData.partial_update_payload()
    response = posts_api.partial_update_post(post_id=target_post_id, payload=payload)

    (PostsAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_post_schema()
     .should_have_field_value("body", payload["body"])
     .should_have_field_value("id", target_post_id)
     .field_should_not_be_empty("title")
     .field_should_not_be_empty("userId"))


def test_delete_post(posts_api):
    """
    Test-case 14: Delete post.
    Check that a post is successfully deleted.
    """
    target_post_id = PostData.existing_post_id()
    response = posts_api.delete_post(post_id=target_post_id)

    (PostsAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_have_empty_body())
