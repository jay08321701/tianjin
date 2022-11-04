import utils_arcpy.funcs as py2func
import datetime
from multiprocessing.pool import ThreadPool

if __name__ == '__main__':
    make_date = datetime.date(2022, 7, 25)  # 制作时间
    data_date = datetime.date(2022, 7, 24)  # 数据时间
    py2func._py2exe = r"D:\Program Files\ArcGIS10.6\python.exe"  # python解释器路径

    pic_params_list = [
        {
            "mxd_path": "./成都NO2.mxd",
            "png_path": "./1_png/成都市NO2.png",
            "layers": {
                "NO2_20220704_tif.tif": r"./0_tif/NO2_20220724_tif.tif",
            },
            "texts": {
                "MakeTime": f"制作时间：{make_date.year}年{make_date.month}月{make_date.day}日",
                "PicTitle": f"{data_date.year}年{data_date.month}月{data_date.day}日NO<sub>2</sub>柱浓度",
            },
            "png_dpi": 300,
        },
        {
            "mxd_path": "./成都HCHO.mxd",
            "png_path": "./1_png/成都市HCHO.png",
            "layers": {
                "HCHO_20220705_lowpass_999.tif": r"./0_tif/HCHO_20220724_lowpass_999.tif",
            },
            "texts": {
                "MakeTime": f"制作时间：{make_date.year}年{make_date.month}月{make_date.day}日",
                "PicTitle": f"{data_date.year}年{data_date.month}月{data_date.day}日HCHO柱浓度",
            },
            "png_dpi": 300,
        },
        {
            "mxd_path": "./天津pm10.mxd",
            "png_path": "./1_png/天津市PM10.png",
            "layers": {
                "HCHO_20220705_lowpass_999.tif": r"./0_tif/HCHO_20220724_lowpass_999.tif",
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
                "HCHO_20220705_lowpass_999.tif": r"./0_tif/HCHO_20220724_lowpass_999.tif",
            },
            "texts": {
                "MakeTime": f"制作时间：{make_date.year}年{make_date.month}月{make_date.day}日",
                "PicTitle": f"{data_date.year}年{data_date.month}月{data_date.day}日PM2.50柱浓度",
            },
            "png_dpi": 300,
        },
        {
            "mxd_path": "./成都ratio.mxd",
            "png_path": "./1_png/成都市ratio.png",
            "layers": {
                "ratio_20220704_tif.tif": r"./0_tif/ratio_20220724_tif.tif",
            },
            "texts": {
                "MakeTime": f"制作时间：{make_date.year}年{make_date.month}月{make_date.day}日",
                "PicTitle": f"{data_date.year}年{data_date.month}月{data_date.day}日HCHO/NO<sub>2</sub>",
            },
            "png_dpi": 300,
        },
        {
            "mxd_path": "./成都O3.mxd",
            "png_path": "./1_png/成都市O3.png",
            "layers": {
                "O3_predict_20220704.tif": r"./0_tif/O3_predict_20220724.tif",
            },
            "texts": {
                "MakeTime": f"制作时间：{make_date.year}年{make_date.month}月{make_date.day}日",
                "PicTitle": f"{data_date.year}年{data_date.month}月{data_date.day}日近地面O<sub>3</sub>柱浓度",
            },
            "png_dpi": 300,
        },
    ]
    # 多线程
    with ThreadPool(4) as p:
        p.map(py2func.mxd2png, pic_params_list)
    # 顺序进行
    # for params in pic_params_list:
        # py2func.mxd2png(params)
