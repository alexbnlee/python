# coding=utf-8

def addToClipboard( string ):
	# 从 ArcGIS 导入的注意空格与 tab 键
	# 已经出错两次了
	"将字符串复制到剪贴板上"
	from Tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(string)
	r.update()
	r.destroy()

def getClipboard():
	"返回剪贴板上的内容"
	from Tkinter import Tk
	r = Tk()
	r.update()
	tmp = r.clipboard_get()
	r.destroy()
	return tmp

def cutChinese(string, *se):
	"实现汉字截取方法 —— 默认start为开始索引，不写end就是到结尾，否则到end"
	start = se[0]
	if len(se)>1:
		end = se[1]
	else:
		end = len(string)
	tmp = string.decode('utf-8')[start:end].encode('utf-8')
	return tmp
