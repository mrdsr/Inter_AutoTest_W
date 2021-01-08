#coding:utf-8
import sys
sys.path.append("/Users/shuangrongdai/PycharmProjects/indexpage/AppiumPrograme")
from util.ReadConfig import GetDate
# from mukewangprogarme.testclient import get_driver 
class find_element:
    def __init__(self,driver):
        self.driver = driver
        self.fileDate = GetDate()
    def chooies_element(self,key):
        date = self.fileDate.get_val(node_name=key)
        select_by_id = date.split(">")[0]
        select_by_loctor =  date.split(">")[1]
        if select_by_id == 'id':
            return self.driver.find_element_by_id(select_by_loctor)
        # elif select_by_id == 'class_name':
        #     return self.driver.find_element_by_id(select_by_loctor)
        #
        # print(date)
        # print(str(select_by_loctor))
        # print(select_by_id)
        return select_by_id,select_by_loctor
# a = find_element()
# print(a.chooies_element('getEmail'))
