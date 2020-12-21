#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import logging
from logging import handlers


#用字典保存日志级别
format_dict = {
   'FULL' : '%(asctime)s [%(threadName)s-%(process)d] %(levelname)s %(filename)s[line:%(lineno)d] - %(message)s'
}

class Logger(object):
    # 日志级别关系映射
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }

    def __init__(self, filename='ihome-face.log', level='info', when='D', backCount=10, fmt=format_dict['FULL']):
        '''
        :param filename: 日志文件名称 例如：应用日志文件名，error日志文件名
        :param level: 日志级别 可选：info、debug、警告：warning、报错：error、严重：crit
        :param when: 间隔的时间单位   # S 秒
                                    # M 分
                                    # H 小时、
                                    # D 天、
                                    # W 每星期（interval==0时代表星期一）
                                    # midnight 每天凌晨
        :param backCount: 备份文件的个数，如果超过这个个数，就会自动删除
        :param fmt: 日志输出格式模版
        '''
        self.logger = logging.getLogger(filename)

        # 设置日志格式
        format_str = logging.Formatter(fmt)

        # 设置日志级别
        self.logger.setLevel(self.level_relations.get(level))

        # 控制台输出
        streamHandler = logging.StreamHandler()

        # 设置控制台输出的格式
        streamHandler.setFormatter(format_str)

        # 往文件里写入
        #指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        timedRotatingFileHandler = handlers.TimedRotatingFileHandler(filename='./logs/{}'.format(filename), when=when, backupCount=backCount, encoding='utf-8')

        # 设置文件里写入的格式
        timedRotatingFileHandler.setFormatter(format_str)

        # 把对象加到logger里
        self.logger.addHandler(streamHandler)
        self.logger.addHandler(timedRotatingFileHandler)

    def getlog(self):
        return self.logger
