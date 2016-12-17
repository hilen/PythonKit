#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os import walk
import os
import fileinput, sys

def replace_text_in_path_deeply(startpath,nowText,targetText):
for file in os.listdir(startpath):
	for line in fileinput.input(file, inplace=True):
		line = line.replace(targetText, nowText)
		sys.stdout.write(line)

replace_text_in_path_deeply("路径","现在的字符","替换的字符")