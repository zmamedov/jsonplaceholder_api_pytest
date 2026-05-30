from jsonplaceholder_api_pytest.api.assertions.response_assert import ResponseAssert


class PostsAssert(ResponseAssert):
    def should_match_post_schema(self):
        pass