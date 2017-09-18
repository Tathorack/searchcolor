class SearchColorException(Exception):
    pass


class OversizeException(SearchColorException):
    pass


class ZeroResultsException(SearchColorException):
    pass
