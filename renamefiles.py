#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def delete_folder(startpath,nowText,targetText):
for root, dirs, files in os.walk(startpath):
    for filename in files:
        # print(len(path) * '---', filename)
        if nowText in filename:
            fullpath = os.path.join(root, filename)
            target = os.path.join(root, filename.replace(nowText, targetText))
            # print(target)
            os.rename(fullpath, target)


delete_folder("your folder path", "现在有的文件名称", "要改的文件名称")



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



