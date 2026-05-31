from pydantic import BaseModel, Field, ConfigDict


class PostModel(BaseModel):
    """Validation scheme for one post with endpoint /posts/{id}."""

    model_config = ConfigDict(strict=True)

    user_id: int = Field(alias='userId')
    id: int
    title: str
    body: str
