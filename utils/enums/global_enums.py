from enum import Enum


class GlobalErrorText(Enum):
    WRONG_NAME = 'Name is not equal to expected'
    WRONG_TEXT = 'Text is not equal to expected'
    WRONG_URL = 'URL is not equal to expected'
    DOG_ERROR = 'Dog is not presented'
