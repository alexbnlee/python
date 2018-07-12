# coding=utf-8

def addToClipboard( string ):
	# 从 ArcGIS 导入的注意空格与 tab 键
	# 已经出错两次了
	"将字符串复制到剪贴板上"
	from tkinter import Tk
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
	r.withdraw()
	r.update()
	tmp = r.clipboard_get()
	r.destroy()
	return tmp

def cutChinese(string, *se):
	"实现汉字截取方法 —— 默认start为开始索引，不写end就是到结尾，否则到end"
	if len(se) == 0:
		return string
	
	# 不定长参数不为0
	start = se[0]
	if len(se)>1:
		end = se[1]
	else:
		end = len(string)
	tmp = string.decode('utf-8')[start:end].encode('utf-8')
	return tmp

def decodeChinese( string ):
	"将中文 utf-8 编码转为 Unicode 编码"
	tmp = string.decode('utf-8')
	return tmp

def encodeChinese( string ):
	"将 Unicode 编码转为 utf-8 编码"
	tmp = string.encode('utf-8')
	return tmp

def deleteEnter():
	"获取剪切板中的内容，将其中的回车键删除，例如从pdf或者caj文件复制的文本，结果添加至剪切板"
	ss = getClipboard()
	ss = ss.replace("\n", "")
	addToClipboard(ss)