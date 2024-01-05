import tracemalloc

def hud(num):
    prefixes = ["k", "M", "G", "T", "P", "E", "Z", "Y"]
    prefix = ""
    while num >= 1024:
        num /= 1024
        prefix = prefixes.pop(0)
    return f"{num:.2f} {prefix}B"




class RaiMemoryMeasure:
    def __init__(self, name=""):
         self.__name = name
         tracemalloc.start()



    def __del__(self):
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{self.__name} tooks: {hud(peak)} of memory.")

