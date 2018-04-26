#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlwt
import sys, os

from os.path import isfile, join, splitext, basename
from collections import OrderedDict
import simplejson as json

reload(sys)
sys.setdefaultencoding('utf8')

#表格结构定义
infomap = {
	'H_活动配置.xlsx' : [
		{"ActList":"ActListData"},
		{"jamboree":"sevenCarnivalData"}
	],
	"J_竞技场配置.xlsx" : [
		{"buy": "arenaBuy"}
	]
}

for teble_name, table_info in infomap.items():
	workbook = xlwt.Workbook()
	for sh_item in table_info:
		for sh_name, json_name in sh_item.items():
			worksheet = workbook.add_sheet(sh_name)
			json_dest = 'data/%s.json' % (json_name)
			with open(json_dest, 'r') as f:
				print teble_name, sh_name
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
	table_dest = 'j2x/%s' % (teble_name)
	workbook.save(table_dest)
	#break