import pytest
@pytest.fixture
def api_request_context(playwright):
    request = playwright.request.new_context(
        extra_http_headers={"Accept": "application/json"}
    )
    yield request
    request.dispose()