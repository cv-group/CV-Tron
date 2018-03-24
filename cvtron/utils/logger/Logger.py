# coding:utf-8
from logbook import Logger, StreamHandler

class Logger(object):
    def __init__(self, level):
        self.level = level

    def info(self, message):
        print(message)

    def warn(self, message):
        print(message)

    def error(self, message):
        print(message)
