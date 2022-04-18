import unittest,os,sys,json

path = os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(path)
from common.login_token import get_token
from config.config_test import Conf
from common.http_requests import HttpRequests
from common.mysql_data import Mysql_connet

class Test_Add_Task(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = Conf.TEST_APP_URL.value
        cls.http = HttpRequests(cls.url)
        cls.mysql = Mysql_connet('device')
        cls.mysql.insert_device()
        cls.mysql.insert_user()


    @classmethod
    def tearDownClass(cls) -> None:
        # cls.mysql.delete_device()
        # cls.mysql.delete_user()
        cls.mysql.close()


    def test_add_task_success(self):
        '''修改设备参数用例：/termianal/modifyDeviceParameters'''
        payload = {
            'angleKillAlarmValue': 10,
            'angleQuake': 250,
            'angleStaticMaxValue': 150,
            'angleStaticTime': 2,
            'broadcastCyc': "1",
            'ch4Level1': 50,
            'ch4Level2': 20,
            'ch4Level3': 10,
            'domain': "www.antan.com",
            'gasHeartbeat': 3600,
            'ip': "106.52.198.240",
            'logNum': 0,
            'mac': self.mysql.mac,
            'monitorModel': 0,
            'openangle': 15,
            'port': 9999,
            'qxAlarmNum': 15,
            'qxDayAbnormalWakeNum': 1500,
            'sensorAlarmShakeNum': 9,
            'sensorHeartbeatDuration': 24,
            'terminalHeartbeatDuration': 1,
            'terminalNo': self.mysql.terminal_no,
            'timeout': 1000,
            'waterRemoveQuakeTime': 5
        }
        payload = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json'}
        response = Test_Add_Task.http.post(
            '/termianal/modifyDeviceParameters', data=payload,headers=headers)
        self.assertEqual(200, response.status_code, '返回非200')
        self.assertEqual(str(0), str(response.json()['code']), '修改设备参数失败')


if __name__ == '__main__':
    unittest.main()
