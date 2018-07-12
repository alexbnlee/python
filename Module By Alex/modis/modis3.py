# coding=utf-8

def get_orbit_tracks(year, month, day):
	# 可以用来打开指定年月日的轨道图像
	# 鉴于监测数据不关注12月，因此不需要单独考虑了
	import datetime, webbrowser
	s_day = datetime.datetime(year,month,day)
	s_day_01 = datetime.datetime(year,month,1)
	s_day_02 = datetime.datetime(year,month+1,1)

	terra_site = "https://www.ssec.wisc.edu/datacenter/terra/archive/ASIA/"+str(year)+"_"+str(month).zfill(2)+\
	"("+str(s_day_01.timetuple().tm_yday).zfill(3)+"-"+str(s_day_02.timetuple().tm_yday - 1).zfill(3)+\
	")/ASIA"+str(year)+"_"+str(month).zfill(2)+"_"+str(day).zfill(2)+"_"+\
	str(s_day.timetuple().tm_yday).zfill(3)+".gif"

	aqua_site = "https://www.ssec.wisc.edu/datacenter/aqua/archive/ASIA/"+str(year)+"_"+str(month).zfill(2)+\
	"("+str(s_day_01.timetuple().tm_yday).zfill(3)+"-"+str(s_day_02.timetuple().tm_yday - 1).zfill(3)+\
	")/ASIA"+str(year)+"_"+str(month).zfill(2)+"_"+str(day).zfill(2)+"_"+\
	str(s_day.timetuple().tm_yday).zfill(3)+"_aqua.gif"

	webbrowser.open(terra_site)
	webbrowser.open(aqua_site)

def open_terra_data(year, month, day):
	# Open terra data download sites based on the current day.
	import datetime, webbrowser, os
	s_day = datetime.datetime(year,month,day)
	site_start = "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/"
	MODS = ["MOD021KM", "MOD02HKM", "MOD02QKM", "MOD03"]
	for MOD in MODS:
		webbrowser.open(site_start+MOD+"/"+str(year)+"/"+str(s_day.timetuple().tm_yday).zfill(3)+"/")

def open_aqua_data(year, month, day):
	# Open aqua data download sites based on the current day.
	import datetime, webbrowser, os
	s_day = datetime.datetime(year,month,day)
	site_start = "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/"
	MYDS = ["MYD021KM", "MYD02HKM", "MYD02QKM", "MYD03"]
	for MYD in MYDS:
		webbrowser.open(site_start+MYD+"/"+str(year)+"/"+str(s_day.timetuple().tm_yday).zfill(3)+"/")




