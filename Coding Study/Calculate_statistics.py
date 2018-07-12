# coding=utf-8
# 地点：国家海洋环境监测中心
# 作者：李炳南
# 时间：2017-12-07
# 说明：对于指定文件夹内部的所有 GeoTIFF 文件进行 Calculate Statistics 操作



import arcpy
import os

# 处理文件所在系的工作空间，即文件夹，注意反斜杠前面的“r”
arcpy.env.workspace = r"D:\01-Working\2017\20171204-IDL_Average\Final-CHL"

# 获取内部的栅格数据
files_raster = arcpy.ListRasters()

# 对数据进行遍历，并执行工具操作
for f in files_raster:
	print("-- Processing " + f)
	arcpy.CalculateStatistics_management(f)

print("")
print("------ Processing Completion ------")

# 用于暂停显示，否则窗体会一闪而过
os.system("pause")