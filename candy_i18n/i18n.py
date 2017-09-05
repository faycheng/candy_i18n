# -*- coding:utf-8 -*-
import os
import gettext

from candy_i18n import errors

INTERNATIONALIZATION_DOMAIN = 'INTERNATIONALIZATION_DOMAIN'
LOCALE_DIR = 'LOCALE_DIR'
LANGUAGE = 'LANG'


def translate(msg_id, msg_plural=None, plural_number=None, domain=None, locale_dir=None, lang=None, **injected_kwargs):
    domain = domain or os.getenv(INTERNATIONALIZATION_DOMAIN, None)
    locale_dir = locale_dir or os.getenv(LOCALE_DIR, '{}/locale'.format(os.getcwd()))
    lang = lang or os.getenv(LANGUAGE, 'zh_CN')
    if domain is None:
        raise errors.DomainNotExist
    if not (os.path.exists(locale_dir) and os.path.isdir(locale_dir)):
        raise errors.LocaleDirNotExist(locale_dir)
    translation = gettext.translation(domain, locale_dir, languages=[lang])
    if msg_plural is not None and plural_number is not None:
        text = translation.ngettext(msg_id, msg_plural, plural_number)
    else:
        text = translation.gettext(msg_id)
    if injected_kwargs:
        text = text.format(**injected_kwargs)
    return text




# TODO
# lazy translate
# variable inject
# strict mode
