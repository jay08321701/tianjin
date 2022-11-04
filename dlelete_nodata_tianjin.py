#-*- encoding:utf-8 -*-
import sys   #reload()之前必须要引入模块
reload(sys)
sys.setdefaultencoding('utf-8')
import arcpy, datetime
'''
批量删除tiff的无效值，此代码已跑通
'''
# 这里使用的方法为“复制栅格”
# tif影像输入路径
tif_file_path = "H:/tianjin/pm10_month"
# 结果输出路径
out_file_path = "H:/tianjin/out"
arcpy.env.workspace = tif_file_path

# 开始计算时间
startTime = datetime.datetime.now()
print startTime

# 遍历工作空间下的所有tif影像
tif_file_name = arcpy.ListRasters("*", "tif")
for tif_file in tif_file_name:
    print(tif_file)
    Cope_file_name = tif_file
    # 执行Cope Raster
    arcpy.CopyRaster_management(tif_file, out_file_path + Cope_file_name,
                                           "DEFAULTS", "0", "nodata", "", "", "8_BIT_UNSIGNED")

print "Finish!"
endTime = datetime.datetime.now()
print "Time use: " + str((endTime - startTime).seconds) + " (second)"
print "-----------------------------------------------------------"