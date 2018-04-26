#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlwt
import sys, os
import config

from os.path import isfile, join, splitext, basename
from collections import OrderedDict
import simplejson as json

reload(sys)
sys.setdefaultencoding('utf8')

#判断输出路径是否存在
if not os.path.exists(config.excl_path):
	#创建路径
	os.makedirs(config.excl_path)

for teble_name, table_info in config.infomap.items():
	workbook = xlwt.Workbook()
	for sh_item in table_info:
		for sh_name, json_name in sh_item.items():
			worksheet = workbook.add_sheet(sh_name)
			json_dest = '%s%s.json' % (config.json_path, json_name)
			with open(json_dest, 'r') as f:
				print '成功输出表格:%s' % (teble_name)
				jsonStr = json.load(f)
				rowCount = 2
				colCount = -1
				colTotal = 0
				colName = {}
				for json_info in jsonStr:
					for jsonKey, jsonVal in json_info.items():
						if colCount == -1:
							colName[jsonKey] = 0
							colCount = 0
							colTotal = 1
							worksheet.write(0, 0, jsonKey)
						else:
							if colName.has_key(jsonKey):
								colCount = colName[jsonKey]
							else:
								colName[jsonKey] = colTotal
								colCount = colTotal
								colTotal = colTotal + 1
								worksheet.write(0, colCount, jsonKey)
						worksheet.write(rowCount, colCount, jsonVal)
						#print jsonKey, jsonVal
					#break
					rowCount = rowCount + 1
			#break
		#break
	table_dest = '%s%s' % (config.excl_path, teble_name)
	workbook.save(table_dest)
	#break