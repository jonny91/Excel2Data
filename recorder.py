# -*-coding:utf-8-*-
__author__ = "Jonny Hong"

import gzip


def record(file_path, content):
    with open(file_path, "wb+") as f:
        content = str(content).replace("\'", "\"")
        content = gzip.compress(bytes(content, "utf-8"))
        f.write(content)