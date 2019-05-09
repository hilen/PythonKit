#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import sys
import os

def delete_top4_lines(folderPath):
	for file in os.listdir(folderPath):
		if file.endswith('.lrc'):
			path = folderPath+'/'+file
			with open(path, 'r') as fin:
			    data = fin.read().splitlines(True)
			with open(path, 'w') as fout:
			    fout.writelines(data[4:])


delete_top4_lines("路径")