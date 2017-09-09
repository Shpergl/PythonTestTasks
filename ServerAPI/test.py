import unittest
import httpretty

from ServiceAPI import RequestModule, JsonStoragePool, SqLiteStoragePool


class ServiceApiTests():
    """Base TestCase class for all connection types"""
    urls = [
        'http://a.com',
        'http://b.com'
    ]
    module = None

    @httpretty.activate
    def test_send_request(self):
        for url in self.urls:
            httpretty.register_uri(httpretty.GET, url,
                                   body="Mock content from: {}".format(url))

            response = self.module.send_request(url)
            assert response.text == "Mock content from: {}".format(url)


class ServiceApiJsonTestCase(unittest.TestCase, ServiceApiTests):
    """ Test case for Json storage file"""
    def setUp(self):
        storage_path = './storage.json'
        storage = JsonStoragePool(storage_path)
        self.module = RequestModule(storage)


class ServiceApiSqliteTestCase(unittest.TestCase, ServiceApiTests):
    """ Test case for sqlite3 database storage"""
    def setUp(self):
        storage_path = './storage.db'
        storage = SqLiteStoragePool(storage_path)
        self.module = RequestModule(storage)

if __name__ == '__main__':
    unittest.main()
