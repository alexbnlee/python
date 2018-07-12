# coding=utf-8

def open_orbit_tracks():
	# Open terra & aqua orbit tracks sites based on the current day.
	import datetime
	import webbrowser
	today = datetime.datetime.today()
	year = today.year
	month = today.month
	day = today.day
	str_date01 = str(year)+'_'+str(month).zfill(2)+'_'+str(day).zfill(2)

	day_num = today.timetuple().tm_yday
	str_date02 = '_'+str(day_num).zfill(3)
	str_date = str_date01 + str_date02

	site_terra = r"https://www.ssec.wisc.edu/datacenter/terra/ASIA" + str_date + ".gif"
	webbrowser.open(site_terra)

	site_aqua = r"https://www.ssec.wisc.edu/datacenter/aqua/ASIA" + str_date + "_aqua.gif"
	webbrowser.open(site_aqua)

def add_time( terra_time_01, aqua_time_01 ):
	# 添加每日的下载时间，一个参数就增加一天，否则增加两天
	from xml.etree import ElementTree
	filepath = r"D:\03-Study\Python\Module\modis\config.xml"
	xmldoc = ElementTree.parse(filepath)
	node = xmldoc.find('TerraTime01')
	node.text = terra_time_01
	node = xmldoc.find('AquaTime01')
	node.text = aqua_time_01
	xmldoc.write(r"D:\03-Study\Python\Module\modis\config.xml")

def terra_data_download():
	# Open terra data download sites based on the current day.
	import datetime
	import webbrowser
	today = datetime.datetime.today()
	year = today.year
	day_num = today.timetuple().tm_yday

	import xml.dom.minidom
	filepath = r"D:\03-Study\Python\Module\modis\config.xml"
	dom = xml.dom.minidom.parse(filepath)
	tmp = dom.getElementsByTagName('TerraTime01')
	terra_time_01 = tmp[0].firstChild.data

	D_time = terra_time_01
	site_end = ".A"+str(year)+str(day_num).zfill(3)+"."+D_time+".061.NRT.hdf"

	site_MOD021KM = r"https://nrt3.modaps.eosdis.nasa.gov/allData/61/MOD021KM/"+str(year)+"/"+str(day_num).zfill(3)+"/MOD021KM"+site_end
	webbrowser.open(site_MOD021KM)

	site_MOD02HKM = r"https://nrt3.modaps.eosdis.nasa.gov/allData/61/MOD02HKM/"+str(year)+"/"+str(day_num).zfill(3)+"/MOD02HKM"+site_end
	webbrowser.open(site_MOD02HKM)

	site_MOD02QKM = r"https://nrt3.modaps.eosdis.nasa.gov/allData/61/MOD02QKM/"+str(year)+"/"+str(day_num).zfill(3)+"/MOD02QKM"+site_end
	webbrowser.open(site_MOD02QKM)

	site_MOD03 = r"https://nrt3.modaps.eosdis.nasa.gov/allData/61/MOD03/"+str(year)+"/"+str(day_num).zfill(3)+"/MOD03"+site_end
	webbrowser.open(site_MOD03)

def aqua_data_download():
	# Open aqua data download sites based on the current day.
	import datetime
	import webbrowser
	today = datetime.datetime.today()
	year = today.year
	day_num = today.timetuple().tm_yday

	import xml.dom.minidom
	filepath = r"D:\03-Study\Python\Module\modis\config.xml"
	dom = xml.dom.minidom.parse(filepath)
	tmp = dom.getElementsByTagName('AquaTime01')
	aqua_time_01 = tmp[0].firstChild.data

	D_time = aqua_time_01
	site_end = ".A"+str(year)+str(day_num).zfill(3)+"."+D_time+".061.NRT.hdf"

	site_MYD021KM = r"https://nrt3.modaps.eosdis.nasa.gov/allData/61/MYD021KM/"+str(year)+"/"+str(day_num).zfill(3)+"/MYD021KM"+site_end
	webbrowser.open(site_MYD021KM)

	site_MYD02HKM = r"https://nrt3.modaps.eosdis.nasa.gov/allData/61/MYD02HKM/"+str(year)+"/"+str(day_num).zfill(3)+"/MYD02HKM"+site_end
	webbrowser.open(site_MYD02HKM)

	site_MYD02QKM = r"https://nrt3.modaps.eosdis.nasa.gov/allData/61/MYD02QKM/"+str(year)+"/"+str(day_num).zfill(3)+"/MYD02QKM"+site_end
	webbrowser.open(site_MYD02QKM)

	site_MYD03 = r"https://nrt3.modaps.eosdis.nasa.gov/allData/61/MYD03/"+str(year)+"/"+str(day_num).zfill(3)+"/MYD03"+site_end
	webbrowser.open(site_MYD03)