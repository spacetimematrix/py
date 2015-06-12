#!/usr/bin/env python
#coding=utf-8

#writing_plist_files.py

import plistlib
import datetime
import tempfile
import os

#如果你的应用程序需要一个临时文件来存储数据，但不需要同其他程序共享，
#那么用TemporaryFile函数创建临时文件是最好的选择。其他的应用程序是无法找到或打开这个文件的，
#因为它并没有引用文件系统表。用这个函数创建的临时文件，关闭后会自动删除。
import tempfile

d = { 'an_int':2,
      'a_bool':False,
      'the_float':5.9,
      'simple_string':'This string has no special characters.',
      'xml_string':'<element attr="value">This string includes XML markup &nbsp;</element>',
      'nested_list':['a', 'b', 'c'],
      'nested_dict':{ 'key':'value' },
      'timestamp':datetime.datetime.now(),
      }

#如果临时文件会被多个进程或主机使用，那么建立一个有名字的文件是最简单的方法。
#这就是NamedTemporaryFile要做的，可以使用name属性访问它的名字
output_file = tempfile.NamedTemporaryFile()
try:
    plistlib.writePlist(d, output_file)
    output_file.seek(0)
    print output_file.read()
    print output_file.name
finally:
    #单引号和双引号的区别，单引号'Let/'s go'
    print "close"
    output_file.close()

print 'Exists after close:', os.path.exists(output_file.name)