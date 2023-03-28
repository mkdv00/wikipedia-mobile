from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str
    fake_username: str
    fake_password: str


user = User(
    username='test_user_mkdv00',
    password='Qwerty_123',
    fake_username='Mark_L_Powell',
    fake_password='8hBXgbkiJxWl'
)
