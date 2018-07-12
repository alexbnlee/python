# coding=utf-8

def getTitleByNum( *t ):
	# 将得到的结果自动复制到剪贴板上
	# 将复制的标题内容添加HTML样式
	# 如果不带参数，则会自从提取剪切板内容
	# 参数举例："一、测试"
	"通过检测大写数字来添加锚点以及标题样式"
	# 需要调用里面关于剪切板的函数
	from win_diy import *
	dict = {'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8}
	num_CHN = ['一', '二', '三', '四', '五', '六', '七', '八']

	# 判断参数，没有参数的话，自动获取剪切板内容
	if len(t) == 0:
		title = win.getClipboard()
	else:
		title = t[0]	
	
	# 样式字符
	s = ""

	# 遍历大写数字，进行查找	
	for num in num_CHN:
		# 判断title的编码类型，判断是否为Unicode
		# 是的话，需要将查找词转成一样的编码
		if isinstance(title, unicode):
			index = title.find(num.decode('utf-8'))
		else:
			index = title.find(num)

		if index > -1:
			s = '<div class="title_hh"><a name="A'+(str(dict[num])).zfill(2)+'"></a><strong>' + title + '</strong></div>\n<div class="arrow-left">&nbsp;</div>'

	# 若s无赋值
	if s == "":
		s = '<div class="title_hh"><a name="A00"></a><strong>' + title + '</strong></div>\n<div class="arrow-left">&nbsp;</div>'

	win.addToClipboard(s)
	return s

def contentAnchor( *t ):
	# 将得到的结果自动复制到剪贴板上
	# 将目录的标题添加数据HTML链接样式
	# 参数举例：“<li>四、测试</li>”或者“<li>四、测试”
	"通过检测大写数字以及<li>来添加链接"
	# 需要调用里面关于剪切板的函数
	from win_diy import *
	dict = {'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8}
	num_CHN = ['一', '二', '三', '四', '五', '六', '七', '八']

	# 判断参数，如果没有参数，则获取剪切板内容
	if len(t) == 0:
		title = win.getClipboard()
		# 从网页或者记事本复制的中文是Unicode编码的
		# python的中文定义字符是utf-8编码的
		# 因此需要转码才能操作
	else:
		# 直接写的参数，编码是utf-8，不需要转换
		title = t[0]

	# 存储代码文本
	ss = ""

	for num in num_CHN:
		# 判断title的编码类型，判断是否为Unicode
		if isinstance(title, unicode):
			index = title.find(num.decode('utf-8'))
			index_end = title.find(u'</li>')

			if index > -1 and index_end > -1:
				ss = '<li><a href="#A'+(str(dict[num])).zfill(2)+'">' + title[index:index_end] + '</a></li>'
			
			#如果有二级标题，则没有</li>
			if index > -1 and index_end == -1:
				index_end = len(title)
				ss = '<li><a href="#A'+(str(dict[num])).zfill(2)+'""' + title[index:index_end] + '</a>'
		else:
			# 编码类型不为Unicode，直接查询
			index = title.find(num)
			index_end = title.find('</li>')
			
			if index > -1 and index_end > -1:
				ss = '<li><a href="#A'+(str(dict[num])).zfill(2)+'">' + title[index:index_end] + '</a></li>'

			#如果有二级标题，则没有</li>，转成Unicode求长度
			if index > -1 and index_end == -1:
				index_end = len(title.decode('utf-8'))
				ss = '<li><a href="#A'+(str(dict[num])).zfill(2)+'">' + title[index:index_end] + '</a>'
	
	# 如果ss没有赋值，则按如下赋值
	if ss == "":
		ss = '<li><a href="#A00">' + title[4:len(title)-5] + '</a></li>'

	win.addToClipboard(ss)
	print ss
	return ss

def changeTitleAndContents_Tier1():
	# 将得到的结果自动复制到剪贴板上
	# 本函数针对整个HTML代码
	# 包括前面目录部分自动添加 目录 & 链接
	# 后面标题部分自动添加标题样式以及锚点
	# 需要引用其他函数
	# 参数来自于剪切板复制
	# 标题特点，按照标题1格式的<h1>
	"为一级标题添加特殊样式、添加目录、为目录添加链接 的 HTML 代码（针对没有添加目录的源码）"
	
	# 为Unicode编码，为了统一复制来的数据编码
	contents = [u'<p>目录：</p>', u'<ul>']

	# 需要调用里面关于剪切板的函数
	from win_diy import *
	str_all = win.getClipboard()
	str_all_array = str_all.splitlines()
	
	# 查找其所在行
	# 转换为 Unicode 编码才可以操作
	# 为标题添加样式以及锚点
	i = 0
	for s in str_all_array:
		# 查找<h2>
		if s.find(u'<h1') >= 0: 
			index_end = s.find(u'</')
			index = s.rfind(u'>', 0, index_end) + 1
			title = s[index:index_end]
			str_all_array[i] = getTitleByNum(title)
			# 添加Unicode编码字符，将目录内容叠加
			contents.append(contentAnchor(u'<li>' + title + '</li>'))
		i = i + 1

	# 最后叠加结尾部分
	contents.append(u'</ul>')
	# 分割线
	contents.append(u'<hr />')
	# 将目录内容后面叠加原修改后列表，再将结果赋值给 str_all_array
	contents.extend(str_all_array)
	str_all_array = contents

	# 通过回车将列表合并起来
	n = '\n'
	win.addToClipboard(n.join(str_all_array))

def changeTitleAndContents_Tier2():
	# 将得到的结果自动复制到剪贴板上
	# 本函数针对整个HTML代码
	# 包括前面目录部分自动添加链接
	# 后面标题部分自动添加标题样式以及锚点
	# 需要引用其他函数
	# 参数来自于剪切板复制
	"为“二级”标题添加特殊样式的 HTML 代码 —— title 为名称 —— index 为锚点名称"
	# 为Unicode编码，为了统一复制来的数据编码
	contents_t2 = [u'\n<ul>', u'\n<ul>', u'\n<ul>', u'\n<ul>', u'\n<ul>', u'\n<ul>', u'\n<ul>', u'\n<ul>']
	flag = [0, 0, 0, 0, 0, 0, 0, 0]

	# 需要调用里面关于剪切板的函数
	from win_diy import *
	str_all = win.getClipboard()
	str_all_array = str_all.splitlines()
	
	# 转换为 Unicode 编码才可以操作
	# 直接遍历查找<h2>
	
	# 为标题添加样式以及锚点
	i = 0
	# 存储二级标题的第一个数字
	num_1 = '0'
	for s in str_all_array:
		# 查找<h2>
		if s.find(u'<h2>') >= 0: 
			# 由于左侧可能有多余的标签，需要先查询"</"
			# 类型一：<h2>4.1 必备参数</h2>
			# 类型二：<h2><span style="font-size: 15px;"><strong>4.3 缺省参数</strong></span></h2>
			index_end = s.find(u'</')
			# 从右侧查询，终点为index_end
			index = s.rfind(u'>', 0, index_end) + 1
			title = s[index:index_end]
			# 获取标题的数字内容，例如"4.1 必备参数"获取4和1
			index_dot = title.find(u'.')
			index_space = title.find(u' ')
			num_1 = title[0:index_dot]
			num_2 = title[(index_dot+1):index_space]
			# 添加样式和锚点，命名规则"N_4_1"
			str_all_array[i] = '<div class="title_hh2"><a name="A_'+num_1+'_'+num_2+'"></a>' + title + '</div>'
			# 如果存在二级标题，则为flag赋值
			flag[int(num_1)] = 1
			# 添加Unicode编码字符，将目录内容叠加
			contents_t2[int(num_1)] = contents_t2[int(num_1)] +'\n<li><a href="#A_'+num_1+'_'+num_2+'">'+title+'</a></li>'
		i = i + 1

	# 将二级目录添加到代码中，通过数字进行迭代
	# 迭代flag为1的部分
	for f in range(0, len(flag)):
		if flag[f] == 1:
			contents_t2[f] = contents_t2[f] + '\n</ul>'
			i = 0
			for line in str_all_array:
				if line.find(u"#A0"+str(f)) >= 0:
					index = line.find(u"</li>")
					str_all_array[i] = line[0:index] + contents_t2[f] + "\n</li>"
					print str_all_array[i]
				i = i + 1

	# 通过回车将列表合并起来
	n = '\n'
	win.addToClipboard(n.join(str_all_array))

def fkNoLink():
	"添加绿色背景的方框，没有连接"
	from win_diy import *
	ss = win.getClipboard()
	ss = '<div class="fkNoLink">' + ss + '</div>' 
	win.addToClipboard(ss)

def restartArcpy():
	"重启ArcPy"
	import os
	import sys
	python = sys.executable
	os.execl(python, python, *sys.argv)

def func(param):
	"string"
	var0 = 'string'
	var1 = 'selected'
	var2 = list(None)

def changeTitle_Tier2():
	# 将得到的结果自动复制到剪贴板上
	# 本函数针对整个HTML代码
	# 包括前面目录部分自动添加链接
	# 后面标题部分自动添加标题样式以及锚点
	# 需要引用其他函数
	# 参数来自于剪切板复制
	# 1. 来源
	"为“二级”标题添加特殊样式的 HTML 代码 —— title 为名称 —— index 为锚点名称"

	# 需要调用里面关于剪切板的函数
	from win_diy import *
	str_all = win.getClipboard()
	str_all_array = str_all.splitlines()
	
	# 转换为 Unicode 编码才可以操作
	# 直接遍历查找<h2>
	
	# 为标题添加样式以及锚点
	i = 0
	# 存储二级标题的第一个数字
	num_1 = '0'
	for s in str_all_array:
		# 查找<h2>
		if s.find(u'<h2>') >= 0: 
			# 由于左侧可能有多余的标签，需要先查询"</"
			# 类型一：<h2>4.1 必备参数</h2>
			# 类型二：<h2><span style="font-size: 15px;"><strong>4.3 缺省参数</strong></span></h2>
			index_end = s.find(u'</')
			# 从右侧查询，终点为index_end
			index = s.rfind(u'>', 0, index_end) + 1
			title = s[index:index_end]
			
			# 添加样式
			str_all_array[i] = '<div class="title_hh2">' + title + '</div>'
		i = i + 1

	# 通过回车将列表合并起来
	n = '\n'
	win.addToClipboard(n.join(str_all_array))


def syntax_IDL_p():
	"将从IDL官网复制的语法文本修改"
	from win_diy import *
	ss = win.getClipboard()
	ss = ss.replace('Syntax', 'Syntax_IDL')
	ss = u'<p class="Syntax_IDL">' + ss + '</p>'
	ss = ss.replace("selected", "selected_IDL")
	ss = ss.replace("14px", "13px")
	win.addToClipboard(ss)
	return ss

def syntax_IDL_replace( string ):
	"将目标文本内容添加到代码中，注意我们的替换文本为“456852”"
	from win_diy import *
	ss = win.getClipboard()
	if u"456852" in ss:
		ss = ss.replace("456852", string)
		win.addToClipboard(ss)
		print "处理成功！"
	else:
		print "处理失败，检查是否增加“456852”"