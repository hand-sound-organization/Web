import csv

# 获取ｊｓｏｎ数据
import json
from app import db
from models import CityHeatMap
from datetime import datetime

if __name__ == '__main__':
    # 把热力图数据写入数据库##################
    with open('HeatdataJson.txt', 'r') as jsonfile:
        jsondata = json.load(jsonfile)
        for heatpoint in jsondata:
            newPoint = CityHeatMap(lng=heatpoint["lng"], lat=heatpoint["lat"], count=heatpoint["count"],
                                   time=datetime.now())
            db.session.add(newPoint)
        db.session.commit()
        db.session.close()

    #######################################
    # 创建热力图数据csv文件##################
    #     print(jsondata)
    #     # # 创建文件对象
    #     with open('Heatdata.csv', 'w') as csvfile:
    #         # # 通过文件创建csv对象
    #         csv_write = csv.writer(csvfile)
    #
    #         # writerow: 按行写入，　writerows: 是批量写入
    #         # 写入数据 取列表的第一行字典，用字典的ｋｅｙ值做为头行数据
    #         csv_write.writerow(jsondata[0].keys())
    #
    #         # 循环里面的字典，将value作为数据写入进去
    #         for data in jsondata:
    #             csv_write.writerow(data.values())
    #######################################
