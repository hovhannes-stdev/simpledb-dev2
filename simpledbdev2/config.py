##################################################
# Copyright (C) 2017, All rights reserved.
##################################################

from pyprelude.file_system import make_path

class Config(object):
    def __init__(self, dir):
        self._dir = dir
        self._data_dir = make_path(self._dir, "data")

    @property
    def data_dir(self): return self._data_dir