# -*- coding:utf-8 -*-

import os
import sys
import random
import string

dn = os.path.dirname
sys.path.append(dn(dn(dn(os.path.abspath(__file__)))))

from candy_i18n.i18n import install

os.environ['INTERNATIONALIZATION_DOMAIN'] = 'candy_i18n.simple_translation'
install('_')


class PathError(BaseException):
    ERR_MSG = _('Path({}) is invalid')

    def __init__(self, path):
        self.message = self.ERR_MSG.format(path)
        super(PathError, self).__init__(self.message)


if __name__ == '__main__':
    fake_path = ''.join([random.choice(string.ascii_letters) for _ in range(6)])
    print(_('Starting simple translation demo...'))
    if not os.path.exists(fake_path):
        raise PathError(fake_path)
