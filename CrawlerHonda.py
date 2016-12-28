# -*- coding: utf-8 -*-
import requests
from ReadTxt_edit import *
from bs4 import BeautifulSoup
from tqdm import *
import os,io,pdb
TxtContant=[]
TxtContant=Read_txt("C:/Python27/Scripts/Crawler/CrawlerHonda/City.txt")#["广东,阳江"]
WriteFile=Write_txt("C:/Python27/Scripts/Crawler/CrawlerHonda/Honda_Store_Result1.txt")
for cityTxt in tqdm(TxtContant):
	WriteTxtStr=""
	try:
		province,city=cityTxt.split(",")
	except ValueError: #遇到香港特別行政區時就跳過.
		continue #跳過這次循環
	url="http://www.ghac.cn/buy/tools/find-dealer?d=ws&type=finddealers&province="+province+"&city="+city
	while True:
		try:
			r = requests.get(url,timeout=30)
		except requests.exceptions.Timeout:
			print "Timeout"
			pass
		else:
			break #離開迴圈

	soup = BeautifulSoup(r.text,"html.parser")
	for Store in soup.find_all("tr"):
		try:
			WriteTxtStr+=province+","
			WriteTxtStr+=city+","
			WriteTxtStr+=str(Store.a).decode("utf-8").split(">")[1].split("<")[0].replace("\n","").replace("\r","").replace(" ","")+","
			WriteTxtStr+=str(Store.find("td",{"class":"item2"})).decode("utf-8").split(">")[1].split("<")[0].replace("\n","").replace("\r","").replace(" ","")+","
			WriteTxtStr+=str(Store.find("td",{"class":"item3"})).decode("utf-8").split(">")[1].split("<")[0].replace("\n","").replace("\r","").replace(" ","")
			WriteFile.Write_Action(WriteTxtStr.encode("utf-8"))
			WriteFile.Write_Action("\n")
			WriteFile.CloseFile()
			pass
		except IndexError:
			pass
		finally:
			WriteTxtStr=""

