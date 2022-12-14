import re
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if len(username) < 3:
            raise UserInputError("Too short username, use at least 3 characters")

        if len(password) < 8:
            raise UserInputError("Too short password, use at least 8 characters")

        if re.match("^[a-zA-Z]+$", password):
            raise UserInputError("Password has to include other characters in addition to letters")

        # lisätarkastus, varmistetaan että käyttäjätunnus koostuu merkeistä a-z tehtävänannon mukaisesti
        if not re.match("^[a-z]+$", username):
            raise UserInputError("Username can only have lower case letters")
