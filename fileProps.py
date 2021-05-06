import os
import hasher
from datetime import datetime


def hr_time(timeNs):
    nano = 1 / 1000000000
    return datetime.fromtimestamp(timeNs * nano).strftime('%Y-%m-%d-%H:%M:%S')


def hr_size(size):
    KB = 1024
    MB = 1024 * 1024
    GB = 1024 * 1024 * 1024
    if size < KB:
        return str(size) + " B "
    if size < MB:
        return str(size // KB) + " KB"
    if size < GB:
        return str(size // MB) + " MB"
    return str(size // GB) + " GB"


class FileProps:
    def __init__(self, path):
        osStats = os.stat(path)
        self.__timeModNs = osStats.st_mtime_ns
        self.__size = osStats.st_size

    def getStringRow(self):
        retVal = "" + str(self.__timeModNs)
        retVal += " " + str(self.__size) + "\n"
        retVal += hr_time(self.__timeModNs)
        retVal += hr_size(self.__size).rjust(7)
        retVal += "\n"
        return retVal
