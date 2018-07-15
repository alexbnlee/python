import pynput, time
from pynput.mouse import Button
from pynput.keyboard import Key
mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()
from PIL import ImageGrab
from PIL import Image, ImageFilter

# position_news = (4235, 216)
# position_back = (4043, 80)
# position_cancel = (4139, 732)
# position_refresh = (4072, 732)
# region = (4430, 450, 4460, 480)

position_news = (4142, 212)
position_back = (3930, 67)
position_cancel = (4139, 732)
position_refresh = (3968, 735)
region = (4430, 450, 4460, 480)

def click():
	'鼠标点击并滑动，然后点击左上角的返回键'
	# 新闻内容的位置
	mouse.position = position_news
	mouse.click(Button.left)
	for i in range(1, 30):
		time.sleep(1)
		mouse.scroll(0, -50)
	# 返回按钮的位置
	mouse.position = position_back
	mouse.click(Button.left)

def clip():
	'剪切图片，判断RGB值，判断是否是安装包'
	keyboard.press(Key.print_screen)
	keyboard.release(Key.print_screen)
	time.sleep(0.5)
	img = ImageGrab.grabclipboard()
	cropImage = img.crop(region)
	lena_L = cropImage.convert("L")
	lena_rgb = lena_L.convert("RGB")
	# 截取图片的四个角的RGB值来判断
	if point(lena_rgb.getpixel((0,0))) and point(lena_rgb.getpixel((0,9))) and point(lena_rgb.getpixel((0,9))) and point(lena_rgb.getpixel((9,9))):
	# if point(lena_rgb.getpixel((0,0)), lena_rgb.getpixel((0,29)), lena_rgb.getpixel((29,0)), lena_rgb.getpixel((29,29))):
		return True
	else:
		return False

def point( rgb ):
	'判断RGB值'
	if rgb[0] < 30 and rgb[0] > 10:
		if rgb[1] < 30 and rgb[1] > 10:
			if rgb[2] < 30 and rgb[2] > 10:
				return True
# 				
# def point( rgb1, rgb2, rgb3, rgb4 ):
# 	'判断4个点RGB值的标准差小于5，说明都很相近，判断为灰色系'
# 	import numpy
# 	if numpy.std([rgb1[0], rgb2[0], rgb3[0], rgb4[0]]) < 5:
# 		if numpy.std([rgb1[1], rgb2[1], rgb3[1], rgb4[1]]) < 5:
# 			if numpy.std([rgb1[2], rgb2[2], rgb3[2], rgb4[2]]) < 5:
# 				return True



def dftt():
	'无限循环'
	import pynput, time, dftt
	from pynput.mouse import Button
	from pynput.keyboard import Key
	mouse = pynput.mouse.Controller()
	keyboard = pynput.keyboard.Controller()

	while(True):
		# 循环20次，需要刷新下新闻
		for i in range(0, 20):
			if clip():
				# 如果是安装包的话，点击取消
				# 取消按钮的位置
				mouse.position = position_cancel
				mouse.click(Button.left)
				time.sleep(0.5)
			else:
				click()
				time.sleep(0.5)
			# 返回主页面后，往下滑动到下一个新闻块
			# 新闻内容位置
			mouse.position = position_news
			mouse.scroll(0, -200)
			time.sleep(0.5)
			mouse.scroll(0, -200)
			time.sleep(0.5)
			mouse.scroll(0, -200)
		# 刷新新闻的位置
		mouse.position = position_refresh
		mouse.click(Button.left)
		time.sleep(0.5)