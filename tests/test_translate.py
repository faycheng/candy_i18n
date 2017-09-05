# -*- coding:utf-8 -*-

import os
import pytest

from candy_i18n import errors
from candy_i18n.i18n import translate

from .faker import *


def test_single_translate():
    pass


def test_plural_translate():
    pass


def test_domain_and_locale(monkeypatch):
    import gettext

    class Translation(object):
        def __init__(self, *args, **kwargs):
            pass

        def gettext(self, *args, **kwargs):
            return None

    msg_id = random_lower_string()
    with pytest.raises(errors.DomainNotExist):
        translate(msg_id)

    domain = random_lower_string()
    with pytest.raises(errors.LocaleDirNotExist):
        translate(msg_id, domain=domain)

    os.environ['INTERNATIONALIZATION_DOMAIN'] = domain
    with pytest.raises(errors.LocaleDirNotExist):
        translate(msg_id)

    locale_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
    monkeypatch.setattr(gettext, 'translation', Translation)
    translate(msg_id, locale_dir=locale_dir)

