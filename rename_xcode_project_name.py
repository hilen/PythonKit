#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import subprocess

def rename_xcode_project(currentname, targetname):
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if root.find("Pods") == -1 and root.find(".git") == -1:
                filepath = os.path.join(root, filename)
                if filepath.find('rename_xcode_project_name.py') != -1:
                    continue
                content = open(filepath).read()

                if currentname in content:
                    content = content.replace(currentname, targetname)
                    with open(filepath, 'w') as f:
                        f.write(content)

                if filename.find(currentname) != -1:
                    newfilename = filename.replace(currentname, targetname)
                    newfilepath = os.path.join(root, newfilename)
                    os.system("mv %s %s" % (filepath, newfilepath))
    for root, dirs, files in os.walk('.'):
        if root.find("Pods") == -1 and root.find(".git") == -1:
            for directory in dirs:
                if directory.find(currentname) != -1:
                    filepath = os.path.join(root, directory)
                    newdir = directory.replace(currentname, targetname)
                    newfilepath = os.path.join(root, newdir)
                    os.system("mv %s %s" % (filepath, newfilepath))

rename_xcode_project("现有的工程名称","替换的工程名称")

