# coding=utf-8
'''
批量出图：在python2.7中运行，如果arcpy显示没有导入，需要在设置里重新设置下arcgis的python
运行代码的时候，需要在outpicrure中放入模板
'''
import os
import arcpy
Path = u'H:/tianjin/out_picture'
RasterPath = u'H:/tianjin/out_pm25_month'
mxdName = u'天津pm25.mxd'
replaceLayerName = u'outPM25-201701-tif.tif'

arcpy.env.workspace = RasterPath
mxd = arcpy.mapping.MapDocument(os.path.join(Path,mxdName))
df = arcpy.mapping.ListDataFrames(mxd)[0]
layer = arcpy.mapping.ListLayers(mxd, replaceLayerName, df)[0] #用20090101_m.tif替换mxd里的图层
print (layer)
#标注
rasters = arcpy.ListRasters()
for raster in rasters:
    # 更新芳年的内容列表
    layer.replaceDataSource(RasterPath, 'RASTER_WORKSPACE', raster)#替换数据源中的栅格数据
    # if layer.symbologyType == 'GraduatedColorsSymbology':  # 分类

    arcpy.RefreshActiveView()  # 更新当前视图
    arcpy.RefreshTOC()
    layer.name = raster #把图层的名字替换成栅格的名字
    #textElement = arcpy.mapping.ListLayoutElements(mxd,'TEXT_ELEMENT','Month')[0]
    #textstr = raster[0:7]#提取数据年
    #textElement.text = str(int(textstr))
    # # Modify the image name
    # for element in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
    #     if element.name == "title":
    #         element.text = "{0}年{1}月{2}日PM2.5浓度".format(
    #             raster[8:12], raster[13:15], raster[14:16])
    arcpy.mapping.ExportToJPEG(mxd, os.path.join(Path, raster[0:17]), resolution = 300)#将mxd结果导出为jpg
    #resolution 分辨率
    #mxd.saveACopy(raster[0:7] + '.mxd')#将mxd保存
del mxd
print (rasters)




