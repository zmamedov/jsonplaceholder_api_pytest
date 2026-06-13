from jsonplaceholder_api_pytest.api.assertions.response_assert import ResponseAssert


def test_get_all_posts(posts_api):
    """
    Test-case 1: Get all posts.
    Check response and validation scheme.
    """
    response = posts_api.get_all_posts()

    (ResponseAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_basic_schema())


def test_get_all_comments(comments_api):
    """
    Test-case 2: Get all comments.
    Check response and validation scheme.
    """
    response = comments_api.get_all_comments()

    (ResponseAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_basic_schema())


def test_get_all_photos(photos_api):
    """
    Test-case 3: Get all photos.
    Check response and validation scheme.
    """
    response = photos_api.get_all_photos()

    (ResponseAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_basic_schema())


def test_get_all_albums(albums_api):
    """
    Test-case 4: Get all albums.
    Check response and validation scheme.
    """
    response = albums_api.get_all_albums()

    (ResponseAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_basic_schema())


def test_get_all_todos(todos_api):
    """
    Test-case 5: Get all todos.
    Check response and validation scheme.
    """
    response = todos_api.get_all_todos()

    (ResponseAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_basic_schema())
    

def test_get_all_users(users_api):
    """
    Test-case 6: Get all users.
    Check response and validation scheme.
    """
    response = users_api.get_all_users()

    (ResponseAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_basic_schema())
    