from pydantic import BaseModel, Field, ConfigDict


class PostModel(BaseModel):
    """Validation scheme for one post with endpoint /posts/{id}."""

    model_config = ConfigDict(strict=True)

    user_id: int = Field(alias='userId')
    id: int
    title: str
    body: str


class CommentModel(BaseModel):
    """Validation scheme for one comment with endpoint /posts/{id}/comments."""

    model_config = ConfigDict(strict=True)

    post_id: int = Field(alias='postId')
    id: int
    name: str
    email: str
    body: str
