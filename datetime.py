# -*-coding: utf-8 -*-

import re 
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str,tz_str):
    cday = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    t = tz_str.split("C")
    t2 = t[1].split(':')  
    hour = int(t2[0])  
    mine = int(t2[1])  
    #创建时区UTC时间  
    tz_utc = timezone(timedelta(hours=hour,minutes=mine))  
    #强制设置UTC时间  
    dt = cday.replace(tzinfo=tz_utc)  
    #返回timestamp时间  
    return dt.timestamp()  
  
if __name__ == "__main__":  
    t1 = to_timestamp('2015-6-1 08:10:30','UTC+7:00')  
    assert t1 == 1433121030.0 ,t1  
  
    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')  
    assert t2 == 1433121030.0 , t2  
  
    print('Pass')  