import uuid
from typing import Any, Callable

from app_core.auth import Token
from app_core.users import User


def test_get_unknown_user(
    client: Any, create_token: Callable[[uuid.UUID], Token]
) -> None:
    token = create_token(uuid.UUID("d1565e7c-86a0-4130-b880-ca02b5a9d613")).access_token

    result = client.get(
        "/api/users/d1565e7c-86a0-4130-b880-ca02b5a9d613",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert result.status_code == 404


def test_get_user(
    client: Any, user: User, create_token: Callable[[uuid.UUID], Token]
) -> None:
    token = create_token(user.id).access_token

    result = client.get(
        f"/api/users/{user.id}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert result.status_code == 200
    user_response = result.json()
    assert user_response["id"] == str(user.id)
    assert user_response["fullName"] == user.full_name
    assert user_response["email"] == user.email


def test_get_user_me(
    client: Any, user: User, create_token: Callable[[uuid.UUID], Token]
) -> None:
    token = create_token(user.id).access_token

    result = client.get(
        "/api/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert result.status_code == 200
    user_response = result.json()
    assert user_response["id"] == str(user.id)
    assert user_response["fullName"] == user.full_name
    assert user_response["email"] == user.email
