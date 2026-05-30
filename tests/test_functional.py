from jsonplaceholder_api_pytest.api.assertions.posts_assert import PostsAssert


def test_get_single_post_by_valid_id(posts_api):
    # Validation scheme
    response = posts_api.get_single_post(post_id=1)

    (PostsAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     )
