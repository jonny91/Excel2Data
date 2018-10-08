# -*-coding:utf-8-*-
__author__ = "Jonny Hong"

import config_reader
import excel_reader


class AppEntrance:
    @staticmethod
    def read_config():
        config_reader.read("config/config.xml")

    @staticmethod
    def read_excel():
        excel_reader.read_excels(config_reader.resPath)
        pass


if __name__ == '__main__':
    entrance = AppEntrance()
    entrance.read_config()
    entrance.read_excel()
