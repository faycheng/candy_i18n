# -*- coding:utf-8 -*-

import os
import pytest
import gettext

from candy_i18n import errors
from candy_i18n.i18n import translate

from .faker import *


def test_single_translate(monkeypatch):
    msg_id = random_lower_string()
    msg_str = random_lower_string()

    class Translation(object):
        def __init__(self, *args, **kwargs):
            pass

        def gettext(self, *args, **kwargs):
            return msg_str

    monkeypatch.setattr(gettext, 'translation', Translation)
    domain = random_lower_string()
    locale_dir = os.path.abspath(os.path.dirname(__file__))
    assert translate(msg_id, domain=domain, locale_dir=locale_dir) == msg_str


def test_plural_translate(monkeypatch):
    msg_id = random_lower_string()
    msg_plural = random_lower_string()
    plural_number = random_number(1, 100)
    msg_str = random_lower_string()

    class Translation(object):
        def __init__(self, *args, **kwargs):
            pass

        def ngettext(self, *args, **kwargs):
            return msg_str

    monkeypatch.setattr(gettext, 'translation', Translation)
    domain = random_lower_string()
    locale_dir = os.path.abspath(os.path.dirname(__file__))
    assert translate(msg_id, msg_plural=msg_plural, plural_number=plural_number, domain=domain, locale_dir=locale_dir) == msg_str


def test_domain_and_locale(monkeypatch):

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


def test_translate_with_injected_kwargs(monkeypatch):
    msg_id = random_lower_string()
    msg_str = random_lower_string() + "{data}"
    data = random_lower_string()

    class Translation(object):
        def __init__(self, *args, **kwargs):
            pass

        def gettext(self, *args, **kwargs):
            return msg_str

    monkeypatch.setattr(gettext, 'translation', Translation)
    domain = random_lower_string()
    locale_dir = os.path.abspath(os.path.dirname(__file__))
    assert translate(msg_id, domain=domain, locale_dir=locale_dir, data=data) == msg_str.format(data=data)

