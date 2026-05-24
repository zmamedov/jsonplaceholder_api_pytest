from jsonplaceholder_api_pytest.api.response_assert import ResponseAssert


def test_get_all_posts(posts_api):
    response = posts_api.get_all_posts()
    
    (ResponseAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_basic_schema())


def test_get_all_comments(comments_api):
    response = comments_api.get_all_comments()

    (ResponseAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_basic_schema())
