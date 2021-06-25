import pymysql
import json
import random
import faker

host = '139.159.202.43'
port = 3306
user = 'root'
password = 'Antian!2020'

faker = faker.Faker(locale='zh_CN')


class Mysql_connet():
    def __init__(self, db):
        self.mysql_conn = pymysql.connect(
            host=host, port=port, user=user, password=password, db=db)

    def insert_sql(self, sql):
        mysql_conn = self.mysql_conn
        try:
            with mysql_conn.cursor() as cursor:
                mysql_conn.ping(reconnect=True)
                cursor.execute(sql)
                mysql_conn.commit()

        except Exception as e:
            mysql_conn.rollback()
        mysql_conn.close()

    def delete_sql(self, sql):
        mysql_conn = self.mysql_conn
        try:
            with mysql_conn.cursor() as cursor:
                mysql_conn.ping(reconnect=True)
                cursor.execute(sql)
                mysql_conn.commit()

        except Exception as e:
            mysql_conn.rollback()
        mysql_conn.close()

    def select_sql(self, sql):
        mysql_conn = self.mysql_conn
        try:
            with mysql_conn.cursor() as cursor:
                mysql_conn.ping(reconnect=True)
                cursor.execute(sql)
                mysql_conn.commit()
                result = cursor.fetchone()
                result = result[0]
                return result

        except Exception as e:
            mysql_conn.rollback()
        mysql_conn.close()

    def update_sql(self, sql):
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


class Mysql_data(Mysql_connet):
    def __init__(self):

        self.user_id = faker.random_number(20)
        self.department_id = faker.random_number(20)
        self.role_id = faker.random_number(20)
        self.device_id = faker.random_number(20)
        self.no = faker.random_number(20)
        self.terminal_no = faker.random_number(20)
        self.user_role_id = faker.random_number(20)
        self.role_menu_id = faker.random_number(20)
        self.menu_id = faker.random_number(20)
        self.capital_id = faker.random_number(20)
        self.alarm_id = faker.random_number(20)
        self.work_order_id = faker.random_number(20)
        self.task_id = faker.random_number(20)
        self.capital_id = faker.random_number(20)

    def insert_user(self):
        self.mysql_conn = Mysql_connet('user')
        self.mysql_conn.insert_sql("insert  into `t_department`(`id`,`name`,`pid`,`province_id`,`province_name`,`city_id`,`city_name`,`area_id`,`area_name`,`remark`,`is_delete`,`create_at`,`create_by`,`update_at`,`update_by`) values \
        ({},'移动部门',0,11,'北京',1101,'北京市辖',110101,'东城区','in ut qui cillum veniam',0,'2021-04-15 13:13:57',NULL,'2021-06-08 18:02:27',NULL)".format(self.department_id))
        self.mysql_conn.insert_sql("insert  into `t_user`(`id`,`code`,`name`,`password`,`salt`,`level`,`phone`,`icon`,`email`,`is_delete`,`status`,`department_id`,`province_id`,`province_name`,`city_id`,`city_name`,`area_id`,`area_name`,`last_login_time`,`create_at`,`create_by`,`update_at`,`update_by`,`remark`,`jpush_id`) values \
        ({},'hy','黄先春','2bd8934d1902b74caa2ce4f77bb84812','c0ae9feb',1,'180358812635','https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/87fef3cda6e14762a572e4022a017a97.jpg','huang_xc@sohu.com',0,0,{},43,'湖南',4311,'永州',431129,'江华瑶族自治县','2021-06-03 09:15:10','2021-03-31 09:45:43',NULL,'2021-05-14 17:16:16',NULL,NULL,NULL)".format(self.user_id, self.department_id))
        self.mysql_conn.insert_sql("INSERT INTO `t_user_role` VALUES ({}, {}, {})".format(
            self.user_role_id, self.role_id, self.user_id))
        self.mysql_conn.insert_sql(
            "INSERT INTO `t_role` VALUES ({}, '普通管理员', '普通管理员', 0, '2021-06-24 09:21:03', 1377074593995628546, '2021-06-24 09:22:11', NULL)".format(self.role_id))
        self.mysql_conn.insert_sql("INSERT INTO `t_role_menu` VALUES ({}, {}, 10)".format(
            self.role_menu_id, self.role_id))

    def delete_user(self):
        self.mysql_conn = Mysql_connet('user')
        self.mysql_conn.insert_sql(
            "delete from t_department where id={}".format(self.department_id))
        self.mysql_conn.insert_sql(
            "delete from t_role where id={}".format(self.role_id))
        self.mysql_conn.insert_sql(
            "delete from t_role_menu where id={}".format(self.role_menu_id))
        self.mysql_conn.insert_sql(
            "delete from t_user where where id={}".format(self.user_id))
        self.mysql_conn.insert_sql(
            "delete from t_user_role where id={}".format(self.user_role_id))

    def insert_device(self):
        self.mysql_conn = Mysql_connet('device')
        self.mysql_conn.insert_sql("INSERT  INTO `t_cellar_well`(`id`,`no`,`terminal_no`,`province_id`,`province_name`,`city_id`,`city_name`,`area_id`,`area_name`,`address`,`spec`,`department_id`,`department_name`,`type`,`sub_type`,`cover_type`,`is_online`,`control_status`,`status`,`is_delete`,`create_at`,`create_by`,`update_at`,`longitude`,`latitude`) VALUES\
        ({},{},{},44,'广东省',4403,'深圳市',440303,'南山区','大新路南头街道88-36号','1',1382562817882931201,'b',0,1,1,1,1,0,0,'2021-06-09 10:21:29',NULL,NULL,'113.93109','22.54901')".format(self.device_id, self.no, self.terminal_no))
        self.mysql_conn.insert_sql("INSERT INTO `t_capital` VALUES ({}, {}, 0, {}, '系统', '', '', NULL, NULL, NULL, 0, NULL, '2021-06-11 17:44:36', NULL, NULL)".format(
            self.capital_id, self.terminal_no, self.department_id))
        self.mysql_conn.insert_sql("INSERT INTO `t_images` VALUES (1403287037510955009, {}, 0, 'https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/7b6cbc69d2324e83bac5bb8b08090440.jpg', 'https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/f9ffa1050a884c1f990803e07b92b16d.jpg', 'https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/5e665f4c55f24b1d944f42b7b61a0fa7.jpg', NULL, 0)".format(self.terminal_no))
        self.mysql_conn.insert_sql("INSERT INTO `t_cellar_well_terminal` VALUES (1403287037427068930, {}, {}, 'ZK-PCB-210507', 'ZK-20210611.1', '95', '27', '0', 0, 1, 0, NULL, NULL, 0000000000, 3, '2021-06-15 11:53:13', '86995104449897874', '0', 0, 1, '{\"ch4\":5,\"domain\":\"antiancorp.com\",\"gasHeartbeat\":86400,\"ip\":\"139.159.199.99\",\"leanangle\":20,\"logNum\":10,\"openangle\":120,\"port\":9999,\"sensorHeartbeat\":86400,\"siltHeartbeat\":86400,\"siltHigh\":150,\"wakeHeartbeat\":86400,\"waterLevel1\":50,\"waterLevel2\":50}', '898604851920C0319067', '0', '2147483647', '460080533209067', '20000', '15000', '25000', '15', '30', '250')".format(self.no, self.terminal_no))
        self.mysql_conn.insert_sql(
            "INSERT INTO `t_cellar_well_control_log` VALUES (1403295756407812097, {}, 0, '2021-06-11 18:19:15')".format(self.terminal_no))
        self.mysql_conn.insert_sql(
            "INSERT INTO `t_cellar_well_sensor` VALUES (1403287188904357889, {}, 90, 20, 10, 0, 'V1.0', 'V1.0', 0, 0, 0, '2021-06-11 17:45:12', '0', 0, NULL, 20, 30)".format(self.terminal_no))
        self.mysql_conn.insert_sql(
            "INSERT INTO `t_device_alarm` VALUES ({}, {}, 51, 0, 0, '2021-06-18 16:44:02', NULL, NULL, 0)".format(self.alarm_id, self.terminal_no))
        self.mysql_conn.insert_sql(
            "INSERT INTO `t_push_message` VALUES (1403288965368262658, {}, {}, NULL, '2021-06-11 17:52:15', '2021-06-11 17:52:16', 1, NULL, 0)".format(self.alarm_id, self.user_id))
        self.mysql_conn.insert_sql(
            "INSERT INTO `t_push_set` VALUES (1403288766956711938, {}, {}, '8', 0, 1, 1, '2021-06-11 17:51:29', 1377074593995628546)".format(self.user_id, self.department_id))
        self.mysql_conn.insert_sql(
            "INSERT INTO `t_task` VALUES (1403291589383565314, {}, 0, '2021-06-11 18:02:41', 1377074593995628546, 1377074593995628546, 0, '1,21,3', 6, 0, NULL, '告警后立即触发', 0, 1)".format(self.department_id))
        self.mysql_conn.insert_sql("insert  into `t_work_order`(`id`,`work_no`,`work_src`,`work_type`,`terminal_no`,`alarm_id`,`user_id`,`reason`,`level`,`prv_finish_time`,`actual_finish_time`,`status`,`create_at`,`create_by`,`address`,`longitude`,`latitude`,`is_delete`,`is_read`) values \
        (1403288961291399169,'GD202106118064',0,0,{},{},{},NULL,0,'2021-06-12 00:00:00','2021-06-11 17:54:58',2,'2021-06-11 17:52:15',NULL,'南山区高新中二道粤海街道25号','113.937336','22.545404',0,1)".format(self.terminal_no, self.alarm_id, self.user_id))
        # self.mysql_conn.insert_sql("insert into t_device_param")

    def delete_device(self):
        self.mysql_conn = Mysql_connet('device')
        self.mysql_conn.delete_sql(
            "delete from t_cellar_well where id={}".format(self.device_id))
        self.mysql_conn.delete_sql(
            "delete from t_capital where id={}".format(self.capital_id))
        self.mysql_conn.delete_sql(
            "delete from t_images where id={}".format(1403287037510955009))
        self.mysql_conn.delete_sql(
            "delete from t_cellar_well_terminal where id={}".format(1403287037427068930))
        self.mysql_conn.delete_sql(
            "delete from t_cellar_well_control_log where id={}".format(1403295756407812097))
        self.mysql_conn.delete_sql(
            "delete from t_cellar_well_sensor where id={}".format(1403287188904357889))
        self.mysql_conn.delete_sql(
            "delete from t_device_alarm where id={}".format(self.alarm_id))
        self.mysql_conn.delete_sql(
            "delete from t_push_message where id={}".format(1403288965368262658))
        self.mysql_conn.delete_sql(
            "delete from t_push_set where id={}".format(1403288766956711938))
        self.mysql_conn.delete_sql(
            "delete from t_task where id={}".format(1403291589383565314))
        self.mysql_conn.delete_sql(
            "delete from t_work_order where id={}".format(1403288961291399169))
        # self.mysql_conn.delete_sql("delete from t_device_param where id={}".format())


if __name__ == "__main__":

    q = Mysql_data()
    print(q.user_id)
    print(q.device_id)
    print(q.department_id)