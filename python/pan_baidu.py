#!/usr/bin/env python
# -*- coding: utf-8 -*-

#����һ�����ڵ�½�ٶȵĽű�
 
import urllib2,requests,time,re
 
def login_baidu(name,password):
    #������ҳ����ȡcookie
    s.get('http://pan.baidu.com')
    s.get('https://passport.baidu.com/v2/api/?login')
    #��ȡtoken ֵ
    cook = s.get("https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=true")
    data = cook.text
    token = re.findall(r"bdPass.api.params.login_token='(.*?)'",data)[0]
 
    #�������ͷ��
    headers = {
    'Host': 'passport.baidu.com',
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0",
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://pan.baidu.com/',
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    s.get("https://passport.baidu.com/v2/api/?login",headers=headers)
 
    #��һ��post����
    payload={
     'staticpage':'http://pan.baidu.com/res/static/thirdparty/pass_v3_jump.html',
            'charset':'utf-8',
            'token':token,
            'tpl':'netdisk',
            'apiver':'v3',
            'tt': '1392637410384',
            'codestring' : '',
            'safeflg' : '0',
            'u' :'http://pan.baidu.com/',
            'isPhone' : 'false',
            'quick_user'  : '0',
            'loginmerge': 'true',
            'logintype' : 'basicLogin',
            'username': name,
            'password': password,
            'verifycode':'',
            'mem_pass':'on',
            'ppui_logintime' : '49586',
            'callback':'parent.bd__pcbs__hksq59'
    }
    #��һ��post����ȡ��֤���ַ
    login = s.post("https://passport.baidu.com/v2/api/?login", data=payload,headers=headers,verify=True)
    get_code = re.findall(r'codeString=(.*?)&userName',login.text)[0]
    print 'codeString: ', get_code
 
    verifycode = ''
   #  #��ȡ��֤��
   #  code = s.get("https://passport.baidu.com/cgi-bin/genimage",params=get_code,stream=True)
   #  path = "/home/zhuliting/code.jpg"  #�������޸�·��
   #  if code.status_code == 200:
   #      with open(path, 'wb') as f:
   #          for chunk in code.iter_content():
   #              f.write(chunk)
 
   #  #������֤��
   #  while not verifycode:
   #      verifycode = raw_input("��������֤��:")
   #      print verifycode
 
    #����post����
    payload={
            'staticpage' : 'http://pan.baidu.com/res/static/thirdparty/pass_v3_jump.html',
            'charset' : 'utf-8',
            'token' : token,
            'tpl':'netdisk',
            'apiver':'v3',
            'tt': '1392637410384',
            'codestring' : get_code,
            'safeflg' : '0',
            'u' :'http://pan.baidu.com/',
            'isPhone' : 'false',
            'quick_user'  : '0',
            'loginmerge': 'true',
            'logintype' : 'basicLogin',
            'username': name,
            'password': password,
            'verifycode':verifycode,
            #'mem_pass':'on',
            'ppui_logintime' : '49586',
            'callback':'parent.bd__pcbs__hksq59'
        }
 
    login2 = s.post("https://passport.baidu.com/v2/api/?login", data=payload,headers=headers,verify=True)
 
    #�ж��Ƿ��¼�ɹ�,�ж�cookie���Ƿ���'BDUSS'
    if 'BDUSS' in s.cookies:
        print "login success"
    else:
        print "login failed"
 
if __name__ == '__main__':
 
    #����һ���Ự�����������󱣴�cookie
    s = requests.Session()
    name = 'me27163'
    password = 'zhulitingok'
    login_baidu(name,password)
 
