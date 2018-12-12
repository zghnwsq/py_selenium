# coding=utf-8
import unittest
import ddt
import readXls
import HTMLTestRunnerCN
import HtmlTestRunner

# test_data = [{'用户名': 'test', '密码':'123'}, {'用户名': 'test1', '密码': '123'}]
aaa = 0

@ddt.ddt
class MyTestCase(unittest.TestCase):

    def setUp(self):
        print '-------begin-------'

    @unittest.skipIf(aaa==0, 'test skip if')
    @ddt.data(*readXls.readXls().read_data('D:/1.xlsx', 0))
    def test_a(self, data):
        print data
        print data['username']
        print data['password']
        print 'a'

    @ddt.data(*readXls.readXls().read_data_by_sheet_name('D:/1.xlsx', 'phpwind'))
    def test_b(self, data):
        # print data
        print data['username']
        print data['password']

    def tearDown(self):
        print '-------end-------'


if __name__ == '__main__':
    # unittest.main()
    fileBase = 'C:/wamp/www'
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fileBase,
        title='{ Test Report }',
        description='aaa',
        tester='ted'
    )
    suit = unittest.TestSuite()
    suit = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    # suit = unittest.TestLoader().loadTestsFromName('test_param.MyTestCase.test_a')
    # suit = unittest.defaultTestLoader.discover(start_dir=".", pattern='test_param.py')
    # suit.addTest(MyTestCase('test_a'))
    runner.run(suit)
