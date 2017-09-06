# -*- coding:utf-8 -*-
import os
import sys
import click
import json
import pickle
import polib

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from candy_i18n.extract import extract
from candy_i18n import po


def parse_lang(ctx, param, value):
    if '.' in value:
        value = value.split('.')[0]
    return value


@click.group()
def cli():
    pass


@cli.command()
def init():
    metadata = dict(
        project_id_version=click.prompt('Project ID Version', type=str),
        report_msg_id_bugs_to=click.prompt('Report Msgid Bugs to', type=str),
        last_translator=click.prompt('Last Translator', type=str, default=os.environ.get('LOGNAME')),
        language_team=click.prompt('Language Team', type=str, default=''),
        mime_version=click.prompt('Mime Version', type=str, default='1.0'),
        content_type=click.prompt('Content Type', type=str, default='text/plain; charset=UTF-8'),
        content_transfer_encoding=click.prompt('Content Transfer Encoding', type=str, default='8bit'),
        plural_forms=click.prompt('Plural Forms', type=str, default='nplurals=2; plural=(n != 1);'),
    )

    conf_file_path = '{}/i18n.json'.format(os.getcwd())
    if not os.path.exists(conf_file_path):
        fd = open(conf_file_path, 'a+')
        fd.close()
    fd = open(conf_file_path, 'w')
    fd.write(json.dumps(metadata))
    fd.close()





if __name__ == '__main__':
    cli()