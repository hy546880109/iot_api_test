import pymysql
import json

def mysql_con(host,port,user,password,db):
    pymysql.connect(host=host, port=port, user=user, password=password, db=db)


def insert_sql(db):
    mysql_conn = pymysql.connect(host='139.159.202.43', port=3306, user='root', password='Antian!2020', db=db)
    sql = "insert into t_user (id,code,passwd) values ()"
    try:
        with mysql_conn.cursor() as cursor:
            cursor.execute(sql)
            mysql_conn.commit()
    except Exception as e:
        mysql_conn.rollback()


def delete_sql(db):
    mysql_conn = pymysql.connect(host='139.159.202.43', port=3306, user='root', password='Antian!2020', db=db)
    sql = "delete from t_user where id == ''"
    try:
        with mysql_conn.cursor() as cursor:
            cursor.execute(sql)
            mysql_conn.commit()
    except Exception as e:
        mysql_conn.rollback()


def select_sql(db,name,table):
    mysql_conn = pymysql.connect(host='139.159.202.43', port=3306, user='root', password='Antian!2020', db=db)
    sql = "select {} from {}".format(name,table)
    try:
        with mysql_conn.cursor() as cursor:
            cursor.execute(sql)
            mysql_conn.commit()
            result = cursor.fetchall()
            data_list = []
            for js in result:
                data = {'code': js[0]}
                data_list.append(data)
            # list = json.dumps(list)
            # print(list[1]['code'])
            return data_list

    except Exception as e:
        mysql_conn.rollback()
    mysql_conn.close()


if __name__ == "__main__":
    q = select_sql('user','code','t_user')
    print(q)
