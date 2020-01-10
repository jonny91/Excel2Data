# -*-coding:utf-8-*-
__author__ = "Jonny Hong"

from xml.dom.minidom import parse
import xml.dom.minidom

resPath = ""
outputPath = ""
outputJsonDirPath = ""


def read(path):
    global resPath
    global outputPath
    global outputJsonDirPath
    dom_tree = xml.dom.minidom.parse(path)
    root = dom_tree.documentElement
    resPath = root.getElementsByTagName("res")[0].childNodes[0].data
    outputPath = root.getElementsByTagName("output")[0].childNodes[0].data
    outputJsonDirPath = root.getElementsByTagName("outputJson")[0].childNodes[0].data
