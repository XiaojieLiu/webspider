# -*- coding: utf-8 -*-
from urllib2 import Request, urlopen, URLError, HTTPError  
import re  
from bs4 import BeautifulSoup
import sqlite3

# 保存到本地Sqlite
def saveToSqlite(lesson_info):
    # 获取lesson_info字典中的信息
    name = lesson_info['name']
    price = lesson_info['price']
    link = lesson_info['link']
    
    #number = lesson_info['number']
    #time = lesson_info['time']
   # degree = lesson_info['degree']

    # 连接数据库并插入相应数据
    con = sqlite3.connect("lesson.db")
    cur = con.cursor()
    sql = "insert into lesson_info values ('%s', '%s','%s')" % (name, price ,link)
    cur.execute(sql)
    con.commit()

def startMain():
	old_url = 'http://faxian.smzdm.com/p'  
	page_number = 1
	while page_number <= 2:
		new_url = old_url + str(page_number)
		#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
		#headers = { 'User-Agent' : user_agent }   
		headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
		req = Request(new_url, headers = headers)   
		#req = Request(old_url)  
		response = urlopen(req)   
		the_page = response.read().decode("utf-8")  
		soup = BeautifulSoup(the_page)
		listtitle = soup.find_all("li",class_="list")
		for x in listtitle:
			if (x.find("span",class_="red").string):
				name = x.find("span",{"class": "black"}).string
				price = x.find("span",{"class": "red"}).string
				link = x.find("a").get("href")
				lesson_info = {"name": name, "price":price, "link": link}
	            	saveToSqlite(lesson_info)
		page_number = page_number + 1


if __name__ == '__main__':
		startMain()
