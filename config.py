#!/usr/bin/python
# -*- coding: UTF-8 -*-

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

#json存放路径
json_path = 'data/'

#excl输出路径
excl_path = 'j2x/'