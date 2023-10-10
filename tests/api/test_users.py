from typing import Any

from app.core.users import User


def test_get_unknown_user(client: Any) -> None:
    result = client.get('/api/users/d1565e7c-86a0-4130-b880-ca02b5a9d613')

    assert result.status_code == 404


def test_get_user(client: Any, user: User) -> None:
    result = client.get(f'/api/users/{user.id}')

    assert result.status_code == 200
    user_response = result.json()
    assert user_response['id']
    assert user_response['fullName'] == user.full_name
    assert user_response['email'] == user.email
