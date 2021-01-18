# coding:utf-8

# 封装Yaml文件读取
import os

import yaml


class YamlReadFlie:
    def __init__(self, yaml_file):
        # 初始化
        if os.path.exists(yaml_file):
            self.yaml_file = yaml_file
        else:
            raise FileExistsError("文件特么不存在")
        self._data = None
        self._moreDate = None

    # 封装读取单个文件的内容
    def oneFile(self):
        if not self._data:
            with open(self.yaml_file, 'rb') as f:
                self._data = yaml.safe_load(f)
            return self._data

    # 读取Yaml文件为多个的方法
    def moreFile(self):
        if not self._moreDate:
            with open(self.yaml_file, 'rb') as f:
                self._moreDate = yaml.safe_load_all(f)
                for i in self._moreDate:
                    return i
        else:
            raise FileExistsError
