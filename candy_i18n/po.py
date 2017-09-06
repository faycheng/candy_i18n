# -*- coding:utf-8 -*-
import polib
import arrow


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


def save():
    pass


