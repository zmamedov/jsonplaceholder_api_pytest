# File with checks of response

from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonplaceholder_api_pytest.schemas.json_schemas import SMOKE_ARRAY_SCHEMA


class ResponseAssert:
    def __init__(self, response):
        self.response = response
        self.json_data = self.response.json()

    def status_code_should_be(self, status_code):
        """Check status code"""
        assert self.response.status_code == status_code, \
            f"Expected status code {status_code}, actual {self.response.status_code}"
        
        return self

    def content_type_should_be_json(self):
        """Check that header 'Content-Type' = 'application/json'"""
        content_type = self.response.headers.get("Content-Type", "")
        assert "application/json" in content_type, f"Expected JSON, but content type {content_type}"
        
        return self
    
    def x_total_count_should_be_present(self):
        """Check that header 'X-Total-Count' is present"""
        x_total_count = self.response.headers.get("X-Total-Count", "")
        assert x_total_count, "Header 'X-Total-Count' is not present"
        
        return self        
    
    def should_match_basic_schema(self):
        """Check that response matches basic schema"""
        try:
            validate(self.response.json(), SMOKE_ARRAY_SCHEMA)
        except ValidationError as e:
            assert False, f"JSON does not match schema: {e.message}"

        return self

    def should_have_length(self, expected_length: int):
        """Check count of objects in the array"""
        actual_length = len(self.json_data)
        assert actual_length == expected_length, f"Expected {expected_length} objects in array, but got {actual_length}"

        return self
