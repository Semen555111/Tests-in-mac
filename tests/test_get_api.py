def test_api_get_request(api_request_context):
    response = api_request_context.get("https://jsonplaceholder.typicode.com/users")
    assert response.status == 200
    json_data = response.json()
    for user in json_data:
        assert "email" in user
        assert len(user["email"]) >0 
