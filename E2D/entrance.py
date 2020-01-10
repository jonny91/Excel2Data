# -*-coding:utf-8-*-
__author__ = "Jonny Hong"

from E2D import recorder, config_reader, excel_reader
import json


class AppEntrance:
    @staticmethod
    def read_config():
        config_reader.read("config/config.xml")

    @staticmethod
    def read_excel():
        excel_reader.read_excels(config_reader.resPath)

    @staticmethod
    def record_data():
        recorder.record(config_reader.outputPath, json.dumps(excel_reader.all_data_dict))

    @staticmethod
    def write_single_json():
        recorder.record_to_json(config_reader.outputJsonDirPath, excel_reader.all_data_dict)


def build(is_build_data=True, is_build_json=True):
    entrance = AppEntrance()
    entrance.read_config()
    entrance.read_excel()
    if is_build_data:
        entrance.record_data()
    if is_build_json:
        entrance.write_single_json()


if __name__ == '__main__':
    build()
