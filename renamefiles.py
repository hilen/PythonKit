#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import sys
import os

# 修改文件夹名字
def rename_folder(startpath,nowText,targetText):
for root, dirs, files in os.walk(startpath):
    for filename in files:
        # print(len(path) * '---', filename)
        if nowText in filename:
            fullpath = os.path.join(root, filename)
            target = os.path.join(root, filename.replace(nowText, targetText))
            # print(target)
            os.rename(fullpath, target)

# rename_folder("your folder path", "现在有的文件名称", "要改的文件名称")


# 替换文件内的内容
def recursion_file_and_replace(startpath,nowText,targetText):
for root, dirs, files in os.walk(startpath):
    for filename in files:
        # print(len(path) * '---', filename)
        if nowText in filename:
            fullpath = os.path.join(root, filename)
            # Read in the file
			filedata = None
			with open(fullpath, 'r') as file :
				filedata = file.read()

			# Replace the target string
			filedata = filedata.replace(nowText, targetText)

			# Write the file out again
			with open(fullpath, 'w') as file:
				file.write(filedata)


def rename_file_in_dir(path,searchExp,replaceExp):
    if not os.path.isdir(path):
        newname = path.replace(searchExp, replaceExp)
        if newname != path:
            os.rename(path, newname)
    else:
        for item in os.listdir(path):
            listdir((path + '/' + item) if path != '/' else '/' + item,searchExp,replaceExp)



if __name__ == '__main__':
    rename_file_in_dir('/Users/hilenlai/Desktop/baiduyun/周杰伦/','（公众号：音乐耳朵）','')



