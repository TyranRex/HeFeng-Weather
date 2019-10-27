import requests
import json
import time
# 邮件发送神器
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send(msg):
    str1='successful.'
    str2='failure'

    # 第三方smtp服务 :qq 邮箱
    mail_host="smtp.qq.com"  # 端口号： 465
    send_user="sender e-mail@qq.com"  # 发送者的邮箱地址
    send_pass="****rzgllihjz****"  # 口令
    rec_user="****878****@qq.com" # 收件者邮箱
    aluo="****7009***@qq.com" # -- 接收者邮箱

    message=MIMEText(msg,'plain','utf-8')
    message['from']=Header(send_user,'utf-8')
    message['to']=Header(rec_user,'utf-8')

    subject='今日份天气预报'
    message['Subject']=Header(subject,'utf-8')

    try:
        smtpObj=smtplib.SMTP_SSL(mail_host,465)
        smtpObj.login(send_user,send_pass)
        smtpObj.sendmail(send_user,rec_user,message.as_string())
        smtpObj.sendmail(send_user, aluo, message.as_string())
        print(str1+'\tThank you!')
    except smtplib.SMTPException:
        print(str2+'\tOh! No')



# 获取今天当前部分信息数据
def now_weather():
    url=url='https://free-api.heweather.net/s6/weather/now?key=fa73cb53a3e1430c9862a91302fd54c9&location=%E6%98%86%E6%98%8E'
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    now_res=requests.get(url,headers=header)
    now_res_json=now_res.json()

    # 实际天气温度
    real_tmp=now_res_json['HeWeather6'][0]['now']['tmp']
    # 体感温度
    feel_tmp=now_res_json['HeWeather6'][0]['now']['fl']

    # 获取信息返回
    return real_tmp,feel_tmp

def now_and_future_twodays_weather():
    # 今天
    now_weathers=[]
    # 明天天气预测
    tomorrow_weather=[]
    # 后天天气预测
    the_day_after_tomorrow_weather=[]

    url = 'https://free-api.heweather.net/s6/weather/forecast?key=fa73cb53a3e1430c9862a91302fd54c9&location=%E6%98%86%E6%98%8E'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    forecast_res = requests.get(url, headers=header)
    forecast_res_json = forecast_res.json()
    # print(forecast_res_json)
    ############################################################
    # 公共信息 头部
    ############################################################
    # 国家 省份 地区 纬度 经度 当地天气更新时间 状态信息
    country = forecast_res_json['HeWeather6'][0]['basic']['cnty']
    province = forecast_res_json['HeWeather6'][0]['basic']['admin_area']
    city_name = forecast_res_json["HeWeather6"][0]["basic"]["location"]
    lat = forecast_res_json['HeWeather6'][0]['basic']['lat']
    lon = forecast_res_json['HeWeather6'][0]['basic']['lon']
    local_update_weather_time = forecast_res_json['HeWeather6'][0]['update']['loc']
    status = forecast_res_json['HeWeather6'][0]['status']
    ###########################################################

    ###########################################################
    # 获取常规天气信息
    # daily_forecast 是一个列表结构，分别取出里面的元素，即可进行分析
    daily_forecast=forecast_res_json['HeWeather6'][0]['daily_forecast']

    # 得到今日份天气信息
    now_weathers=daily_forecast[0]
    # 获取日期
    now_date=now_weathers['date']
    # 获取今日份天气状态信息-- 白天
    now_cond_txt_d=now_weathers['cond_txt_d']
    # 获取日出 紫外线强度 日落 月出 月落 时间
    now_sr=now_weathers['sr']
    now_uv_index=now_weathers['uv_index']
    now_ss=now_weathers['ss']
    now_mr=now_weathers['mr']
    now_ms=now_weathers['ms']
    # 获取今日份天气状态信息-- 晚上
    now_cond_txt_n=now_weathers['cond_txt_n']

    # 最高温 最低温 当前温度 体感温度 相对湿度
    now_tmp_max=now_weathers['tmp_max']
    now_tmp_min=now_weathers['tmp_min']
    now_hum=now_weathers['hum']

    # 风向 风力 风速  降雨量 降雨概率
    now_wind_dir=now_weathers['wind_dir']
    now_wind_sc=now_weathers['wind_sc']
    now_wind_spd=now_weathers['wind_spd']
    now_pcpn=now_weathers['pcpn']
    now_pop=now_weathers['pop']


    # 获取明天的天气预报信息
    tomorrow_weather=daily_forecast[1]
    # 获取日期
    tomorrow_date = tomorrow_weather['date']

    # 获取今日份天气状态信息-- 白天
    tomorrow_cond_txt_d = tomorrow_weather['cond_txt_d']
    # 获取日出 紫外线强度 日落 月出 月落 时间
    tomorrow_sr = tomorrow_weather['sr']
    tomorrow_uv_index = tomorrow_weather['uv_index']
    tomorrow_ss = tomorrow_weather['ss']
    tomorrow_mr = tomorrow_weather['mr']
    tomorrow_ms = tomorrow_weather['ms']
    # 获取今日份天气状态信息-- 晚上
    tomorrow_cond_txt_n = tomorrow_weather['cond_txt_n']

    # 最高温 最低温 当前温度 体感温度 相对湿度
    tomorrow_tmp_max = tomorrow_weather['tmp_max']
    tomorrow_tmp_min = tomorrow_weather['tmp_min']
    tomorrow_hum = tomorrow_weather['hum']

    # 风向 风力 风速  降雨量 降雨概率
    tomorrow_wind_dir = tomorrow_weather['wind_dir']
    tomorrow_wind_sc = tomorrow_weather['wind_sc']
    tomorrow_wind_spd = tomorrow_weather['wind_spd']
    tomorrow_pcpn = tomorrow_weather['pcpn']
    tomorrow_pop = tomorrow_weather['pop']


    # 获取后天的天气预报信息
    the_day_after_tomorrow_weather=daily_forecast[2]
    # 获取日期
    the_day_after_tomorrow_date = the_day_after_tomorrow_weather['date']

    # 获取今日份天气状态信息-- 白天
    the_day_after_tomorrow_cond_txt_d = the_day_after_tomorrow_weather['cond_txt_d']
    # 获取日出 紫外线强度 日落 月出 月落 时间
    the_day_after_tomorrow_sr = the_day_after_tomorrow_weather['sr']
    the_day_after_tomorrow_uv_index = the_day_after_tomorrow_weather['uv_index']
    the_day_after_tomorrow_ss = the_day_after_tomorrow_weather['ss']
    the_day_after_tomorrow_mr = the_day_after_tomorrow_weather['mr']
    the_day_after_tomorrow_ms = the_day_after_tomorrow_weather['ms']
    # 获取今日份天气状态信息-- 晚上
    the_day_after_tomorrow_cond_txt_n = the_day_after_tomorrow_weather['cond_txt_n']

    # 最高温 最低温 当前温度 体感温度 相对湿度
    the_day_after_tomorrow_tmp_max = the_day_after_tomorrow_weather['tmp_max']
    the_day_after_tomorrow_tmp_min = the_day_after_tomorrow_weather['tmp_min']
    the_day_after_tomorrow_hum = the_day_after_tomorrow_weather['hum']

    # 风向 风力 风速  降雨量 降雨概率
    the_day_after_tomorrow_wind_dir = the_day_after_tomorrow_weather['wind_dir']
    the_day_after_tomorrow_wind_sc = the_day_after_tomorrow_weather['wind_sc']
    the_day_after_tomorrow_wind_spd = the_day_after_tomorrow_weather['wind_spd']
    the_day_after_tomorrow_pcpn = the_day_after_tomorrow_weather['pcpn']
    the_day_after_tomorrow_pop = the_day_after_tomorrow_weather['pop']

    # 获取的数据返回
    return country, province, city_name, lat, lon, local_update_weather_time, status, \
           now_date,now_cond_txt_d,now_sr,now_uv_index,now_ss,now_mr,now_ms,now_cond_txt_n, \
           now_tmp_max,now_tmp_min,now_hum,now_wind_dir,now_wind_sc,now_wind_spd,now_pcpn,now_pop,\
           tomorrow_date,tomorrow_cond_txt_d,tomorrow_sr,tomorrow_uv_index,tomorrow_ss,tomorrow_mr,tomorrow_ms,tomorrow_cond_txt_n,\
           tomorrow_tmp_max,tomorrow_tmp_min,tomorrow_hum,tomorrow_wind_dir,tomorrow_wind_sc,tomorrow_wind_spd,tomorrow_pcpn,tomorrow_pop,\
           the_day_after_tomorrow_date,the_day_after_tomorrow_cond_txt_d,the_day_after_tomorrow_sr,the_day_after_tomorrow_uv_index,the_day_after_tomorrow_ss,\
           the_day_after_tomorrow_mr,the_day_after_tomorrow_ms,the_day_after_tomorrow_cond_txt_n,the_day_after_tomorrow_tmp_max,the_day_after_tomorrow_tmp_min,\
           the_day_after_tomorrow_hum,the_day_after_tomorrow_wind_dir,the_day_after_tomorrow_wind_sc,the_day_after_tomorrow_wind_spd,the_day_after_tomorrow_pcpn,the_day_after_tomorrow_pop

def main(tm_hour,tm_min):
    #获取 now_weather() 函数的返回值
    real_tmp, feel_tmp=now_weather()

    #获取 now_and_future_twodays_weather() 函数的所有返回值
    country, province, city_name, lat, lon, local_update_weather_time, status, \
    now_date,now_cond_txt_d,now_sr,now_uv_index,now_ss,now_mr,now_ms,now_cond_txt_n, \
    now_tmp_max,now_tmp_min,now_hum,now_wind_dir,now_wind_sc,now_wind_spd,now_pcpn,now_pop,\
    tomorrow_date,tomorrow_cond_txt_d,tomorrow_sr,tomorrow_uv_index,tomorrow_ss,tomorrow_mr,tomorrow_ms,tomorrow_cond_txt_n,\
    tomorrow_tmp_max,tomorrow_tmp_min,tomorrow_hum,tomorrow_wind_dir,tomorrow_wind_sc,tomorrow_wind_spd,tomorrow_pcpn,tomorrow_pop,\
    the_day_after_tomorrow_date,the_day_after_tomorrow_cond_txt_d,the_day_after_tomorrow_sr,the_day_after_tomorrow_uv_index,the_day_after_tomorrow_ss,\
    the_day_after_tomorrow_mr,the_day_after_tomorrow_ms,the_day_after_tomorrow_cond_txt_n,the_day_after_tomorrow_tmp_max,the_day_after_tomorrow_tmp_min,\
    the_day_after_tomorrow_hum,the_day_after_tomorrow_wind_dir,the_day_after_tomorrow_wind_sc,the_day_after_tomorrow_wind_spd,the_day_after_tomorrow_pcpn,\
    the_day_after_tomorrow_pop=now_and_future_twodays_weather()

    #邮件消息构建
    msg='地区：'+country+province+city_name+'\n'+'经度：'+lon+'\n'+'纬度：'+lat+'\n'+'当前天气信息更新时间：\n'+local_update_weather_time+'\n消息发送时间：'+str(tm_hour)+':'+str(tm_min)+'\n状态：'+status+'\n=======================\n'+ \
        '以下是今日份信息：\n'+'日期：'+now_date+'\n白天天气状态：'+now_cond_txt_d+'\n日出：'+now_sr+'\n紫外线强度：'+now_uv_index+'\n最高气温：'+now_tmp_max+'\n最低气温：'+now_tmp_min+'\n'+ \
        '真实温度：'+real_tmp+'\n体感温度：'+feel_tmp+'\n相对湿度：'+now_hum+'\n风向：'+now_wind_dir+'\n风力：'+now_wind_sc+'\n风速：'+now_wind_spd+'\n是否有雨：'+now_pcpn+'\n下雨概率(百分制)：'+now_pop+'\n'+ \
        '日落：'+now_ss+'\n月升：'+now_mr+'\n夜间天气状况：'+now_cond_txt_n+'\n月落：'+now_ms+'\n======================='+'\nEvery day is beautiful, just enjoy it!'+'\n----From a warm Bear！'

    return msg

def get_time():
    tim=time.localtime(time.time())
    tm_hour=tim[3]
    tm_min=tim[4]
    return tm_hour,tm_min


if __name__=="__main__":
    print('waiting... ...')
    #while True:
    tm_hour, tm_min = get_time()
    msg = main(tm_hour,tm_min)
       # if tm_hour==23 and tm_min==20:
    send(msg)
        #    time.sleep(60*60)
	#	else:
     #       continue
        #elif tm_hour==11 and tm_min==45:
         #   send(msg)
          #  time.sleep(60*60)
			#
            #exit(10)
