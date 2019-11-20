#!/usr/bin/env python3
import errno
import os
import stat
import sys
import time

import fuse

fuse.fuse_python_api = (0, 2)

class EbcdicFS(fuse.Fuse):
  def __init__(self, backing):
    fuse.Fuse.__init__(self)
    self.backing = backing

  def readdir(self, path, offset):
    for r in '.', '..':
      yield fuse.Direntry(r)
    for i in os.scandir(os.path.join(self.backing, path[1:])):
      print(i.name)
      yield fuse.Direntry(i.name)

  def getattr(self, path):
    return os.stat(os.path.join(self.backing, path[1:]))

  def getdir(self, path):
    return -errno.ENOSYS

  def open (self, path, flags):
    # TODO(bluecmd): This assumes the permissions of the fuse running is
    # the same as the user accessing the files, maybe not the greatest but
    # is secure by default in FUSE IIRC.
    return 0

  def read (self, path, length, offset):
    with open(os.path.join(self.backing, path[1:]), 'rb') as f:
        f.seek(offset, os.SEEK_SET)
        return f.read(length).upper()
    return r

  def write (self, path, data, offset):
    with open(os.path.join(self.backing, path[1:]), 'ab') as f:
        f.seek(offset, os.SEEK_SET)
        return f.write(data.lower())

if __name__ == '__main__':
  backing = sys.argv[1]
  fs = EbcdicFS(backing)
  fs.parse(sys.argv[2:] + ['-osubtype=ebcdic,fsname=' + backing], errex=1)
  fs.main()
