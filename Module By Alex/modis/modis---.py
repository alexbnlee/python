# coding=utf-8
# 针对 Python 3.6.5 进行更新，包括 Twilio 模块，以及 print 函数。（2018年6月20日）

def open_orbit_tracks():
	# Open terra & aqua orbit tracks sites based on the current day.
	import datetime, webbrowser
	today = datetime.datetime.today()
	str_date01 = str(today.year)+'_'+str(today.month).zfill(2)+'_'+str(today.day).zfill(2)
	str_date = str_date01 + '_'+str(today.timetuple().tm_yday).zfill(3)
	webbrowser.open("https://www.ssec.wisc.edu/datacenter/terra/ASIA" + str_date + ".gif")
	webbrowser.open("https://www.ssec.wisc.edu/datacenter/aqua/ASIA" + str_date + "_aqua.gif")

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

	terra = "Terra: "+str(int(terra_time_01[0:2]))+":"+terra_time_01[2:4]+" - "+str(int(terra_time_01[0:2])+8)+":"+terra_time_01[2:4]
	aqua = "Aqua: "+str(int(aqua_time_01[0:2]))+":"+aqua_time_01[2:4]+" - "+str(int(aqua_time_01[0:2])+8)+":"+aqua_time_01[2:4]
	print(terra+"\n"+aqua)

	from Tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(terra+"\n\n"+aqua)
	r.update()
	r.destroy()

def download_terra_data():
	# Open terra data download sites based on the current day.
	import datetime, webbrowser, xml.dom.minidom, os, time

	rootdir = r"D:\MODISPRO\MODIS"
	for file in os.listdir(rootdir):
		if file.find("hdf") > 0:
			os.remove(os.path.join(rootdir, file))

	today = datetime.datetime.today()
	filepath = r"D:\03-Study\Python\Module\modis\config.xml"
	dom = xml.dom.minidom.parse(filepath)
	tmp = dom.getElementsByTagName('TerraTime01')
	site_end = ".A"+str(today.year)+str(today.timetuple().tm_yday).zfill(3)+"."+tmp[0].firstChild.data+".061.NRT.hdf"
	site_start = "https://nrt3.modaps.eosdis.nasa.gov/allData/61/"
	MODS = ["MOD021KM", "MOD02HKM", "MOD02QKM", "MOD03"]
	for MOD in MODS:
		webbrowser.open(site_start+MOD+"/"+str(today.year)+"/"+str(today.timetuple().tm_yday).zfill(3)+"/"+MOD+site_end)

	time.sleep(60)
	for i in range(0, 1000):
		time.sleep(10)
		flag = 0
		files = os.listdir(r"D:\MODISPRO\MODIS")
		for file in files:
			if "hdf.part" in file:
				flag = 1
		if flag == 0:
			print("processing...")
			textMessage("McDelfino, it's time to process MODIS data~")
			os.chdir(r"D:\MODISPRO")
			os.system(r"D:\MODISPRO\run-rename.bat")
			return
		else:
			if i*10%60==0:
				print("Download "+str(1+i*10/60)+" minite(s)...")

def download_aqua_data():
	# Open aqua data download sites based on the current day.
	import datetime, webbrowser, xml.dom.minidom, os, time
	
	rootdir = r"D:\MODISPRO\MODIS"
	for file in os.listdir(rootdir):
		if file.find("hdf") > 0:
			os.remove(os.path.join(rootdir, file))

	today = datetime.datetime.today()
	filepath = r"D:\03-Study\Python\Module\modis\config.xml"
	dom = xml.dom.minidom.parse(filepath)
	tmp = dom.getElementsByTagName('AquaTime01')
	site_end = ".A"+str(today.year)+str(today.timetuple().tm_yday).zfill(3)+"."+tmp[0].firstChild.data+".061.NRT.hdf"
	site_start = "https://nrt3.modaps.eosdis.nasa.gov/allData/61/"
	MYDS = ["MYD021KM", "MYD02HKM", "MYD02QKM", "MYD03"]
	for MYD in MYDS:
		webbrowser.open(site_start+MYD+"/"+str(today.year)+"/"+str(today.timetuple().tm_yday).zfill(3)+"/"+MYD+site_end)

	time.sleep(60)
	for i in range(0, 1000):
		time.sleep(10)
		flag = 0
		files = os.listdir(r"D:\MODISPRO\MODIS")
		for file in files:
			if "hdf.part" in file:
				flag = 1
		if flag == 0:
			print("processing...")
			textMessage("McDelfino, it's time to process MODIS data~")
			os.chdir(r"D:\MODISPRO")
			os.system(r"D:\MODISPRO\run-rename.bat")
			return
		else:
			if i*10%60==0:
				print("Download "+str(1+i*10/60)+" minite(s)...")

def monitoring_terra_data():
	# Open terra data download sites based on the current day.
	import datetime, webbrowser, xml.dom.minidom, time
	today = datetime.datetime.today()
	filepath = r"D:\03-Study\Python\Module\modis\config.xml"
	dom = xml.dom.minidom.parse(filepath)
	tmp = dom.getElementsByTagName('TerraTime01')
	terra = tmp[0].firstChild.data

	moniter_time = datetime.datetime(today.year, today.month, today.day, int(terra[0:2])+8,int(terra[2:4]),0,0)
	now = datetime.datetime.today()
	while((now - moniter_time).days == -1):
		time.sleep(300)
		print("倒计时："+str(60+(moniter_time-now).seconds/60)+"分")
		now = datetime.datetime.today()
	now = datetime.datetime.today()
	while((now - moniter_time).seconds/60 < 60):
		time.sleep(300)
		print("流逝："+str((now-moniter_time).seconds/60)+"分")
		now = datetime.datetime.today()

	site_end = ".A"+str(today.year)+str(today.timetuple().tm_yday).zfill(3)+"."+terra+".061.NRT.hdf"
	site_start = "https://nrt3.modaps.eosdis.nasa.gov/allData/61/"
	for i in range(0, 100):
		time.sleep(300)
		webbrowser.open(site_start+"MOD021KM"+"/"+str(today.year)+"/"+str(today.timetuple().tm_yday).zfill(3)+"/"+"MOD021KM"+site_end)

def monitoring_aqua_data():
	# Open aqua data download sites based on the current day.
	import datetime, webbrowser, xml.dom.minidom, time
	today = datetime.datetime.today()
	filepath = r"D:\03-Study\Python\Module\modis\config.xml"
	dom = xml.dom.minidom.parse(filepath)
	tmp = dom.getElementsByTagName('AquaTime01')
	aqua = tmp[0].firstChild.data

	moniter_time = datetime.datetime(today.year, today.month, today.day, int(aqua[0:2])+8,int(aqua[2:4]),0,0)
	now = datetime.datetime.today()
	while((now - moniter_time).days == -1):
		time.sleep(300)
		print("倒计时："+str(60+(moniter_time-now).seconds/60)+"分")
		now = datetime.datetime.today()
	now = datetime.datetime.today()
	while((now - moniter_time).seconds/60 < 60):
		time.sleep(300)
		print("流逝：："+str((now-moniter_time).seconds/60)+"分")
		now = datetime.datetime.today()

	site_end = ".A"+str(today.year)+str(today.timetuple().tm_yday).zfill(3)+"."+tmp[0].firstChild.data+".061.NRT.hdf"
	site_start = "https://nrt3.modaps.eosdis.nasa.gov/allData/61/"
	for i in range(0, 100):
		time.sleep(300)
		webbrowser.open(site_start+"MYD021KM"+"/"+str(today.year)+"/"+str(today.timetuple().tm_yday).zfill(3)+"/"+"MYD021KM"+site_end)

def a():
	# 根据时间和相应参数智能调用函数
	import datetime, xml.dom.minidom, time
	from xml.etree import ElementTree
	today = datetime.datetime.today()
	filepath = r"D:\03-Study\Python\Module\modis\config.xml"
	dom = xml.dom.minidom.parse(filepath)
	tmp = dom.getElementsByTagName('Date')
	str_date = tmp[0].firstChild.data
	array_date = str_date.split(u'-')
	date_date = datetime.datetime(int(array_date[0]), int(array_date[1]), int(array_date[2]))
	if (today - date_date).days >= 1:
		tmp = '-'.join([str(today.year), str(today.month), str(today.day)])
		xmldoc = ElementTree.parse(filepath)
		node = xmldoc.find('Date')
		node.text = tmp
		xmldoc.write(filepath)
		# 今天第一次运行，将今天日期添加，同时打开轨道图
		print("正在执行 open_orbit_tracks() 函数...")
		open_orbit_tracks()
		# 输入Terra和Aqua的过境时间
		terra_input = raw_input("Terra Time: ")
		aqua_input = raw_input("Aqua Time: ")
		print("正在执行 add_time() 函数...")
		add_time(terra_input, aqua_input)
		# 执行监测Terra、Aqua监测函数
		if today.hour <= 12:
			print("正在执行 monitoring_terra_data() 函数...")
			monitoring_terra_data()
		else:
			print("正在执行 monitoring_aqua_data() 函数...")
			monitoring_aqua_data()
	else:
		# 执行监测Terra、Aqua监测函数
		if today.hour <= 12:
			print("正在执行 monitoring_terra_data 函数...")
			monitoring_terra_data()
		else:
			print("正在执行 monitoring_aqua_data() 函数...")
			monitoring_aqua_data()

def textMessage(message):
	from twilio.rest import Client  
			
	account = 'AC898e7bb8fd507eb1b911cfff1298b5bd' 
	token = '2af358e9fc0ef645d324e3d21c7975d9' 
	myNumber='+8615942402910' 
	twilioNumber='+14243734855' 

	client = Client(account, token) 
	message = client.messages.create(to=myNumber, from_=twilioNumber, body=message)