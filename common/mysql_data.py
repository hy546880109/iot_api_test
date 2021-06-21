import pymysql
import json


host = '139.159.202.43'
port = 3306
user = 'root'
password = 'Antian!2020'


class Mysql_connet():
    def __init__(self,db):
        self.mysql_conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db)


    def insert_sql(self,sql):
        mysql_conn = self.mysql_conn
        # sql = "insert into t_user (id,code,passwd) values ()"
        try:
            with mysql_conn.cursor() as cursor:
                mysql_conn.ping(reconnect=True)
                cursor.execute(sql)
                mysql_conn.commit()

        except Exception as e:
            mysql_conn.rollback()
        mysql_conn.close()

    def delete_sql(self,sql):
        mysql_conn = self.mysql_conn
        # sql = "delete from t_user where id == ''"
        try:
            with mysql_conn.cursor() as cursor:
                mysql_conn.ping(reconnect=True)
                cursor.execute(sql)
                mysql_conn.commit()
            
        except Exception as e:
            mysql_conn.rollback()
        mysql_conn.close()

    def select_sql(self,sql):
        mysql_conn = self.mysql_conn
        # sql = "select {} from {}".format(name,table)
        try:
            with mysql_conn.cursor() as cursor:
                mysql_conn.ping(reconnect=True)
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


    def update_sql(self,sql):
        mysql_conn = self.mysql_conn
        try:
            with mysql_conn.cursor() as cursor:
                mysql_conn.ping(reconnect=True)
                cursor.execute(sql)
                mysql_conn.commit()
            
        except Exception as e:
            mysql_conn.rollback()
        mysql_conn.close()
        

    def close(self):
        mysql_conn = self.mysql_conn
        mysql_conn.cursor().close()
        mysql_conn.close()


if __name__ == "__main__":
    q = Mysql_connet('user')  
    s = q.select_sql('select * from t_user where code="hy"')
    print(s)
