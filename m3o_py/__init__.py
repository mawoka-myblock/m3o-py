class GeneralException(Exception):
    def __getattr__(self, item) -> str | int:
        return self.__dict__.get(item)

    def __init__(self, data: dict):
        self.__dict__.update(data)

    code: int
    Detail: str
    Id: str
    Status: str


class UnknownError(Exception):
    pass
