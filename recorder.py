# -*-coding:utf-8-*-
__author__ = "Jonny Hong"

import os
import gzip


def record(file_path, content):
    file_parent = os.path.dirname(file_path)
    if not os.path.exists(file_parent):
        os.mkdir(file_parent)
    with open(file_path, "wb+") as f:
        content = gzip.compress(bytes(content, "utf-8"))
        f.write(content)

        print("dat file record complete => %s " % file_path)
