import unittest
from test_project.common.http_requests import HttpRequests

class Log(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = 'http://10.10.100.224:10001'
        cls.http = HttpRequests(cls.url)

    def test_001_query_device_log(self):
        data = {}
        response = Log.http.post('/api/deviceLogServiceZuul/deviceLog/findDeviceLogs',data = data)
        self.assertEqual(200,response.status_code,'返回非200')

    def test_002_query_sys_log(self):
        data = {}
        response = Log.http.post('/api/deviceLogServiceZuul/deviceLog/findSystemLogs',data = data)
        self.assertEqual(200,response.status_code,'返回非200')

    def test_003_delete_device_log(self):
        data = {}
        response = Log.http.post('/api/deviceLogServiceZuul/deviceLog/deleteDeviceLogs',data = data)
        self.assertEqual(200,response.status_code,'返回非200')

    def test_004_delete_sys_log(self):
        data = {}
        response = Log.http.post('/api/deviceLogServiceZuul/deviceLog/deleteSystemLogs',data = data)
        self.assertEqual(200,response.status_code,'返回非200')

    def test_005_delete_user_log(self):
        data = {}
        response = Log.http.post('/api/deviceLogServiceZuul/deviceLog/deleteUserLogs',data = data)
        self.assertEqual(200,response.status_code,'返回非200')

    def test_006_export_device_log(self):
        data = {}
        response = Log.http.post('/api/deviceLogServiceZuul/deviceLog/deviceLogExport',data = data)
        self.assertEqual(200,response.status_code,'返回非200')

    def test_007_export_sys_log(self):
        data = {}
        response = Log.http.post('/api/deviceLogServiceZuul/deviceLog/systemLogExport',data = data)
        self.assertEqual(200,response.status_code,'返回非200')

    def test_008_export_user_log(self):
        data = {}
        response = Log.http.post('/api/deviceLogServiceZuul/deviceLog/userLogExport',data = data)
        self.assertEqual(200,response.status_code,'返回非200')

    def test_009_query_user_log(self):
        data = {}
        response = Log.http.post('/api/deviceLogServiceZuul/deviceLog/findUserLogs',data = data)
        self.assertEqual(200,response.status_code,'返回非200')

if __name__ == '__main__':
    unittest.main()