import io
import hashlib
import zlib


def md5sum(src, length=io.DEFAULT_BUFFER_SIZE):
    md5 = hashlib.md5()
    with io.open(src, mode="rb") as fd:
        for chunk in iter(lambda: fd.read(length), b''):
            md5.update(chunk)
    return md5.hexdigest()


def crc32(src, length=io.DEFAULT_BUFFER_SIZE):
    crc_sum = 0
    with io.open(src, mode="rb") as fd:
        for chunk in iter(lambda: fd.read(length), b''):
            crc_sum = zlib.crc32(chunk, crc_sum)
    return format(crc_sum, "x").zfill(8)
