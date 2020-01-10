# -*-coding:utf-8-*-
__author__ = "Jonny Hong"

import os
import gzip
import sys


def record(file_path, content):
    if not os.path.isabs(file_path):
        file_path = os.path.join(os.path.dirname(sys.argv[0]), file_path)

    file_parent = os.path.dirname(file_path)
    if not os.path.exists(file_parent):
        os.mkdir(file_parent)
    with open(file_path, "wb+") as f:
        content = gzip.compress(bytes(content, "utf-8"))
        f.write(content)

        print("dat file record complete => %s " % file_path)


def record_to_json(dir_path, json_data):
    if not os.path.isabs(dir_path):
        dir_path = os.path.join(os.path.dirname(sys.argv[0]), dir_path)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    json_data_dic = dict(json_data)
    for (key, data) in json_data_dic.items():
        file_path = os.path.join(dir_path, key + ".json")

        with open(file_path, 'w+', encoding='utf-8') as f:
            f.write(data)
    print("json write complete => %s " % dir_path)
