import random
import string

class Shortner:
    token_size = 5
    
    def __init__(self, token_size=None):
        self.token_size = token_size if token_size is not None else 5

    def generate_token(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(self.token_size))