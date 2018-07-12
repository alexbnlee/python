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
		
	win.addToClipboard(ss)
	print ss
	return ss

def changeTitle():
	# 将得到的结果自动复制到剪贴板上
	# 本函数针对整个HTML代码
	# 包括前面目录部分自动添加链接
	# 后面标题部分自动添加标题样式以及锚点
	# 需要引用其他函数
	# 参数来自于剪切板复制
	"为标题添加特殊样式的 HTML 代码 —— title 为名称 —— index 为锚点名称"
	# 需要调用里面关于剪切板的函数
	from win_diy import *
	str_all = win.getClipboard()
	str_all_array = str_all.splitlines()
	# 查找相关标题指示
	num_CHN = ['一、', '二、', '三、', '四、', '五、', '六、', '七、', '八、']   
	
	# 查找其所在行，并判断不是目录，进行行的替换
	# 转换为 Unicode 编码才可以操作
	# 对于大写数字进行遍历，进行查找
	for num in num_CHN:
		# 为标题添加样式以及锚点
		i = 0
		for s in str_all_array:
			index = s.find(num.decode('utf-8'))
			if index >= 0:
				# 如果不含有<li>，说明不是目录内容，引用样式函数，需要将汉字提取
				if s.find(u'<li>') < 0: 
					index_end = s.find(u'</', index)
					title = s[index:index_end]
					str_all_array[i] = getTitleByNum(title)
				else:
					# 带有<li>为目录，为目录添加链接地址
					str_all_array[i] = contentAnchor(s)

			i = i + 1

	# 通过回车将列表合并起来
	n = '\n'
	win.addToClipboard(n.join(str_all_array))

def changeTitleAndContents():
	# 将得到的结果自动复制到剪贴板上
	# 本函数针对整个HTML代码
	# 包括前面目录部分自动添加 目录 & 链接
	# 后面标题部分自动添加标题样式以及锚点
	# 需要引用其他函数
	# 参数来自于剪切板复制
	# 标题特点，以大写数字+顿号开头
	"为标题添加特殊样式、添加目录、为目录添加链接 的 HTML 代码（针对没有添加目录的源码）"
	
	# 为Unicode编码，为了统一复制来的数据编码
	contents = [u'<p>目录：</p>', u'<ul>']

	# 需要调用里面关于剪切板的函数
	from win_diy import *
	str_all = win.getClipboard()
	str_all_array = str_all.splitlines()
	# 查找相关标题指示
	num_CHN = ['一、', '二、', '三、', '四、', '五、', '六、', '七、', '八、']   
	
	# 查找其所在行
	# 转换为 Unicode 编码才可以操作
	# 对于大写数字进行遍历，进行查找
	for num in num_CHN:
		# 为标题添加样式以及锚点
		i = 0
		for s in str_all_array:
			index = s.find(num.decode('utf-8'))
			if index >= 0:
				# 如果不含有<li>，说明不是目录内容，引用样式函数，需要将汉字提取
				if s.find(u'<li>') < 0: 
					index_end = s.find(u'</', index)
					title = s[index:index_end]
					str_all_array[i] = getTitleByNum(title)
					# 添加Unicode编码字符，将目录内容叠加
					contents.append(contentAnchor(u'<li>' + title + '</li>'))
			i = i + 1

	# 最后叠加结尾部分
	contents.append(u'</ul>')
	# 将目录内容后面叠加原修改后列表，再将结果赋值给 str_all_array
	contents.extend(str_all_array)
	str_all_array = contents

	# 通过回车将列表合并起来
	n = '\n'
	win.addToClipboard(n.join(str_all_array))


