# -*- coding:utf-8 -*-
import tokenize


class EXTRACT_STATUS(object):
    WAITING = 'WAITING'
    SCANNING_LOP = 'SCANNING_LOP'
    SCANNING_ROP = 'SCANNING_ROP'
    SCANNING_STR = 'SCANNING_STR'


def extract(file, keywords=None):
    keywords = keywords or ['_']
    status = EXTRACT_STATUS.WAITING
    extracted_msgs = []
    with open(file, 'rb') as fd:
        extracted_msg = None
        for token_type, token_str, (source_row, source_col), (err_row, err_col), line in tokenize.tokenize(fd.readline):
            if status == EXTRACT_STATUS.WAITING:
                if token_type == tokenize.NAME and token_str in keywords:
                    status = EXTRACT_STATUS.SCANNING_LOP
                continue
            if status == EXTRACT_STATUS.SCANNING_LOP:
                if token_type == tokenize.OP and token_str == '(':
                    status = EXTRACT_STATUS.SCANNING_STR
                    continue
                status = EXTRACT_STATUS.WAITING
                continue
            if status == EXTRACT_STATUS.SCANNING_STR:
                if token_type == tokenize.STRING and token_str:
                    extracted_msg = token_str
                    status = EXTRACT_STATUS.SCANNING_ROP
                    continue
                status = EXTRACT_STATUS.WAITING
                continue
            if status == EXTRACT_STATUS.SCANNING_ROP:
                if token_type == tokenize.OP and token_str == ')':
                    extracted_msgs.append(extracted_msg)
                status = EXTRACT_STATUS.WAITING
                continue
    return extracted_msgs


