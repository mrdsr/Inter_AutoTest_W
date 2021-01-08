#coding:utf-8
from selenium import webdriver

driver = webdriver.Chrome()
cookie='{bad_id6b938920-2fd5-11e7-b826-7d8f77b5695d=621f0ae1-c52a-11e8-8666-378671ab4c30; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216bd4a5efa938-0906567cb98901-37677e02-2073600-16bd4a5efaa7d7%22%2C%22%24device_id%22%3A%2216bd4a5efa938-0906567cb98901-37677e02-2073600-16bd4a5efaa7d7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lvt_7428da64c45ca777f8efb1ba6a86a14f=1563158953,1563416572,1564127109,1564642170; Hm_lpvt_7428da64c45ca777f8efb1ba6a86a14f=1564642213}'
driver.add_cookie(cookie)
driver.get("http://test3-wealth.dhibank.net/#/home")
# driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/form/div[1]/div/div/input').send_keys('admin')
cookies = driver.get_cookies()

print(cookies)
