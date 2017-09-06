# -*- coding:utf-8 -*-
import os
import polib
import arrow

from candy_i18n import errors


INTERNATIONALIZATION_DOMAIN = 'INTERNATIONALIZATION_DOMAIN'
LOCALE_DIR = 'LOCALE_DIR'
LANGUAGE = 'LANG'


def gen(entries,
        project_id_version,
        report_msg_id_bugs_to,
        last_translator,
        language_team,
        mime_version,
        content_type,
        content_transfer_encoding,
        plural_forms
        ):
    po = polib.POFile()
    po.metadata = {
        'Project-Id-Version': project_id_version,
        'Report-Msgid-Bugs-To': report_msg_id_bugs_to,
        'POT-Creation-Date': arrow.now().isoformat(),
        'Last-Translator': last_translator,
        'Language-Team': language_team,
        'MIME-Version': mime_version,
        'Content-Type': content_type,
        'Content-Transfer-Encoding': content_transfer_encoding,
        'Plural-Forms': plural_forms
    }
    for entry in entries:
        po.append(entry)
    return po


def init_locale_dir():
    pass


def save(po, domain=None, locale_dir=None, lang=None):
    domain = domain or os.getenv(INTERNATIONALIZATION_DOMAIN, None)
    locale_dir = locale_dir or os.getenv(LOCALE_DIR, '{}/locale'.format(os.getcwd()))
    lang = lang or os.getenv(LANGUAGE, 'zh_CN')
    if domain is None:
        raise errors.DomainNotExist
    if not (os.path.exists(locale_dir) and os.path.isdir(locale_dir)):
        raise errors.LocaleDirNotExist(locale_dir)
    po.save('{locale}/{lang}/LC_MESSAGES/{domain}.po'.format(locale_dir, lang, domain))


def compile(po, domain=None, locale_dir=None, lang=None):
    domain = domain or os.getenv(INTERNATIONALIZATION_DOMAIN, None)
    locale_dir = locale_dir or os.getenv(LOCALE_DIR, '{}/locale'.format(os.getcwd()))
    lang = lang or os.getenv(LANGUAGE, 'zh_CN')
    if domain is None:
        raise errors.DomainNotExist
    if not (os.path.exists(locale_dir) and os.path.isdir(locale_dir)):
        raise errors.LocaleDirNotExist(locale_dir)
    po.save_as_mofile('{locale}/{lang}/LC_MESSAGES/{domain}.mo'.format(locale_dir, lang, domain))


