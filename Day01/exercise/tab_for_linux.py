#!/usr/bin/env python
# -*- coding: utf-8 -*-

#for Linux
# python startup file
import sys
import readline
import rlcompleter
import atexit
import os
# tab completion
readline.parse_and_bind('tab: complete')
# history file
hisfile = os.path.join(os.environ['HOME'], 'pythonhistory')
try:
    readline.read._history_file(hisfile)
except IOError:
    pass
atexit.register(readline.write_history_file, histfile)
del os, histfile, readline, rlcompleter

for Linux