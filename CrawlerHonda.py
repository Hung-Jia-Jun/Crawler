# -*- coding: utf-8 -*-
import requests
from ReadTxt_edit import *
from bs4 import BeautifulSoup
from tqdm import *
import os,io,pdb


TxtContant=[]
TxtContant=["广东,阳江"]#Read_txt("C:/Python27/Scripts/Crawler/CrawlerHonda/City.txt")
WriteFile=Write_txt("C:/Python27/Scripts/Crawler/CrawlerHonda/Honda_Store_Result.txt")
for cityTxt in TxtContant:
	WriteTxtStr=""
	province,city=cityTxt.split(",")
	url="http://www.ghac.cn/buy/tools/find-dealer?d=ws&type=finddealers&province="+province+"&city="+city
	r = requests.get(url)
	soup = BeautifulSoup(r.text,"html.parser")
	for Store in soup.find_all("tr"):
		try:
			WriteTxtStr+=province+","
			WriteTxtStr+=city+","
			WriteTxtStr+=str(Store.a).decode("big5").split(">")[1].split("<")[0].replace("\n","").replace("\r","").replace(" ","")+","
			print WriteTxtStr
			WriteTxtStr+=str(Store.find("td",{"class":"item2"})).decode("utf-8").split(">")[1].split("<")[0].replace("\n","").replace("\r","").replace(" ","")+","
			print WriteTxtStr
			WriteTxtStr+=str(Store.find("td",{"class":"item3"})).split(">")[1].split("<")[0].replace("\n","").replace("\r","").replace(" ","")
			print WriteTxtStr
			WriteFile.Write_Action(WriteTxtStr)
			WriteFile.Write_Action("\n")
			pass
		except IndexError:
			pass
		finally:
			WriteTxtStr=""

WriteFile.CloseFile()