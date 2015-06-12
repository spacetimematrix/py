#coding=utf-8

#utility.py

import os

__author__= 'LEE'


def CopyFolder(sourceDir, targetDir):
	for f in os.listdir(sourceDir):
	 	sourceFile = os.path.join(sourceDir, f)
	 	targetFile = os.path.join(targetDir, f)

	 	if os.path.isfile(sourceFile):
	 		if not os.path.exists(targetDir):
	 			os.makedirs(targetDir)
	 		open(targetFile, "wb").write(open(sourceFile, "rb").read())

	 	if os.path.isdir(sourceFile):
	 		CopyFolder(sourceFile, targetFile)

	return


def CleanFolder(path):
	if not os.path.exists(path):
	 	return

	for root, dirs, files in os.walk(path, topdown=False):
		for f in files:
			os.remove(os.path.join(root, f))
		for folder in dirs:
			os.rmdir(os.path.join(root, folder))
	return