# Pncdu
pncdu是基于ncdu工具实现快速获取路径下top n的大文件，根据自己的展示的文件列表快速选择删除的文件

系统需求

操作系统：Linux Python >= 2.6 ncdu >= 1.9

注意：必须先安装ncdu工具，centos可以使用yum install -y ncdu安装，或离线安装，详见百度

配置全局命令方法：
cp pncdu /usr/bin/pncdu

使用方法
--------------------------------
| args |  note |
|--------|-------|
|-h/--help|使用帮助|
|-v/--version|版本信息|
|-t|大文件top n|
|-d|路径|
|-e|排除在外的文件关键字|

使用举例：

找出/tmp目录下大文件的前五个，排除.sh文件

pncdu -t 5 -d /tmp -e .sh

[root@localhost opt]# pncdu -t 5 -d /tmp -e .sh

1 /tmp/yum_save_tx.2018-03-22.22-35.la2cIL.yumtx 4.00K

2 /tmp/yum_save_tx.2018-03-22.22-33.1_s5gi.yumtx 4.00K

3 /tmp/yum_save_tx.2018-03-22.22-34.pudkbA.yumtx 4.00K

4 /tmp/ks-script-aTJtZ6 4.00K

5 /tmp/yum.log NoneB

input your operation(q=quit|delfile n-top):

delfile 1,3,4-5

you will delete these 4 files:

1 /tmp/yum_save_tx.2018-03-22.22-35.la2cIL.yumtx

2 /tmp/yum_save_tx.2018-03-22.22-34.pudkbA.yumtx

3 /tmp/ks-script-aTJtZ6

4 /tmp/yum.log

rm those 4 files?Y/n:Y

rm -f /tmp/yum_save_tx.2018-03-22.22-35.la2cIL.yumtx

rm -f /tmp/yum_save_tx.2018-03-22.22-34.pudkbA.yumtx

rm -f /tmp/ks-script-aTJtZ6

rm -f /tmp/yum.log

input your operation(q=quit|delfile n-top):

q

[root@localhost opt]# 
