#!/usr/bin/env python
# -*- coding:utf-8 -*-

#处理生成的Swig包装类并且将一些函数开放出来

import os;
import sys;

def AfterSwigCreate():
    cppInterfaceDir = "C++生成的CS接口所在目录“
    for parent, dirnames, filenames in os.walk(cppInterfaceDir):
        for filename in filenames:#输出文件信息
            fullname = "%s/%s"%(parent,filename)
            f = open(fullname,"r")
            lines = f.readlines()
            f.close()
            f = open(fullname, 'w')
            for line in lines:
               if line.startswith("  internal %s"%filename[:-3]):
                   line = "  public %s"%line[11:]
               f.write(line)
            f.close()

if __name__ == '__main__':
    AfterSwigCreate()