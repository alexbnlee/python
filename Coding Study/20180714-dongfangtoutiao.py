import pynput
from pynput.mouse import Button
from pynput.keyboard import Key
mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()


def a():
	mouse.position = (3788, 289)
	for i in range(1, 20):
		time.sleep(0.5)
		mouse.scroll(0, -50)


def b():
	while(true):
		mouse.click(Button.left)
		a()


def c():
	mouse.press(Button.left)
	for i in range(0, 10):
		time.sleep(0.5)
		mouse.move(0, 50)
	mouse.release(Button.left)

def click():
	mouse.position = (3788, 289)
	mouse.click(Button.left)
	for i in range(1, 20):
		time.sleep(0.5)
		mouse.scroll(0, -50)

	mouse.position = (3666, 153)
	mouse.click(Button.left)

while(True):
	click()
	time.sleep(0.5)
	mouse.position = (3788, 289)
	mouse.scroll(0, -200)
	time.sleep(0.5)
	mouse.scroll(0, -200)
	time.sleep(0.5)
	mouse.scroll(0, -200)


from PIL import ImageGrab
from PIL import Image, ImageFilter
img = ImageGrab.grabclipboard()
region = (4010, 350, 4020, 360)
cropImage = img.crop(region)
lena_L = cropImage.convert("L")
lena_rgb = lena_L.convert("RGB")


def clip():
	keyboard.press(Key.print_screen)
	keyboard.release(Key.print_screen)
	img = ImageGrab.grabclipboard()
	region = (4010, 350, 4020, 360)
	cropImage = img.crop(region)
	lena_L = cropImage.convert("L")
	lena_rgb = lena_L.convert("RGB")
	if point(lena_rgb.getpixel((0,0))) and point(lena_rgb.getpixel((0,9))) and point(lena_rgb.getpixel((0,9))) and point(lena_rgb.getpixel((9,9))):
		return True
	else:
		return False



def point( rgb ):
	if rgb[0] < 20 and rgb[0] > 10:
		if rgb[1] < 20 and rgb[1] > 10:
			if rgb[2] < 20 and rgb[2] > 10:
				return True

point(lena_rgb.getpixel((0,0))) and point(lena_rgb.getpixel((0,9))) and point(lena_rgb.getpixel((0,9))) and point(lena_rgb.getpixel((9,9)))




mouse.position = (3735, 803)
mouse.click(Button.left)
time.sleep(0.5)


def dftt():
	while(True):
		for i in range(0, 20):
			if clip():
				mouse.position = (3735, 803)
				mouse.click(Button.left)
				time.sleep(0.5)
			else:
				click()
				time.sleep(0.5)

			mouse.position = (3788, 289)
			mouse.scroll(0, -200)
			time.sleep(0.5)
			mouse.scroll(0, -200)
			time.sleep(0.5)
			mouse.scroll(0, -200)
		mouse.position=(3678, 806)
		mouse.click(Button.left)
		time.sleep(0.5)
