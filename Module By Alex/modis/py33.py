# coding=utf-8

def get_orbit_tracks(year, month, day):
	# 可以用来打开指定年月日的轨道图像
	# 鉴于监测数据不关注12月，因此不需要单独考虑了
	import datetime, webbrowser
	s_day = datetime.datetime(year,month,day)
	s_day_01 = datetime.datetime(year,month,1)
	s_day_02 = datetime.datetime(year,month+1,1)

	terra_site = "http://www.ssec.wisc.edu/datacenter/terra/archive/ASIA/"+str(year)+"_"+str(month).zfill(2)+\
	"("+str(s_day_01.timetuple().tm_yday).zfill(3)+"-"+str(s_day_02.timetuple().tm_yday - 1).zfill(3)+\
	")/ASIA"+str(year)+"_"+str(month).zfill(2)+"_"+str(day).zfill(2)+"_"+\
	str(s_day.timetuple().tm_yday).zfill(3)+".gif"

	aqua_site = "http://www.ssec.wisc.edu/datacenter/aqua/archive/ASIA/"+str(year)+"_"+str(month).zfill(2)+\
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

# 打开浏览器为主浏览器，已废弃
def openFirefox():
	# import pynput, time
	# from pynput.mouse import Button
	# mouse = pynput.mouse.Controller()
	# mouse.position = (307, 850)
	# mouse.click(Button.left)
	# time.sleep(0.4)
	# mouse.position = (282, 764)
	# mouse.click(Button.left)
	import pynput, time
	from pynput.keyboard import Key
	keyboard = pynput.keyboard.Controller()
	# 通过 Ctrl+w 快捷键删除当前页面
	with keyboard.pressed(Key.alt):
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)

# 关闭网页
def closePage():
	import pynput, time
	from pynput.keyboard import Key
	keyboard = pynput.keyboard.Controller()
	# 通过 Ctrl+w 快捷键删除当前页面
	with keyboard.pressed(Key.ctrl):
		keyboard.press('w')
		keyboard.release('w')

def monitoring_terra_data():
	# Open terra data download sites based on the current day.
	from PIL import ImageGrab
	from PIL import Image, ImageFilter
	import pynput, time, os, psutil, pytesseract, datetime, webbrowser, xml.dom.minidom
	from pynput.mouse import Button
	from pynput.keyboard import Key
	mouse = pynput.mouse.Controller()
	keyboard = pynput.keyboard.Controller()

	today = datetime.datetime.today()
	filepath = r"D:\03-Study\Python\Module\modis\config.xml"
	dom = xml.dom.minidom.parse(filepath)
	tmp = dom.getElementsByTagName('TerraTime01')
	terra = tmp[0].firstChild.data

	moniter_time = datetime.datetime(today.year, today.month, today.day, int(terra[0:2])+8,int(terra[2:4]),0,0)
	now = datetime.datetime.today()
	while((now - moniter_time).days == -1):
		time.sleep(300)
		print("倒计时："+str(60+(moniter_time-now).seconds//60)+"分")
		now = datetime.datetime.today()
	now = datetime.datetime.today()
	while((now - moniter_time).seconds//60 < 60):
		time.sleep(300)
		print("流逝："+str((now-moniter_time).seconds//60)+"分")
		now = datetime.datetime.today()

	site_end = ".A"+str(today.year)+str(today.timetuple().tm_yday).zfill(3)+"."+terra+".061.NRT.hdf"
	site_start = "https://nrt3.modaps.eosdis.nasa.gov/allData/61/"
	# 用于判断数据是否能够下载
	flag = 0
	flag_cha = 0
	for i in range(0, 100):
		print("Downloading file: " + "MOD021KM" + site_end)
		#openFirefox()
		webbrowser.open(site_start+"MOD021KM"+"/"+str(today.year)+"/"+str(today.timetuple().tm_yday).zfill(3)+"/"+"MOD021KM"+site_end)
		# 用来打开网页
		time.sleep(10)
		x1 = mouse.position[0]-36
		y1 = mouse.position[1]-11
		x2 = mouse.position[0]+36
		y2 = mouse.position[1]+11
		# 移动鼠标，然后点击下左键，否则 printscreen 总出错
		mouse.position = (x1-64, y1+11)
		mouse.click(Button.left)
		keyboard.press(Key.print_screen)
		keyboard.release(Key.print_screen)
		# 剪切板不会立即获取，需要处理时间
		time.sleep(0.5)
		img = ImageGrab.grabclipboard()
		region = (x1,y1,x2,y2)
		if(img):
			cropImg = img.crop(region)
			# 放大图像，否则识别不到
			zoomImg = cropImg.resize((cropImg.size[0]*2, cropImg.size[1]*2), Image.ANTIALIAS)
			zoomImg.filter(ImageFilter.SHARPEN).save("D:\\03-Study\\Python\\Module\\modis\\save.jpg")
			#zoomImg.save('D:\\03-Study\\Python\\Module\\modis\\save.jpg')
			# 识别图像内容，是否为“保存”
			text=pytesseract.image_to_string(Image.open('D:\\03-Study\\Python\\Module\\modis\\save.jpg'),lang='chi_sim')
			print(text)
			# 判断是否有“保存”字样
			chas = ["保","存","戾","荏","固","僳","菌","阱"]
			for cha in chas:
				if cha.find(cha) > - 1:
					flag_cha = 1
			if(flag_cha):
				# 删除HDF文件
				rootdir = r"D:\MODISPRO\MODIS"
				for file in os.listdir(rootdir):
					if file.find("hdf") > 0:
						os.remove(os.path.join(rootdir, file))
				
				mouse.position = (x1+36, y1+11)
				mouse.click(Button.left)
				closePage()
				MODS = ["MOD02HKM", "MOD02QKM", "MOD03"]
				for MOD in MODS:
					webbrowser.open(site_start+MOD+"/"+str(today.year)+"/"+str(today.timetuple().tm_yday).zfill(3)+"/"+MOD+site_end)
					print("Downloading file: " + MOD + site_end)
					time.sleep(10)
					mouse.click(Button.left)
					closePage()
				print("----- Downloading Start -----")

				# 判断数据是否下载完毕，并处理
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
						os.chdir(r"D:\MODISPRO")
						os.system(r"D:\MODISPRO\run-rename.bat")
						return
					else:
						if i*10%60==0:
							print("Download "+str(1+i*10//60)+" minite(s)...")
				flag = 1
			else:
				print("----- Downloading Error -----")
				#关闭网页，需要定位，因此要重新打开一次，然后关闭两次
				webbrowser.open("www.baidu.com")
				time.sleep(0.5)
				closePage()
				closePage()
		if(flag):
			break
		# 每次循环的时间为5分钟
		time.sleep(300)

def monitoring_aqua_data():
	# Open aqua data download sites based on the current day.
	from PIL import ImageGrab
	from PIL import Image
	import pynput, time, os, psutil, pytesseract, datetime, webbrowser, xml.dom.minidom
	from pynput.mouse import Button
	from pynput.keyboard import Key
	mouse = pynput.mouse.Controller()
	keyboard = pynput.keyboard.Controller()

	today = datetime.datetime.today()
	filepath = r"D:\03-Study\Python\Module\modis\config.xml"
	dom = xml.dom.minidom.parse(filepath)
	tmp = dom.getElementsByTagName('AquaTime01')
	aqua = tmp[0].firstChild.data

	moniter_time = datetime.datetime(today.year, today.month, today.day, int(aqua[0:2])+8,int(aqua[2:4]),0,0)
	now = datetime.datetime.today()
	while((now - moniter_time).days == -1):
		time.sleep(300)
		print("倒计时："+str(60+(moniter_time-now).seconds//60)+"分")
		now = datetime.datetime.today()
	now = datetime.datetime.today()
	while((now - moniter_time).seconds//60 < 60):
		time.sleep(300)
		print("流逝："+str((now-moniter_time).seconds//60)+"分")
		now = datetime.datetime.today()

	site_end = ".A"+str(today.year)+str(today.timetuple().tm_yday).zfill(3)+"."+aqua+".061.NRT.hdf"
	site_start = "https://nrt3.modaps.eosdis.nasa.gov/allData/61/"
	# 用于判断数据是否能够下载
	flag = 0
	for i in range(0, 100):
		print("Downloading file: " + "MYD021KM" + site_end)
		#openFirefox()
		webbrowser.open(site_start+"MYD021KM"+"/"+str(today.year)+"/"+str(today.timetuple().tm_yday).zfill(3)+"/"+"MYD021KM"+site_end)
		# 用来打开网页
		time.sleep(10)
		x1 = mouse.position[0]-36
		y1 = mouse.position[1]-8
		x2 = mouse.position[0]+36
		y2 = mouse.position[1]+8
		# 移动鼠标，然后点击下左键，否则 printscreen 总出错
		mouse.position = (x1-64, y1+8)
		mouse.click(Button.left)
		keyboard.press(Key.print_screen)
		keyboard.release(Key.print_screen)
		# 剪切板不会立即获取，需要处理时间
		time.sleep(0.5)
		img = ImageGrab.grabclipboard()
		region = (x1,y1,x2,y2)
		if(img):
			cropImg = img.crop(region)
			# 放大图像，否则识别不到
			zoomImg = cropImg.resize((cropImg.size[0]*2, cropImg.size[1]*2), Image.ANTIALIAS)
			zoomImg.save('D:\\03-Study\\Python\\Module\\modis\\save.jpg')
			# 识别图像内容，是否为“保存”
			text=pytesseract.image_to_string(Image.open('D:\\03-Study\\Python\\Module\\modis\\save.jpg'),lang='chi_sim')
			# 判断是否有“保存”字样
			if(text.find("保") > -1 or text.find("存") > -1):
				# 删除HDF文件
				rootdir = r"D:\MODISPRO\MODIS"
				for file in os.listdir(rootdir):
					if file.find("hdf") > 0:
						os.remove(os.path.join(rootdir, file))
				
				mouse.position = (x1+64, y1+8)
				mouse.click(Button.left)
				closePage()
				MYDS = ["MYD02HKM", "MYD02QKM", "MYD03"]
				for MYD in MYDS:
					webbrowser.open(site_start+MYD+"/"+str(today.year)+"/"+str(today.timetuple().tm_yday).zfill(3)+"/"+MYD+site_end)
					print("Downloading file: " + MYD + site_end)
					time.sleep(10)
					mouse.click(Button.left)
					closePage()
				print("----- Downloading Start -----")

				# 判断数据是否下载完毕，并处理
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
						os.chdir(r"D:\MODISPRO")
						os.system(r"D:\MODISPRO\run-rename.bat")
						return
					else:
						if i*10%60==0:
							print("Download "+str(1+i*10//60)+" minite(s)...")
				flag = 1
			else:
				print("----- Downloading Error -----")
				#关闭网页，需要定位，因此要重新打开一次，然后关闭两次
				webbrowser.open("www.baidu.com")
				time.sleep(0.5)
				closePage()
				closePage()
		if(flag):
			break
		# 每次循环的时间为5分钟
		time.sleep(300)

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
		terra_input = input("Terra Time: ")
		aqua_input = input("Aqua Time: ")
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

def open_orbit_tracks():
	# Open terra & aqua orbit tracks sites based on the current day.
	import datetime, webbrowser
	today = datetime.datetime.today()
	str_date01 = str(today.year)+'_'+str(today.month).zfill(2)+'_'+str(today.day).zfill(2)
	str_date = str_date01 + '_'+str(today.timetuple().tm_yday).zfill(3)
	webbrowser.open("www.ssec.wisc.edu/datacenter/terra/ASIA" + str_date + ".gif")
	webbrowser.open("www.ssec.wisc.edu/datacenter/aqua/ASIA" + str_date + "_aqua.gif")

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

	from tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(terra+"\n\n"+aqua)
	r.update()
	r.destroy()
