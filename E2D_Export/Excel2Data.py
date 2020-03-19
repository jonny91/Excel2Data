# -*-coding:utf-8-*-
__author__ = "Jonny Hong"

from E2D import entrance
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        entrance.build()
    elif len(sys.argv) == 2:
        if int(sys.argv[1]) == 1:
            entrance.build(True, False)
        elif int(sys.argv[1]) == 2:
            entrance.build(False, True)
        else:
            entrance.build()
