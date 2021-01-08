from timebox import settings


class TokenAuth:
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["Authorization"] = "Token " + self.token
        r.headers["User-Agent"] = settings.USER_AGENT
        return r
