class ClientError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)
