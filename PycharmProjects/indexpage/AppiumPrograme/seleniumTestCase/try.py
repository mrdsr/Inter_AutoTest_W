#!/usr/bin/python
# -*- coding: UTF-8 -*-
try:
    ph = open("try.txt","w")
    ph.write('呆-try')
except:
    print("无法写入文件")
else:
    ph.write("else-呆")
    ph.close()