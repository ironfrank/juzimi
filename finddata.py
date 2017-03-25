# -*- coding: utf-8 -*-
import sys#, os
import time

for i in range(10):
    time.sleep(.5)
    sys.stdout.write("""\033[1;32;40ma :[%3d], b:[%3d], c:[%3d]\r""" % (i, i, i))
    sys.stdout.flush()