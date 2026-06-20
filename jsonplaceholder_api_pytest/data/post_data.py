import random
from faker import Faker


class PostData:
    """
    Post data Factory layer for API testing.
    Isolates mock data generation and state definitions from test logic.
    """

    @staticmethod
    def generate_random_post_payload():
        """Generates a random post payload for testing purposes."""
        fake = Faker()
        return {
            "title": fake.sentence(nb_words=4),
            "body": fake.paragraph(nb_sentences=3),
            "userId": random.randint(1, 10)
        }

    @staticmethod
    def full_update_payload(post_id):
        """Generates all fields required for a full resource overwrite (PUT)."""
        fake = Faker()
        return {
            "id": post_id,
            "title": f"Test PUT: {fake.sentence(nb_words=3)}",
            "body": fake.paragraph(nb_sentences=2),
            "userId": random.randint(1, 10)
        }

    @staticmethod
    def partial_update_payload():
        """Generates only specific fields for a partial resource modification (PATCH)."""
        fake = Faker()
        return {
            "body": f"Test PATCH: {fake.sentence(nb_words=5)}"
        }

    @staticmethod
    def existing_post_id():
        """Returns ID of existing post."""
        return 2

    @staticmethod
    def non_existent_post_id():
        """Returns a non-existent ID guaranteed to trigger a 404 error."""
        return 2222

    @staticmethod
    def invalid_query_params():
        """Returns invalid query parameters."""
        return {"userId": "invalid_value"}

    @staticmethod
    def malformed_json_string():
        """Returns a broken JSON string missing a closing quote to test syntax handling."""
        return '{"title": "Broken JSON, "body": "Missing quote"}'

    @staticmethod
    def empty_json_payload():
        """Returns an empty JSON object to verify default schema constraints."""
        return {}
