# -*-coding:utf-8-*-
__author__ = "Jonny Hong"

from xlrd import open_workbook
import os
from os import path
import sys
import json
import re

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
        if d.find(".svn") != -1:
            continue
        d = path.join(folder_path, d)
        # 是文件夹的话 递归读取
        if path.isdir(d):
            if d.find("other") == -1:
                read_excels(d)

        else:
            read_single_excel(d)

    print("%s read complete " % folder_path)


def read_single_excel(excel_path):
    if excel_path.find(".DS_Store") != -1 or excel_path.find("~") != -1:
        return
    wb = open_workbook(excel_path, encoding_override='utf-8')
    # excel_name_with_extension ==> abc.xlsx
    # mac 平台
    if sys.platform.find("darwin") != -1:
        excel_name_with_extension = excel_path[excel_path.rfind('/') + 1:]
    else:
        excel_name_with_extension = excel_path[excel_path.rfind('\\') + 1:]

    # excel_name ==> abc
    excel_name = excel_name_with_extension[:excel_name_with_extension.rfind('.')]

    for s in wb.sheets():
        sheet_name = s.name
        re_result = re.match("^Sheet[0-9]|^_", sheet_name)
        if re_result:
            continue

        all_data_dict[sheet_name] = list()
        # single_data 单个sheet的数据结构
        single_data = all_data_dict[sheet_name]
        print(excel_name + "  --   " + sheet_name)
        # 行数
        count = 0
        # 类型列表
        property_list = {}
        # 每一行拆开
        for row in read_sheet(s):
            # 注释
            if count == 0:
                pass
            # 数据类型
            elif count == 1:
                type_list = row
                pass
            # 变量名
            elif count == 2:
                property_list = row
            # 数据
            else:
                value_list = row
                # 每一行的数据拼接结果
                pro = {}

                available = True
                for index in range(len(value_list)):
                    if property_list[index] == "" or property_list[index][0] == '_':
                        continue
                    # ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
                    ctype = s.cell(count, index).ctype
                    if ctype == 0:
                        available = False
                        break

                    if str(type_list[index]).lower() == "string":
                        if ctype == 2:
                            v = int(value_list[index])
                            v = str(v)
                        else:
                            v = str(value_list[index])
                    elif str(type_list[index]).lower() == "int":
                        v = int(value_list[index])
                    elif str(type_list[index]).lower() == "boolean":
                        if value_list[index] == 0:
                            v = False
                        elif value_list[index] == 1:
                            v = True
                        else:
                            print("bool 类型存在错误值 ")
                        pass
                    else:
                        print("不支持的表类型 %s " % str(property_list[index]))

                    pro[property_list[index]] = v
                if available:
                    single_data.append(pro)
            count += 1
        all_data_dict[sheet_name] = json.dumps(all_data_dict[sheet_name], ensure_ascii=False)
