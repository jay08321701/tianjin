import pandas
import utils_arcpy.funcs as py2func
import datetime
from multiprocessing.pool import ThreadPool
if __name__ == '__main__':
    make_date = datetime.date(2022, 11, 2)  # 制作时间
    data_date = datetime.date(2022, 11, 1)  # 数据时间
    py2func._py2exe = r"C:\Python27\ArcGIS10.7"  # python解释器路径
    pic_params_list = [
        {
        {
            "mxd_path": "./天津pm10.mxd",
            "png_path": "./1_png/天津市PM10.png",
            "layers": {
                "PM10_20211002_tif.tif": r"./2021年10月至2022年6月日均值/PM10_20211003_tif.tif",
            },
            "texts": {
                "MakeTime": f"制作时间：{make_date.year}年{make_date.month}月{make_date.day}日",
                "PicTitle": f"{data_date.year}年{data_date.month}月{data_date.day}日PM10柱浓度",
            },
            "png_dpi": 300,
        },
        {
            "mxd_path": "./天津pm2.5.mxd",
            "png_path": "./1_png/天津市PM2.5.png",
            "layers": {
                "PM25_20211002_tif.tif": r"./2021年10月至2022年6月日均值/PM25_20211003_tif.tif",
            },
            "texts": {
                "MakeTime": f"制作时间：{make_date.year}年{make_date.month}月{make_date.day}日",
                "PicTitle": f"{data_date.year}年{data_date.month}月{data_date.day}日PM2.5柱浓度",
            },
            "png_dpi": 300,
        },

        },
    ]
    # 多线程
    with ThreadPool(4) as p:
        p.map(py2func.mxd2png, pic_params_list)
    # 顺序进行
    # for params in pic_params_list:
        # py2func.mxd2png(params)
