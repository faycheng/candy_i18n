# -*- coding:utf-8 -*-


class BaseError(BaseException):
    ERROR_MSG_TEMPLATE = 'i18n domain not exist'


class DomainNotExist(BaseError):
    ERROR_MSG_TEMPLATE = 'i18n domain not exist'

    def __init__(self):
        self.message = self.ERROR_MSG_TEMPLATE.format()
        super(DomainNotExist, self).__init__(self.message)


class LocaleDirNotExist(BaseError):
    ERROR_MSG_TEMPLATE = 'locale dir {} not exist'

    def __init__(self, locale_dir):
        self.message = self.ERROR_MSG_TEMPLATE.format(locale_dir)
        super(LocaleDirNotExist, self).__init__(self.message)
