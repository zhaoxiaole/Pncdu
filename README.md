# Pncdu
pncdu�ǻ���ncdu����ʵ�ֿ��ٻ�ȡ·����top n�Ĵ��ļ��������Լ���չʾ���ļ��б����ѡ��ɾ�����ļ�

ϵͳ����

����ϵͳ��Linux Python >= 2.6 ncdu >= 1.9

ע�⣺�����Ȱ�װncdu���ߣ�centos����ʹ��yum install -y ncdu��װ�������߰�װ������ٶ�

����ȫ���������
cp pncdu /usr/bin/pncdu

ʹ�÷���
--------------------------------
| args |  note |
|--------|-------|
|-h/--help|ʹ�ð���|
|-v/--version|�汾��Ϣ|
|-t|���ļ�top n|
|-d|·��|
|-e|�ų�������ļ��ؼ���|

ʹ�þ�����

�ҳ�/tmpĿ¼�´��ļ���ǰ������ų�.sh�ļ�

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
