from string import ascii_lowercase
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if len(username) < 3:
            raise UserInputError("The username has to be at least three characters long")

        if len(password) < 8:
            raise UserInputError("The password has to be at least eight characters long")
        
        all_letters = True
        for c in password.lower():
            if c not in ascii_lowercase:
                all_letters = False
                break
        
        if all_letters:
            raise UserInputError("The password has to have at least one character that is not a letter")

        if password != password_confirmation:
            raise UserInputError("The given passwords don't match")

        if self._user_repository.find_by_username(username):
            raise UserInputError("The username is already in use")

user_service = UserService()
