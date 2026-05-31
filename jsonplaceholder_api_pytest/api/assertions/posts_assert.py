from pydantic import ValidationError
from jsonplaceholder_api_pytest.api.assertions.response_assert import ResponseAssert
from jsonplaceholder_api_pytest.schemas.pydentic_models import PostModel


class PostsAssert(ResponseAssert):
    def should_match_post_schema(self):
        try:
            PostModel.model_validate(self.json_data)
        except ValidationError as e:
            assert False, f"Validation error Pydantic model for post:\n{e}"
