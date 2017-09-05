# -*- coding:utf-8 -*-
import os
import gettext

from candy_i18n import errors

INTERNATIONALIZATION_DOMAIN = 'INTERNATIONALIZATION_DOMAIN'
LOCALE_DIR = 'LOCALE_DIR'
LANGUAGE = 'LANG'


def translate(msg_id, msg_plural=None, plural_number=None, domain=None, locale_dir=None, lang=None):
    domain = domain or os.getenv(INTERNATIONALIZATION_DOMAIN, None)
    locale_dir = locale_dir or os.getenv(LOCALE_DIR, '{}/locale'.format(os.getcwd()))
    lang = lang or os.getenv(LANGUAGE, 'zh_CN')
    if domain is None:
        raise errors.DomainNotExist
    if not (os.path.exists(locale_dir) and os.path.isdir(locale_dir)):
        raise errors.LocaleDirNotExist(locale_dir)
    if msg_plural is not None and plural_number is not None:
        return gettext.translation(domain, locale_dir, languages=[lang]).ngettext(msg_id, msg_plural, plural_number)
    return gettext.translation(domain, locale_dir, languages=[lang]).gettext(msg_id)




# TODO
# lazy translate
# variable inject
# strict mode
