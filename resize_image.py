#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import humanfriendly
from PIL import Image
import io

def get_files_by_file_size(dirname, reverse=False):
    """ Return list of file paths in directory sorted by file size """

    # Get list of files
    filepaths = []
    for basename in os.listdir(dirname):
        filename = os.path.join(dirname, basename)
        if os.path.isfile(filename):
            filepaths.append(filename)

    # Re-populate list with filename, size tuples
    for i in xrange(len(filepaths)):
        filepaths[i] = (filepaths[i], os.path.getsize(filepaths[i]))

    # Sort list by file size
    # If reverse=True sort from largest to smallest
    # If reverse=False sort from smallest to largest
    filepaths.sort(key=lambda filename: filename[1], reverse=reverse)

    # Re-populate list with just filenames
    for i in xrange(len(filepaths)):
        filepaths[i] = filepaths[i][0]

    return filepaths


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        # print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in sorted(files, key=lambda f: os.path.getsize(root + os.sep + f)):
            if f!="__init__" and f!=".DS_Store":
                size = os.path.getsize(root + os.sep + f)
                humanread = humanfriendly.format_size(size)
                path = '{}{}'.format(startpath, f, humanread)
                with open(path, "rb") as f:
                    img = Image.open(path)
                    orig_width = img.size[0] #原始图片宽度
                    orig_height = img.size[1] #原始图片高度
                    baseLine = 500
                    new_height = 0
                    new_width = 0
                    if orig_width == orig_height:
                        new_height = baseLine
                        new_width = baseLine
                    elif orig_width > orig_height: # 如果宽度 > 高度
                        new_height = baseLine
                        new_width = int(orig_width*new_height/orig_height)
                    else: # 如果高度 > 宽度
                        new_width = baseLine
                        new_height = int(new_width*orig_height/orig_width)
                    print("路径:{}   原图图片宽高:{}_{}   订正图片宽高:{}_{}".format(path,orig_width,orig_height,new_width,new_height))

                    #准备名字
                    replace_p1 = (str(orig_width) + '-' + str(orig_height))
                    replace_n2 = (str(new_width) + '-' + str(new_height))
                    #重命名新的路径
                    new_path = path.replace(replace_p1,replace_n2)
                    img = img.resize((new_width,new_height), Image.ANTIALIAS)
                    img.save(new_path)

list_files("/Users/hilenlai/Desktop/tttttttttt/周杰伦-专辑封面/")
