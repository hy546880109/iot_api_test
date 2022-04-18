import pymysql
import os
import sys
import json
def add_syspath():
    path = os.path.join((os.path.dirname((
        os.path.dirname(os.path.abspath(__file__))))))
    sys.path.append(path)

add_syspath()
from config.config_test import Conf
from importlib.resources import path


host = Conf.host.value
port = Conf.port.value
user = Conf.user.value
password = Conf.password.value


class Mysql_connet():
    def __init__(self, db):
        self.mysql_conn = pymysql.connect(
            host=host, port=port, user=user, password=password, db=db)
        self.cur = self.mysql_conn
        self.user_id = 123456789
        self.mac = str('C3:B2:5D:7E:AE:7A')
        self.department_id = 234567891
        self.role_id = 345678912
        self.device_id = 456789123
        self.no = 567891234
        self.terminal_no = 678912345
        self.user_role_id = 789123456
        self.role_menu_id = 789123456
        self.menu_id = 1234512345
        self.alarm_id = 12334565434
        self.push_message_id = 1234509876
        self.task_id = 12346473453
        self.push_set_id = 123456321456
        self.capital_id = 124345657563
        self.cellar_well_terminal_id = 111222333444
        self.cellar_well_control_log_id = 222333444555
        self.cellar_well_sensor_id = 333444555666
        self.images_id = 1231232121
        self.work_order_id = 333444555666777
        self.value = '{"alarmIsSwitch":0,"angleBluetoothSignalValue":10,"angleKillAlarmValue":"12","angleQuake":"250","angleStaticMaxValue":"150","angleStaticTime":"2","broadcastCyc":1,"ch4Level1":"50","ch4Level2":"20","ch4Level3":"10","coverIsSwitch":1,"domain":"www.antan.com","gasHeartbeat":86400,"ip":"106.52.198.240","leanangle":15,"logNum":0,"moduleType":"1,2,4,16","monitorModel":0,"openangle":15,"port":9999,"qxAlarmNum":15,"qxDayAbnormalWakeNum":1500,"sensorAlarmShakeNum":9,"sensorHeartbeat":86400,"sensorHeartbeatDuration":24,"sensorIsSwitch":0,"siltHeartbeat":86400,"siltHigh":1,"terminalHeartbeatDuration":24,"timeout":1000,"wakeHeartbeat":86400,"waterLevel1":10,"waterLevel2":20,"waterRemoveQuakeTime":5}'
        self.value = json.dumps(self.value)

    def insert_sql(self, sql):
        mysql_conn = self.cur
        try:
            with mysql_conn.cursor() as cursor:
                mysql_conn.ping(reconnect=True)
                cursor.execute(sql)
                mysql_conn.commit()

        except Exception as e:
            mysql_conn.rollback()

    def delete_sql(self, sql):
        mysql_conn = self.cur
        try:
            with mysql_conn.cursor() as cursor:
                mysql_conn.ping(reconnect=True)
                cursor.execute(sql)
                mysql_conn.commit()

        except Exception as e:
            mysql_conn.rollback()

    def select_sql(self, sql):
        mysql_conn = self.cur
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

    def update_sql(self, sql):
        mysql_conn = self.cur
        try:
            with mysql_conn.cursor() as cursor:
                mysql_conn.ping(reconnect=True)
                cursor.execute(sql)
                mysql_conn.commit()

        except Exception as e:
            mysql_conn.rollback()

    def close(self):
        mysql_conn = self.cur
        mysql_conn.cursor().close()
        mysql_conn.close()

    def insert_user(self):
        self.mysql_conn = Mysql_connet('user')
        self.mysql_conn.insert_sql("insert  into `t_department`(`id`,`name`,`pid`,`province_id`,`province_name`,`city_id`,`city_name`,`area_id`,`area_name`,`remark`,\
        `is_delete`,`create_at`,`create_by`,`update_at`,`update_by`) values\
        ({},'移动部门',0,11,'北京',1101,'北京市辖',110101,'东城区','in ut qui cillum veniam',0,'2021-04-15 13:13:57',NULL,'2021-06-08 18:02:27',NULL)"
                                   .format(self.department_id))

        self.mysql_conn.insert_sql("insert  into `t_user`(`id`,`code`,`name`,`password`,`salt`,`level`,`phone`,`icon`,`email`,`is_delete`,`status`,`department_id`,\
        `province_id`,`province_name`,`city_id`,`city_name`,`area_id`,`area_name`,`last_login_time`,`create_at`,`create_by`,`update_at`,`update_by`,`remark`,`jpush_id`) values \
        ({},'hy','黄先春','2bd8934d1902b74caa2ce4f77bb84812','c0ae9feb',1,'180358812635','https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/87fef3cda6e14762a572e4022a017a97.jpg',\
        'huang_xc@sohu.com',0,0,{},43,'湖南',4311,'永州',431129,'江华瑶族自治县','2021-06-03 09:15:10','2021-03-31 09:45:43',NULL,'2021-05-14 17:16:16',NULL,NULL,NULL)"
                                   .format(self.user_id, self.department_id))

        self.mysql_conn.insert_sql("INSERT INTO `user`.`t_user_role`(`id`, `role_id`, `user_id`) VALUES ({}, {}, {});"
                                   .format(self.user_role_id, self.role_id, self.user_id))
        self.mysql_conn.insert_sql(
            "INSERT INTO `user`.`t_role`(`id`, `name`, `remark`, `is_delete`, `create_at`, `create_by`, `update_at`, `update_by`) VALUES ({}, '施工人员', '施工人员', 0,\
            '2021-06-24 09:21:23', 1377074593995628546, '2021-06-30 10:06:57', NULL);"
            .format(self.role_id))
        self.mysql_conn.insert_sql("INSERT INTO `user`.`t_role_menu`(`id`, `role_id`, `menu_id`) VALUES ({}, {}, 10);"
                                   .format(self.role_menu_id, self.role_id))

    def delete_user(self):
        self.mysql_conn = Mysql_connet('user')
        self.mysql_conn.delete_sql(
            "delete from t_department where id={}".format(self.department_id))
        self.mysql_conn.delete_sql(
            "delete from t_user where id={}".format(self.user_id))
        self.mysql_conn.delete_sql(
            "delete from t_user_role where id={}".format(self.user_role_id))
        self.mysql_conn.delete_sql(
            "delete from t_role where id={}".format(self.role_id))
        self.mysql_conn.delete_sql(
            "delete from t_role_menu where id={}".format(self.role_menu_id))

    def insert_device(self):
        self.mysql_conn = Mysql_connet('device')
        self.mysql_conn.insert_sql("INSERT  INTO `t_cellar_well`(`id`, `no`, `terminal_no`, `unit_id`, `province_id`, `province_name`, `city_id`, `city_name`,\
         `area_id`, `area_name`, `address`, `spec`, `department_id`, `department_name`, `type`, `sub_type`, `cover_type`, `is_online`, `control_status`, \
         `status`, `is_delete`, `create_at`, `create_by`, `update_at`, `update_by`, `longitude`, `latitude`, `name`, `remark`)  VALUES\
        ({}, {}, {}, 1, 44, '广东省', 4403, '深圳市', 440305, '南山区', '南山区科技中二路29号靠近深圳软件园2期',\
        '1', 1456087868379238402, '测试部', 2, 2, 0, 0, 0, 0, 0, '2022-04-12 14:10:04', 1512260802038464514, '2022-04-12 17:17:11', 1512260802038464514,\
        '113.93764', '22.545283', 'hy', NULL);"
                                   .format(self.device_id, self.no, self.terminal_no))
        self.mysql_conn.insert_sql("INSERT INTO `t_capital`(`id`, `no`, `unit_id`, `department_id`, `department_name`, `duty_man`, `duty_man_phone`,\
        `safe_man`, `safe_man_phone`, `insurance_corp`, `insurance_status`, `insurance_at`, `create_at`, `create_by`, `remark`) VALUES\
        ({}, {}, 1, {}, '测试部', NULL, NULL, NULL, NULL, NULL, 0, NULL, '2022-04-12 14:10:04', NULL, NULL)"
                                   .format(self.capital_id, self.no, self.department_id))
        self.mysql_conn.insert_sql("INSERT INTO `t_images`(`id`, `terminal_no`, `pid`, `type`, `images1`, `images2`,`images3`, `images4`,\
             `is_delete`, `create_at`) VALUES ({}, {}, 1506887104729194497,0, 'https://antian-iot-oss.obs.cn-south-1.myhuaweicloud.com:443/ce8ca0ed40e34647b42f04059408a722.jpg',\
             NULL, NULL, NULL, 0,'2022-03-24 14:54:17');"
                                   .format(self.images_id, self.terminal_no))
        # self.mysql_conn.insert_sql("INSERT INTO `t_cellar_well_terminal`(`id`, `no`, `terminal_no`, `hardware_ver`, `software_ver`, `battery_num`,\
        #      `semaphore`, `heart_rate`, `is_online`, `alarm_status`, `protect_status`, `last_protect_at`, `create_at`, `alarm_total`, `heart_total`,\
        #      `last_heart_time`, `sim`, `sinr`, `upgrade_status`, `upgrade_at`, `config_status`, `config_value`, `curr_config_value`, `config_at`, `iccid`,\
        #      `is_delete`, `mac`, `imsi`, `firedamp`, `co`, `hs`, `mud_high`, `water_high`, `temperature`, `install_status`, `down_config_value`, `lean_angle`,\
        #      `name`, `remark`, `third_id`, `lock_id`, `lock_status`, `inner_cap_status`, `out_cap_stuatus`, `lock_temperature`, `lock_humidity`, `unlocking_at`)\
        #      VALUES ({}, {}, {}, 'IGW-NB-K-BX-V1.0', 'ZL-V1.0.3-220324', '0', '0', '0', 0, 1, 1, '2022-03-24 14:54:17', NULL,\
        #      0000000004, 0, NULL, NULL, '0', 0, NULL, 4, NULL, NULL, NULL, NULL, '1', {}, '460081087908397', NULL, '0', '0', '0', '0', '0', 0, NULL,\
        #      NULL, NULL, NULL, NULL, NULL, 1, 0, 0, NULL, NULL, NULL);"
        self.mysql_conn.insert_sql("INSERT INTO `device`.`t_cellar_well_terminal`(`id`, `no`, `terminal_no`, `hardware_ver`, `software_ver`, `battery_num`,\
             `semaphore`, `heart_rate`, `is_online`, `alarm_status`, `protect_status`, `last_protect_at`, `create_at`, `alarm_total`, `heart_total`,\
            `last_heart_time`, `sim`, `sinr`, `upgrade_status`, `upgrade_at`, `config_status`, `config_value`, `curr_config_value`, `config_at`,\
            `iccid`, `is_delete`, `mac`, `imsi`, `firedamp`, `co`, `hs`, `mud_high`, `water_high`, `temperature`, `install_status`,\
            `down_config_value`, `lean_angle`, `name`, `remark`, `third_id`, `lock_id`, `lock_status`, `inner_cap_status`, `out_cap_stuatus`,\
            `lock_temperature`, `lock_humidity`, `unlocking_at`) VALUES ({}, {}, {}, 'IGW-NB-K-BX-V1.0',\
            'ZL-V1.0.5-220411', '96', '19', '0', 0, 1, 0, '2022-04-13 15:48:43', NULL, 0000000003, 22, '2022-04-14 11:23:19', '89861119212002368684','21', 4, NULL, 4,\
            {},NULL,NULL, '89861119212002368684', '0', 'C3:B2:5D:7E:AE:7B', '460113036642806', '0', '0', '0', '0', '0', '0', 1, '', 2, NULL, NULL,\
            '', '', 0, 0, 1, '25\0', '80\0', '2022-04-13 15:50:07');"
            .format(self.cellar_well_terminal_id, self.no, self.terminal_no, self.value))
                            
        self.mysql_conn.insert_sql(
            "INSERT INTO `t_cellar_well_control_log` (`id`, `terminal_no`, `status`, `create_at`) VALUES ({}, {}, 0, '2022-03-24 13:58:52')"
            .format(self.cellar_well_control_log_id, self.terminal_no))
        self.mysql_conn.insert_sql(
            "INSERT INTO `t_cellar_well_sensor` (`id`, `terminal_no`, `battery_num`, `lean_angle`, `open_angle`, `is_online`, `hardware_ver`, `software_ver`,\
            `upgrade_status`, `upgrade_at`, `type`, `is_delete`, `create_at`, `mac`, `bind_status`, `sensor_no`, `lean_alarm_value`, `open_alarm_value`,\
             `angle_sensor_wake_times`, `config_at`, `config_status`) VALUES ({}, {}, 35, 2, 0, 0, 'IGW-AWA100-NB-K-PCBV1.1', 'SC-V1.1.6-220120', 4, NULL, 1, 0,\
             '2022-04-12 15:06:35', 'C3:B2:5D:7E:AE:7A', 1, NULL, NULL, NULL, 3, NULL, NULL)"
            .format(self.cellar_well_sensor_id, self.terminal_no))
        self.mysql_conn.insert_sql(
            "INSERT INTO `t_device_alarm` (`id`, `terminal_no`, `alarm_type`, `status`, `dispatch_status`, `alarm_date`, `dissolve_date`, `alarm_value`,\
             `is_read`, `related_id`, `directive`, `dissolve_value`) VALUES ({}, {}, 72, 1, 0, '2022-04-12 16:13:19',\
             '2022-04-12 16:37:02', '', 1, 1513792108694200321, '', NULL);"
            .format(self.alarm_id, self.terminal_no))
        self.mysql_conn.insert_sql(
            "INSERT INTO `t_push_message`(`id`, `alarm_id`, `user_id`, `app_push_date`, `sms_push_date`, `phone_push_date`, `app_push_status`,\
             `sms_push_status`, `phone_push_status`, `department_id`) VALUES ({}, {}, {},\
             '2022-03-24 15:24:36', '2022-03-24 15:24:36', '2022-03-24 15:24:36', 1, 1, 1, 1456087868379238402);"
            .format(self.push_message_id, self.alarm_id, self.user_id))
        self.mysql_conn.insert_sql(
            "INSERT INTO `t_push_set`(`id`, `user_id`, `department_id`, `message_type`, `app_type`, `sms_type`, `phone_type`, `create_at`, `create_by`)\
             VALUES ({}, {}, {}, '1', 1, 0, 0, '2022-04-07 09:52:54', 123456789);"
            .format(self.push_set_id, self.user_id, self.department_id))
        self.mysql_conn.insert_sql(
            "INSERT INTO `t_task`(`id`, `department_id`, `task_type`, `create_at`, `create_by`, `task_receive`, `device_type`, `alarm_type`,\
             `finsih_firish_policy_date`, `select_do_policy_date`, `pre_finish_time`, `remark`, `status`, `is_delete`, `app_type`, `sms_type`, `phone_type`)\
             VALUES ({}, {}, 0, '2022-03-24 18:45:37', 1377074593995628546, 1456088038487625729, 0,'13,9,11,1,51,4,53,109,16,12', 2, 0, NULL, '', 0, 0, 1, 1, 0);"
            .format(self.task_id, self.department_id, self.user_id))
        self.mysql_conn.insert_sql("insert  into `t_work_order`(`id`,`work_no`,`work_src`,`work_type`,`terminal_no`,`alarm_id`,`user_id`,`reason`,`level`,\
            `prv_finish_time`,`actual_finish_time`,`status`,`create_at`,`create_by`,`address`,`longitude`,`latitude`,`is_delete`,`is_read`) values \
            ({},'GD202106118064',0,0,{},{},{},NULL,0,'2021-06-12 00:00:00','2021-06-11 17:54:58',2,'2021-06-11 17:52:15',NULL,'南山区高新中二道粤海街道25号',\
            '113.937336','22.545404',0,1)"
            .format(self.work_order_id, self.terminal_no, self.alarm_id, self.user_id))

    def delete_device(self):
        self.mysql_conn = Mysql_connet('device')
        self.mysql_conn.delete_sql(
            "delete from t_cellar_well where no={}".format(self.no))
        self.mysql_conn.delete_sql(
            "delete from t_capital where no={}".format(self.no))
        self.mysql_conn.delete_sql(
            "delete from t_images where id={}".format(self.images_id))
        self.mysql_conn.delete_sql(
            "delete from t_cellar_well_terminal where id={}".format(self.cellar_well_terminal_id))
        self.mysql_conn.delete_sql(
            "delete from t_cellar_well_control_log where id={}".format(self.cellar_well_control_log_id))
        self.mysql_conn.delete_sql(
            "delete from t_cellar_well_sensor where id={}".format(self.cellar_well_sensor_id))
        self.mysql_conn.delete_sql(
            "delete from t_device_alarm where id={}".format(self.alarm_id))
        self.mysql_conn.delete_sql(
            "delete from t_push_message where id={}".format(self.push_message_id))
        self.mysql_conn.delete_sql(
            "delete from t_push_set where id={}".format(self.push_set_id))
        self.mysql_conn.delete_sql(
            "delete from t_task where id={}".format(self.task_id))
        self.mysql_conn.delete_sql(
            "delete from t_work_order where id={}".format(self.work_order_id))


if __name__ == '__main__':
    con = Mysql_connet('device')
    print(con)
    # con.insert_device()
    # con.delete_device()
    # con.insert_user()
    con.delete_user()
    con.close()
