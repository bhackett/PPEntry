import os


class Person:
    """Person defines two usernames and passwords to sign in to FamilySearch"""

    def __init__(self, per: int):
        params = list(os.environ['FS_PARAMS'].split(","))  # Get user parameters from OS Environment
        self.per = per
        self.name: str = params[per]
        self.username: str = params[per+2]
        self.password: str = params[per+4]
        self.fn: str = params[per+6]

    def get_person(self):
        """Return the stored per value as an integer"""
        return self.per

    def get_name(self):
        """Return the stored name value as a string"""
        return self.name

    def get_username(self):
        """Return the stored username as a string"""
        return self.username

    def get_password(self):
        """Return the stored password as a string"""
        return self.password

    def get_fn(self):
        """Return the stored filename that contains the FS IDs as a string"""
        return self.fn

    def get_params(self):
        """Return the stored per, username, password, filename as space separated string"""
        return f"Person({self.per}, '{self.name}', '{self.username}', '{self.password}', '{self.fn}')"

    def __repr__(self):
        return f"Person('{self.name}', {self.username}', {self.password}, '{self.fn}')"
