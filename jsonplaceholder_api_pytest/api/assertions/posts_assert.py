from pydantic import TypeAdapter, ValidationError
from jsonplaceholder_api_pytest.api.assertions.response_assert import ResponseAssert
from jsonplaceholder_api_pytest.schemas.pydentic_models import PostModel


class PostsAssert(ResponseAssert):
    """Custom asserts of 'Post', extended base ResponseAssert."""

    def should_match_post_schema(self):
        """Check that response matches PostModel."""
        try:
            PostModel.model_validate(self.json_data)
        except ValidationError as e:
            raise AssertionError(f"Validation error Pydantic model for post!\n{e}") from e

        return self

    def should_have_field_value(self, field_name: str, expected_value):
        """Check specific field value of response."""
        actual_value = self.json_data.get(field_name)
        assert actual_value == expected_value, \
            f"Expected {field_name} = {expected_value}, but got {actual_value}"

        return self

    def all_posts_should_belong_to_user(self, user_id: int):
        """Check that all posts belong to specific user."""
        for post in self.json_data:
            assert post["userId"] == user_id, \
                f"Post {post['id']} belongs to user {post['userId']} instead of {user_id}"

        return self

    def should_match_posts_list_schema(self):
        """Check that response is a list and each element matches PostModel."""
        try:
            # Parsed list of comments.
            # TypeAdapter is required here to validate a top-level JSON array (List)
            # since BaseModel.model_validate() only accepts top-level dictionaries.
            TypeAdapter(list[PostModel]).validate_python(self.json_data)
        except ValidationError as e:
            raise AssertionError(f"Validation error Pydantic model for list posts!\n{e}") from e

        return self
