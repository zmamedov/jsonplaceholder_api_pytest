# File with checks of response

from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonplaceholder_api_pytest.schemas.json_schemas import SMOKE_ARRAY_SCHEMA


class ResponseAssert:
    def __init__(self, response):
        self.response = response

    def status_code_should_be(self, status_code):
        assert self.response.status_code == status_code, \
            f"Expected status code {status_code}, actual {self.response.status_code}"
        
        return self

    def content_type_should_be_json(self):
        content_type = self.response.headers.get("Content-Type", "")
        assert "application/json" in content_type, f"Expected JSON, but content type {content_type}"
        
        return self
    
    def should_match_basic_schema(self):
        try:
            validate(self.response.json(), SMOKE_ARRAY_SCHEMA)
        except ValidationError as e:
            assert False, f"JSON does not match schema: {e.message}"

        return self
