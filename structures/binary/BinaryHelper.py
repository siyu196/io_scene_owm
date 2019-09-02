import io
import os
import struct


def open_stream(filename):
    stream = None
    with open(filename, 'rb') as f:
        stream = io.BytesIO(f.read())
    return stream


def normalize_path(path):
    return os.path.normpath(path.replace('\\', os.path.sep).replace('/', os.path.sep))


def read_string(file):
    size_byte1 = struct.unpack('B', file.read(1))[0]
    size_byte2 = 0

    if size_byte1 > 128:
        size_byte2 = struct.unpack('B', file.read(1))[0]

    length = (size_byte1 % 128) + (size_byte2 * 128)
    if length == 0:
        return ''
    return file.read(length).decode('utf8')


fmt_size = {
  'c': 1,
  'b': 1,
  '?': 1,
  'h': 2,
  'i': 4,
  'l': 4,
  'q': 8,
  'f': 4,
  'd': 8,
  's': 1,
  'p': 1
}


def read(file, fmt):
    size = 0
    for char in fmt:
        if char == '<':
            continue
        if char.lower() in fmt_size:
            size += fmt_size[char.lower()]
        else:
            print('unrecognized fmt char %s' % (char))
    if size == 0:
        return []
    return list(struct.unpack(fmt, file.read(size)))


def read_fmt(file, fmts):
    a = []
    for fmt in fmts:
        if fmt == str:
            a += [read_string(file)]
        else:
            a += [read(file, fmt)]
    if len(a) == 1:
        return a[0]
    return a


def read_fmt_flat(file, fmts):
    a = []
    for fmt in fmts:
        if fmt == str:
            a += [read_string(file)]
        else:
            a += read(file, fmt)
    if len(a) == 1:
        return a[0]
    return a
