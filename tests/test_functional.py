from jsonplaceholder_api_pytest.api.assertions.comments_assert import CommentsAssert
from jsonplaceholder_api_pytest.api.assertions.posts_assert import PostsAssert


def test_get_single_post_by_valid_id(posts_api):
    """
    Test-case 7: Get a single post by valid ID.
    Check response, Pydantic model and field values.
    """
    response = posts_api.get_single_post(post_id=1)

    (PostsAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_post_schema()
     .should_have_field_value("id", 1)
     .should_have_field_value("userId", 1))


def test_get_nested_resources_of_post(posts_api):
    """
    Test-case 8: Get nested resources of a post.
    Check comments belong to the specific post, they are valid list and count = 5.
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
