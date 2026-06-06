from pydantic import ValidationError
from jsonplaceholder_api_pytest.api.assertions.response_assert import ResponseAssert
from jsonplaceholder_api_pytest.schemas.pydentic_models import PostModel


class PostsAssert(ResponseAssert):
    """Custom asserts of 'Post', extended base ResponseAssert."""

    def should_match_post_schema(self):
        """Check that response matches PostModel."""
        try:
            PostModel.model_validate(self.json_data)
        except ValidationError as e:
            assert False, f"Validation error Pydantic model for post:\n{e}"
        return self

    def should_have_field_value(self, field_name: str, expected_value):
        """Check specific field value of response."""
        actual_value = self.json_data.get(field_name)
        assert actual_value == expected_value, \
            f"Expected {field_name} = {expected_value}, but got {actual_value}"
        return self
