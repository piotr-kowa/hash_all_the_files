import time


class RaiTimer:
    def __init__(self, name=""):
        self.__startTime = time.time()
        self.__name = name

    def __del__(self):
        timediff = time.time() - self.__startTime
        print(f"{self.__name} tooks: {timediff:.2f}s.")
