# -*-coding:utf-8-*-
__author__ = "Jonny Hong"

import gzip


def record(file_path, content):
    with open(file_path, "wb+") as f:
        content = gzip.compress(bytes(content, "utf-8"))
        f.write(content)

        print("dat文件写入完成 => %s " % file_path)
