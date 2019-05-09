#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import sys
import os

array = ["琼斯一家人在哪里？",
"孩子们是正从公园里出来还是正在往里走？",
"苏珊最喜欢哪种颜色？",
"萨姆把花瓶放在什么地方？",
"那听烟丝是给谁买的？",
"你怎么知道萨姆不常沏茶？",
"帕梅拉为什么无法打信？",
"安想要什么样的咖啡？",
"伯德先生喜欢什么？",
"希腊下过雪吗？",
"在英国最受欢迎的话题是什么？",
"孩子们什么时候做功课？",
"索耶先生今晚正在做什么？",
"这位女士有没有买粉笔？",
"吉米有什么好消息？",
"还有谁今天也卧床休息？",
"吉尔有没有拿到大门的钥匙？",
"约翰逊夫妇周末准备做什么？",
"哪辆车在1995年的比赛中获胜？",
"波淋在9点接电话时是如何说的？",
"为什么这位男士需要一本常用语手册？",
"这些时髦的鞋有什么毛病？",
"你认为现在是几点钟？",
"卡罗尔不准备买什么？",
"为什么卡罗尔感到失望？",
"今年萨姆去了什么地度假？",
"肯是在什么季节访问巴黎的？",
"修理工能否修复伍德先生的汽车？",
"为什么奈杰尔作不了决定？",
"谁想卖房？",
"为什么说奈杰尔很幸运？",
"为什么乔治和肯误了火车？",
"霍尔先生有没有要回他的提箱？",
"安迪需要去看医生吗？",
"收到吉米寄来的一张明信片，祖母是否显得高兴？",
"考试持续了多长时间？",
"给桑德拉的礼物是什么？",
"这位女士想要什么样的服装？",
"喝咖啡时简吃了什么？",
"弗里斯先生可以用分期付款方式购买电视机吗？",
"谁有零钱？",
"吉姆只能喝什么饮料？",
"最后一名话中的change 是什么意思？",
"谁在暗处对窃贼喊了一声？",
"为什么卡罗琳没有马上认出那位顾客？",
"那个长着络腮胡子的人是谁？",
"苏珊是一个人喝茶吗？",
"谁只有29岁？",
"安建议她的丈夫下次做什么？",
"决定如何度假有什么为难的地方？",
"卡伦.马什说她为什么想要退休？",
"你认为卡伦.马什会退休吗？",
"如果朱莉有那笔钱，她想做什么呢？",
"格雷厄姆.特纳以为他在和哪一个约翰.史密斯通话？",
"为什么母亲感到尴尬？",
"牌子上的字有什么可笑的地方？"]

def path_deeply(folderPath):
	file_count = 0
	array_index = 0
	for file in os.listdir(folderPath):
		filepath = folderPath+'/'+file
		print filepath
		if file_count > 15 and filepath.endswith('.lrc'):
			append_string(filepath, array_index)
			array_index += 1
		file_count +=1

def append_string(filepath,file_count):
	filedata = open(filepath, 'r+')
	inside_count = 0

	finput = fileinput.input(filepath,inplace=1)
	for line in finput:
		# print line
		if inside_count == 2:
			array_text = array[file_count].replace('\n', ' ')
			searchExp = line.rstrip()
			replaceExp = searchExp + '^' + array_text
			line = line.replace(searchExp,replaceExp)
		sys.stdout.write(line)
		inside_count += 1
	finput.close()

path_deeply("/Users/hilenlai/Desktop/usa_test12/")