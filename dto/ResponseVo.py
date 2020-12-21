#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-


class ResponseVo(object):
    def __init__(self, data, code, success, msg):
        self.data = data
        self.code = code
        self.success = success
        self.msg = msg

    def clear(self):
        self.data.clear()
        self.code = None
        self.success = None
        self.msg = None