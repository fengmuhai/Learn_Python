# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

def crawler(page):
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        content = response.read()   
        #.decode('utf-8')#用了decode后出现编码问题
        # 正则表达式，'.*?'表示匹配任意长度字符串，'(.*?)'表示要获取的那个tuple元素
        pattern = re.compile('<div.*?author clearfix">.*?<a.*?>.*?<h2>(.*?)</h2>.*?</a>.*?<div.*?'+
                          'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
        #pattern = re.compile('<div.*?content">(.*?)<!--(.*?)-->.*?</div>',re.S)
    
        items = re.findall(pattern,content)
        for item in items:
            haveImg = re.search("img",item[3])
            if not haveImg:
                #item[0].decode('utf-8')
                #item[1].decode('utf-8')
                text = item[1].replace('<br/>','\n')
                print item[0],text,item[2],item[4]
                print ''
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

x = 1
for x in range(4):
	crawler(x)