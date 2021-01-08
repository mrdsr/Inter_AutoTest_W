#coding:utf-8

import configparser
#
# parser = configparser.ConfigParser()
#
# parser.read('/Users/shuangrongdai/PycharmProjects/indexpage/AppiumPrograme/config/Logcal_element.ini')
#
# a = parser.get('Loging-element','getEmail')
# print(a)
#

class GetDate:
    def __init__(self,filePath = None):
        self.parser = configparser.ConfigParser()
        if filePath == None:
            self.filePath = '/Users/shuangrongdai/PycharmProjects/indexpage/AppiumPrograme/config/Logcal_element.ini'
            self.parser.read(self.filePath)
        else:
            self.parser.read(filePath)

    def get_val(self, node=None, node_name=None):
        if node == None:
            node = 'Loging-element'
            local_element = self.parser.get(node, node_name)
        else:
            local_element = self.parser.get(node, node_name)
        return local_element

