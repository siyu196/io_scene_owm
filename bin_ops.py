import struct

def readString(file):
    lb1 = struct.unpack('B', file.read(1))[0]
    lb2 = 0

    if lb1 > 128:
        lb2 = struct.unpack('B', file.read(1))[0]

    l = (lb1 % 128) + (lb2 * 128)
    if l == 0:
        return ''
    s = file.read(l)
    return s.decode('utf8')

fmtSz = {
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
  'p': 1,
  'C': 1,
  'B': 1,
  '?': 1,
  'H': 2,
  'I': 4,
  'L': 4,
  'Q': 8,
  'F': 4,
  'D': 8,
  'S': 1,
  'P': 1
} # lets not run .lower millions of times during map imports

def read(file, fmt):
    size = 0
    for char in fmt:
        if char == '<': continue
        if char in fmtSz:
            size += fmtSz[char]
        else:
            print('unrecognized fmt char %s' % (char))
    if size == 0:
        return []
    return list(struct.unpack(fmt, file.read(size)))

def readFmt(file, fmts):
    a = []
    for fmt in fmts:
        if fmt == str:
            a += [readString(file)]
        else:
            a += [read(file, fmt)]
    if len(a) == 1:
        return a[0]
    return a

def getSize(fmt):
    size = 0
    for char in fmt:
        if char == '<': continue
        if char in fmtSz:
            size += fmtSz[char]
    return size

def readFmtFlat(file, fmts):
    a = []
    for fmt in fmts:
        if fmt == str:
            a += [readString(file)]
        else:
            a += read(file, fmt)
    if len(a) == 1:
        return a[0]
    return a

def readFmtFlatArray(file, fmt, count):
    size = 0
    for char in fmt:
        if char == '<': continue
        if char in fmtSz:
            size += fmtSz[char]
        else:
            print('unrecognized fmt char %s' % (char))
    size*=count
    if fmt[0] == '<': 
        fmt="<"+(fmt[1:]*count)
    else:
        fmt*=count
    return list(struct.unpack(fmt, file.read(size)))
