import unittest

import self as self
from flask import request, json

from apiproject.model.property import Property

class MyTestClass(unittest.TestCase):

    # initialization logic for the test suite declared in the test module
    # code that is executed before all tests in one test run
    @classmethod
    def setUpClass(cls):
        pass


    # clean up logic for the test suite declared in the test module
    # code that is executed after all tests in one test run
    @classmethod
    def tearDownClass(cls):
        pass

    # initialization logic
    # code that is executed before each test
    def setUp(self):
        pass

    # clean up logic
    # code that is executed after each test
    def tearDown(self):
        pass

    # test method
    def test_add_property(self):
        response = self.app.post('/test_function',
                                 data=json.dumps(
                                     dict(name='ipon', description='appartement proche de paris', type='appartement',
                                          city='Vanves', pieces_number=1, caracteristic='', owner='jean')),
                                 content_type='application/json')
        property = Property("ipon", "appartement proche de paris", "appartement", "Vanves", 1, "", "jean")
        self.assertEqual(response, property)


# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()
