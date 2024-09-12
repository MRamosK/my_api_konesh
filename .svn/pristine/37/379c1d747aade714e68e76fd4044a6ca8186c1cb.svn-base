def test_index(client) -> None:
    """
    Test the index route.

    Args:
        client: The test client used to make requests.
    
    Returns:
        None
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Flask' in response.data
