# -*- coding: utf-8 -*-
from urllib2 import Request, urlopen, URLError, HTTPError  
import re  
from bs4 import BeautifulSoup

old_url = 'http://faxian.smzdm.com/p1'  //hander URL
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
#headers = { 'User-Agent' : user_agent }   
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}//Add header
req = Request(old_url, headers = headers)    
#req = Request(old_url)  
response = urlopen(req)   
the_page = response.read().decode("utf-8")  
soup = BeautifulSoup(the_page) 
#<span class="black">RADO 雷达 Centrix 晶萃系列 R30940112 女款机械腕表</span>
listtitle = soup.find_all("span",class_="black")//get title
#<span class="red">$638（需用码，约￥4070）</span></a></h2>
listtitle1 = soup.find_all("span",class_="red")//get price
#<h2 class="itemName"><a href="http://faxian.smzdm.com/p/500465" onclick="ga('send', 'event','发现频道','列表_文章标题',
#'500465_RADO 雷达 Centrix 晶萃系列 R30940112 女款机械腕表');" target="_blank">
listtitle2 = soup.find_all("h2",class_="itemName")//get link

for x,y,z in zip(listtitle,listtitle1,listtitle2):
	print x.string,y.string,z.find("a").get("href")

#another way
listtitle = soup.find_all("li",class_="list") // get all list tag and use keyword to get title link and herf

print (listtitle[1].prettify())

for x in listtitle:
	if (x.find("span",class_="red").string):
		print x.find("span",{"class": "black"}).string +" "+ x.find("span",{"class": "red"}).string + " " 
		      + x.find("a").get("href")

