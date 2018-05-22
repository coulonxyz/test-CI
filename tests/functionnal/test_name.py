import unittest
import json
from ddt import ddt, file_data

from app import app


@ddt
class TestHello(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()  # we instantiate a flask test client

    def tearDown(self):
        pass

    @file_data('./name.json')
    def test_get_hello_route(self, name, expected_name):
        response = self.client.get(
            '/hello/{}'.format(name),
            content_type='application/json')

        response = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response['hello'], expected_name)


if __name__ == '__main__':
    unittest.main()
