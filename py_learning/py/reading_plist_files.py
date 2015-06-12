#!/usr/bin/env python
#coding=utf-8

#reading_plist_files.py

import plistlib
import os
import glob

#设置一个根目录
calendar_root = os.path.expanduser('~/Library/Calendars')

#返回~/Library/Calendars/*.caldav/*.calendar和~/Library/Calendars/*.calendar匹配的所有路径
calendar_directories = (
	#搜索 ~/Library/Calendars/*.caldav/*.calendar
    glob.glob(os.path.join(calendar_root, '*.caldav', '*.calendar')) +
	#搜索 ~/Library/Calendars/*.calendar
    glob.glob(os.path.join(calendar_root, '*.calendar'))
    )

#遍历得到的路径
for dirname in calendar_directories:

	#拼接一个新路径，目的是找到Info.plist文件
    info_filename = os.path.join(dirname, 'Info.plist')

	#该文件是否存在
    if os.path.isfile(info_filename):

		#利用plistlib.readPlist函数读区Info.plist文件
        info = plistlib.readPlist(info_filename)

        #获取Info.plist中键为Checked的值，是否存在
        if info.get('Checked'):
            print info['Title']