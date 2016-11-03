##################### 递归的修改文件名称 #####################
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