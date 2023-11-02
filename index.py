import re
from typing import Callable
from cuid2 import cuid_wrapper


class Id:
    cuid_generator: Callable[[], str] = cuid_wrapper()

    @staticmethod
    def create_id():
        return Id.cuid_generator()

    @staticmethod
    def is_valid_id(_id):
        if _id is None or \
                not isinstance(_id, str) or \
                not 2 <= len(_id) <= 32:
            return False
        return bool(re.match('^[0-9a-z]+$', _id))
