class PasswordInvalid(Exception):
    def __init__(self, message="Your entered password is invalid."):
        self.message = message
        super().__init__(self.message)