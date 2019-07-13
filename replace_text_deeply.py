#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import sys
import os

# 替换文件内的内容
def replace_text_in_path_deeply(folderPath,searchExp,replaceExp):
	for file in os.listdir(folderPath):
	    for line in fileinput.input(file, inplace=1):
	        if searchExp in line:
	            line = line.replace(searchExp,replaceExp)
	        sys.stdout.write(line)

replace_text_in_path_deeply("路径","现在的字符","替换的字符")
