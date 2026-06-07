from pydantic import TypeAdapter, ValidationError
from jsonplaceholder_api_pytest.api.assertions.response_assert import ResponseAssert
from jsonplaceholder_api_pytest.schemas.pydentic_models import CommentModel


class CommentsAssert(ResponseAssert):
    """Custom asserts of 'Comment', extended base ResponseAssert."""

    def should_match_comments_list_schema(self):
        """Check that response is a list and each element matches CommentModel."""
        try:
            # Parsed list of comments.
            # TypeAdapter is required here to validate a top-level JSON array (List)
            # since BaseModel.model_validate() only accepts top-level dictionaries.
            TypeAdapter(list[CommentModel]).validate_python(self.json_data)
        except ValidationError as e:
            raise AssertionError(f"Validation error Pydantic model for list comments!\n{e}") from e

        return self

    def all_comments_should_belong_to_post(self, expected_post_id: int):
        """Check that all comments belong to post with id = expected_post_id."""
        for comment in self.json_data:
            assert comment['postId'] == expected_post_id, \
                f"Comment belongs to post {comment['postId']} instead of {expected_post_id}"

        return self
