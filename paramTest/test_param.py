# coding=utf-8
import unittest
import ddt
import readXls

# test_data = [{'用户名': 'test', '密码':'123'}, {'用户名': 'test1', '密码': '123'}]


@ddt.ddt
class MyTestCase(unittest.TestCase):

    def setUp(self):
        print '-------begin-------'

    @ddt.data(*readXls.dataRead().read_data('/Users/ted/Documents/test/1.xlsx', 0))
    # @ddt.data(*test_data)
    def test_something(self, data):
        print data
        print data['username']
        print data['password']

    def tearDown(self):
        print '-------end-------'


if __name__ == '__main__':
    unittest.main()
