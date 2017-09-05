# -*- coding:utf-8 -*-
import os
import gettext

from candy_i18n import errors

INTERNATIONALIZATION_DOMAIN = os.getenv('INTERNATIONALIZATION_DOMAIN', None)
LOCALE_DIR = os.getenv('LOCALE_DIR', '{}/{locale}'.format(os.getcwd()))
LANGUAGE = os.getenv('LANG', 'zh_CN')


def translate(msg_id, msg_plural=None, plural_number=None, domain=None, localedir=None, lang=None):
    domain = domain or INTERNATIONALIZATION_DOMAIN
    localedir = localedir or LOCALE_DIR
    lang = lang or LANGUAGE
    if domain is None:
        raise errors.DomainNotExist
    if not (os.path.exists(localedir) && os.path.isdir(localedir)):
        raise errors.LocaleDirNotExist(localedir)
    if msg_plural is not None and plural_number is not None:
        return gettext.translation(domain, localedir, languages=[lang]).ngettext(msg_id, msg_plural, plural_number)
    return gettext.translation(domain, localedir, languages=[lang]).gettext(msg_id)




