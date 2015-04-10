# -*- coding: utf-8 -*-
from urllib2 import Request, urlopen, URLError, HTTPError  
import re  
from bs4 import BeautifulSoup

old_url = 'http://faxian.smzdm.com/p1'  
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
#headers = { 'User-Agent' : user_agent }   
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
req = Request(old_url, headers = headers)   
#req = Request(old_url)  
response = urlopen(req)   
the_page = response.read().decode("utf-8")  
soup = BeautifulSoup(the_page)
listtitle = soup.find_all("span",class_="black")
listtitle1 = soup.find_all("span",class_="red")
listtitle2 = soup.find_all("h2",class_="itemName")

for x,y,z in zip(listtitle,listtitle1,listtitle2):
	print x.string,y.string,z.find("a").get("href")
