# -*- coding:utf-8 -*-


# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import random
import uuid
import string


def random_lower_string(length=8):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def random_upper_string(length=8):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))


def random_number_string(length=8):
    return ''.join(random.choice(string.digits) for _ in range(length))


def random_string(length=8):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def random_uuid():
    return str(uuid.uuid4())


def random_enum(enum_list=None):
    assert enum_list is not None and isinstance(enum_list, list)
    return random.choice(enum_list)


def random_number(min, max):
    return random.randint(min, max)
