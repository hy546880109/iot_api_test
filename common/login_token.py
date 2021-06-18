# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : Huny
# @Email : hy546880109@qq.com
# @date  : 2020.12.08
# @Project: 云平台接口测试用例

from pymysql import NULL
from config.config_test import Conf
import requests
import json
from common.mysql_data import Mysql_connet
url = Conf.TEST_URL.value

mysql = Mysql_connet('user')
in_mysql = mysql.select_sql('select is_delete from t_user where code="hy"') #数据库是逻辑删除，所以判断是否有删除标志位

if in_mysql is None:   #判断是否存在数据库
    mysql.insert_sql("INSERT INTO t_user(id,code,name,password,salt,level,phone,icon,email,is_delete,status,department_id,province_id,province_name,city_id,city_name,area_id,area_name,last_login_time,create_at,create_by,update_at,update_by,remark,jpush_id) VALUES\
(1234567890,'hy','黄先春','2bd8934d1902b74caa2ce4f77bb84812','c0ae9feb',1,'180358812635','https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/87fef3cda6e14762a572e4022a017a97.jpg','huang_xc@sohu.com',0,0,1382562817882931201,43,'湖南',4311,'永州',431129,'江华瑶族自治县','2021-06-03 09:15:10','2021-03-31 09:45:43',NULL,'2021-05-14 17:16:16',NULL,NULL,NULL)")

code = mysql.select_sql('select code from t_user where code="hy"')

payload = {
    "code": code,
    # "code": 'admin',
    "password": "e10adc3949ba59abbe56e057f20f883e",
    "validateCode": 'code'  # 暂时屏蔽验证码用来测试
}
headers = {'Content-Type': 'application/json'}
payload = json.dumps(payload)
url = url + '/login'


def get_token():
    res = requests.post(url, data=payload, headers=headers)
    token = res.json()['data']['token']
    return token

mysql.close()

if __name__ == '__main__':
    print('url:', url)
    print('data:', payload)
    print(get_token())
