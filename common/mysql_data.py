import pymysql
import json


host = '139.159.202.43'
port = 3306
user = 'root'
password = 'Antian!2020'
db = 'user'

class Mysql_connet():
    def __init__(self):
        self.mysql_conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db)


    def insert_sql(self,table):
        mysql_conn = self.mysql_conn
        sql = "insert into t_user (id,code,passwd) values ()"
        try:
            with mysql_conn.cursor() as cursor:
                cursor.execute(sql)
                mysql_conn.commit()
        except Exception as e:
            mysql_conn.rollback()


    def delete_sql(self,table):
        mysql_conn = self.mysql_conn
        sql = "delete from t_user where id == ''"
        try:
            with mysql_conn.cursor() as cursor:
                cursor.execute(sql)
                mysql_conn.commit()
        except Exception as e:
            mysql_conn.rollback()


    def select_sql(self,name,table):
        mysql_conn = self.mysql_conn
        sql = "select {} from {}".format(name,table)
        try:
            with mysql_conn.cursor() as cursor:
                cursor.execute(sql)
                mysql_conn.commit()
                # result = cursor.fetchall()
                result = cursor.fetchone()
                result = result[0]
                # data_list = []
                # for js in result:
                #     data = {'code': js[0]}
                #     data_list.append(data)
                # list = json.dumps(list)
                # print(list[1]['code'])
                # return data_list
                return result

        except Exception as e:
            mysql_conn.rollback()
        mysql_conn.close()


if __name__ == "__main__":
    q = Mysql_connet()
    s = q.select_sql('code','t_user')
    print(s)
