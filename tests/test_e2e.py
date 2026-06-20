from jsonplaceholder_api_pytest.api.assertions.posts_assert import PostsAssert
from jsonplaceholder_api_pytest.data.post_data import PostData


def test_post_lifecycle_e2e(posts_api):
    """
    Test-case 19: Full End-to-End lifecycle of a post (CRUD).

    Steps:
    1. Create a new post (POST) and verify it.
    2. Read the post (GET).
    3. Fully update the created post (PUT) and verify changes.
    4. Delete the post (DELETE) and verify the empty response state.
    """

    # Step 1
    payload = PostData.generate_random_post_payload()
    response = posts_api.create_post(payload=payload)

    (PostsAssert(response)
     .status_code_should_be(201)
     .content_type_should_be_json()
     .should_match_post_schema()
     .should_have_field_value("title", payload["title"]))
    
    created_id = response.json().get("id")

    # JSONPlaceholder doesn't save id 101 in DB.
    test_id = 1 if created_id == 101 else created_id

    # Step 2
    response = posts_api.get_single_post(post_id=test_id)

    (PostsAssert(response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_post_schema()
     .should_have_field_value("id", test_id))
    
    # Step 3
    update_payload = PostData.partial_update_payload()
    update_response = posts_api.partial_update_post(post_id=test_id, payload=update_payload)

    (PostsAssert(update_response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_match_post_schema()
     .should_have_field_value("id", test_id)
     .should_have_field_value("body", update_payload["body"]))
    
    # Step 4
    delete_response = posts_api.delete_post(post_id=test_id)

    (PostsAssert(delete_response)
     .status_code_should_be(200)
     .content_type_should_be_json()
     .should_have_empty_body())
