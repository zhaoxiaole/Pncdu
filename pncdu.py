#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-12 21:01:43
# @Author  : zhaoxiaole (zhaoxiaole@sogou-inc.com)
from __future__ import division
import os
import json
import sys
def useage():
	msg = '''使用帮助：
    * -t -显示大文件top n，默认top10
    * -d - 指定路径，默认为当前路径
    * -e - 排除的文件关键字
    * -h/--help - 帮助信息
    * -v/--version - 版本信息
示例：
    pncdu -t 5 -d /tmp -e .sh
    '''
	return msg

file_size={}
def ncdu_file(d,file_list):
	if d[-1]=='/':
		flag=''
	else:
		flag='/'
	for x in file_list[1:]:
		if isinstance(x, dict):
			if x.get('excluded'):
				continue
			file_size['%s%s%s' % (d,flag,x.get('name'))]=x.get('dsize')
		if isinstance(x, list):
			ncdu_file('%s%s%s' % (d,flag,x[0].get('name')),x)

def get_top_file(cdir,exclude,top):
	if not cdir:
		cdir=os.getcwd()
	cmd='ncdu %s -o /tmp/ncdu_temp %s >/dev/null 2>&1' % (cdir,exclude)
	flag=os.system(cmd)
	if flag!=0:
		print 'please install ncdu and try again!'
		exit(1)
	with open("/tmp/ncdu_temp",'r') as load_f:
		load_dict = json.load(load_f)
	ncdu_file(cdir,load_dict[3])
	result=sorted(file_size.items(), key=lambda e:e[1], reverse=True)
	if int(top)<=len(result):
		result=result[0:int(top)]
	for x in result:
		if x[1]>=1024 and x[1]<1048576:
			size='%.2fK' % (x[1]/1024)
		elif x[1]>=1048576 and x[1]<1073741824:
			size='%.2fM' % (x[1]/1024/1024)
		elif x[1]>=1073741824:
			size='%.2fG' % (x[1]/1024/1024/1024)
		else:
			size='%sB' % x[1]
		print '%s %s %s' % (result.index(x)+1,x[0],size)
	input_op(result)
def input_op(result):
	val=raw_input('input your operation(q=quit|delfile n-top):\n')
	if val in ['q','exit','quit']:
		exit(0)
	input_list=str(val).split(' ')
	del_list=[]
	for arg in input_list:
		if arg=='delfile':
			did=input_list.index(arg)+1
			if len(input_list)>did:
				delfile=input_list[did]
				#print delfile
				for x in delfile.split(','):
					if '-' in x:
						tmp=x.split('-')
						del_list=del_list+range(int(tmp[0])-1,int(tmp[-1]))
					else:
						del_list.append(int(x)-1)
				#print del_list
			else:
				input_op(result)
	if del_list:
		if max(del_list)+1 > len(result):
			print 'your chose file num out of top list!'
			input_op(result)
		print 'you will delete these %s files:' % len(del_list)
		for x in del_list:
			print '%s %s' % (del_list.index(x)+1,result[x][0])
		rm_input=raw_input('rm those %s files?Y/n:' % len(del_list))
		if rm_input=='Y':
			pass
			for x in del_list:
				print 'rm -f %s' % result[x][0]
				os.system('rm -f %s' % x)
	input_op(result)
exclude, cdir, top='','',10
if len(sys.argv)==1:
	get_top_file(cdir,exclude,top)
if len(sys.argv) % 2 == 0:
	if sys.argv[1] in ['-h','--help']:
		print useage()
		exit(0)
	if sys.argv[1] in ['-v','--version']:
		print 'pncdu 0.0.1 dependence:python 2.X && ncdu >= 1.9'
		exit(0)
	print useage()
	exit(1)
else:
	for arg in sys.argv:
		if arg=='-e':
			eid=sys.argv.index(arg)+1
			exclude='--exclude %s' % sys.argv[eid]
		if arg=='-d':
			did=sys.argv.index(arg)+1
			cdir=sys.argv[did]
		if arg=='-t':
			tid=sys.argv.index(arg)+1
			top=sys.argv[tid]
	if not exclude and not cdir and top==10:
		print useage()
		exit(1)
get_top_file(cdir,exclude,top)