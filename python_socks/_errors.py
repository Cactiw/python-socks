class ProxyError(IOError):
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code


class ProxyTimeoutError(IOError):
    pass


class ProxyConnectionError(IOError):
    pass
