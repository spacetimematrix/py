#!/usr/bin/env python
#coding=utf-8

#binary_property_data.py

import plistlib

d = { 'binary_data':plistlib.Data('somestring you plistl Data file. \0'),}

print plistlib.writePlistToString(d)


DATA = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>binary_data</key>
	<data>
	c29tZXN0cmluZyB5b3UgcGxpc3RsIERhdGEgZmlsZS4gAA==
	</data>
</dict>
</plist>
"""

m = plistlib.readPlistFromString(DATA)

#输出'somestring you plistl Data file. \x00'
print repr(m['binary_data'].data)

#输出somestring you plistl Data file.
print m['binary_data'].data