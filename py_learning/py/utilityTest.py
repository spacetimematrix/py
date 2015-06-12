#!/usr/bin/env python
#coding=utf-8

__author__= 'LEE'

import utility
import os

#获取当前脚本所在的路径
curPath = os.getcwd()

def main():
	#当前脚本执行路径的上级目录的source文件夹
 	sourceDir = os.path.join(curPath, "..", "source")
 	#当前脚本执行路径的上级目录的target文件夹
 	targetDir = os.path.join(curPath, "..", "target")

 	if os.path.exists(targetDir):
 		utility.CleanFolder(targetDir)

 	#执行拷贝
	utility.CopyFolder(sourceDir, targetDir)

	#需要重命名的文件
	srcName = os.path.join(targetDir, "22.rtf")

	#命名后的的文件
	desName = os.path.join(targetDir, "44.rtf")

	#命名后的的文件
	os.rename(srcName, desName)


if __name__ == '__main__':
    main()