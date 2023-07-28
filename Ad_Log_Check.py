import pandas as pd
from datetime import datetime
import os


def file_check(filepath):
    if not os.path.isfile(filepath):
        print("檔案不存在: " + filepath)


if __name__ == '__main__':
    root = "./"
    cam_list = ["cam1_2_playlog"]
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")
    print("目前時間: " + time_now)
    date_slash_type = datetime.now().strftime("%Y/%m/%d")
    # print(date_slash_type)
    # 設定起訖日期DatePeriod = pd.date_range("2019/1/1", "2019/1/3", freq='D')
    DatePeriod = pd.date_range("2023/7/4", date_slash_type, freq='D')
    # 將DatePeriod格式化成像要的格式，以及最重要的把時間由index改為string
    dp_concat = DatePeriod.strftime('%Y%m%d')
    dp_dash = DatePeriod.strftime('%Y-%m-%d')

    for cam in cam_list:
        for dir_str, file_str in zip(dp_concat, dp_dash):
            path = f"{root}{cam}/{dir_str}/{file_str}.csv"
            # print(path)
            file_check(path)
