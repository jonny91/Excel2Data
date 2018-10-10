# -*-coding:utf-8-*-
__author__ = "Jonny Hong"

from xlrd import open_workbook
import os
from os import path
import sys
import json

all_data_dict = dict()


# 创建一个用于读取sheet的生成器,依次生成每行数据,row_count 用于指定读取多少行, col_count 指定用于读取多少列
def read_sheet(s, row_count=-1, col_count=-1):
    # Sheet 有多少行
    n_rows = s.nrows
    # Sheet 有多少列
    n_cols = s.ncols

    # 没有传值进来
    if row_count < 0:
        row_count = n_rows

    if col_count < 0:
        col_count = n_cols

    row_index = 0
    while row_index < row_count:
        yield [s.cell(row_index, col).value for col in range(col_count)]
        row_index += 1


def read_excels(folder_path):
    os.chdir(folder_path)
    dirs = os.listdir(folder_path)
    for d in dirs:
        d = path.join(folder_path, d)
        # 是文件夹的话 递归读取
        if path.isdir(d):
            read_excels(d)
        else:
            read_single_excel(d)

    print("数据 : %s " % all_data_dict)


def read_single_excel(excel_path):
    wb = open_workbook(excel_path)
    # excel_name_with_extension ==> abc.xlsx
    # windows平台
    if sys.platform.find("win") != -1:
        excel_name_with_extension = excel_path[excel_path.rfind('\\') + 1:]
    else:
        excel_name_with_extension = excel_path[excel_path.rfind('/') + 1:]

    # excel_name ==> abc
    excel_name = excel_name_with_extension[:excel_name_with_extension.rfind('.')]
    all_data_dict[excel_name] = list()
    single_data = all_data_dict[excel_name]
    count = 0
    property_list = {}
    for s in wb.sheets():
        for row in read_sheet(s):
            # 注释
            if count == 0:
                pass
            # 数据类型
            elif count == 1:
                pass
            # 变量名
            elif count == 2:
                property_list = row
            # 数据
            else:
                value_list = row
                # 每一行的数据拼接结果
                pro = {}
                for index in range(len(value_list)):
                    pro[property_list[index]] = value_list[index]
                single_data.append(pro)
            count += 1
