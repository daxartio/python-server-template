def test_get_unknown_user(client):
    result = client.get('/api/users/d1565e7c-86a0-4130-b880-ca02b5a9d613')

    assert result.status_code == 404


def test_create_user(client):
    result = client.post(
        '/api/users', json={'full_name': 'John Doe', 'email': 'email@ex.com'}
    )

    assert result.status_code == 200
    user = result.json()
    assert user['id']
    assert user['fullName'] == 'John Doe'
    assert user['email'] == 'email@ex.com'


def test_create_existed_user():
    pass
