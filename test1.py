# coding=utf-8
import unittest
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
# import logging
# import time
# import keywords
# import log
# import filewrite
# import time
import executetest, xlrd


class MyTestCase(unittest.TestCase):

    def setUp(self):
        pass
        # logging.basicConfig(filename="/Users/ted/Documents/testlog/1.txt",
        #                     level=logging.INFO,
        #                     format='%(asctime)s %(filename)s %(funcName)s[line:%(lineno)d] %(levelname)s %(message)s',
        #                     datefmt='%a, %d %b %Y %H:%M:%S')

        # # 第一步，创建一个logger
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)  # Log等级总开关
        #
        # # 第二步，创建一个handler，用于写入日志文件
        # logfile = '/Users/ted/Documents/testlog/1.txt'
        # handler = logging.FileHandler(logfile, mode='a')
        # handler.setLevel(logging.INFO)  # 输出到file的log等级的开关
        #
        # # 第三步，再创建一个handler，用于输出到控制台
        # # ch = logging.StreamHandler()
        # # ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关
        #
        # # 第四步，定义handler的输出格式
        # formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s",
        #                               datefmt='%a, %d %b %Y %H:%M:%S')
        # handler.setFormatter(formatter)
        # # ch.setFormatter(formatter)
        #
        # # 第五步，将logger添加到handler里面
        # logger.addHandler(handler)
        # # logger.addHandler(ch)
        #
        # self.dr = Chrome()
        # self.dr.set_page_load_timeout(30)
        # # self.dr.get("http://mail.sina.com.cn")
        # #时间获取
        # print time.strftime("%Y%m%d%H%M%S", time.localtime())

    def tearDown(self):
        pass
        # self.dr.close()
        # self.dr.quit()

    def test_a(self):
        # print "111"
        # logging.info("1111")
        # res = False
        # log2 = log.Log("/Users/ted/Documents/testlog/log999.txt", "info")
        # tmp = keywords.Keywords(self.dr,
        #                         "打开网页",
        #                         "http://mail.sina.com.cn",
        #                         "",
        #                         "打开网页",
        #                         log2).execute_keyword()
        # tmp = tmp and keywords.Keywords(self.dr,
        #                                 "输入文本",
        #                                 "id=freename",
        #                                 "tedwang@sina.cn",
        #                                 "输入用户名",
        #                                 log2).execute_keyword()
        # tmp = tmp and keywords.Keywords(self.dr,
        #                                 "输入文本",
        #                                 "id=freepassword",
        #                                 "wsq851021",
        #                                 "输入密码",
        #                                 log2).execute_keyword()
        # time.sleep(5)
        # res = tmp
        #
        # log_read = open('/Users/ted/Documents/testlog/log999.txt', 'r')
        # fr = filewrite.FileWrite("/Users/ted/Documents/testlog/report999.html")
        # fr.write_head('登录新浪邮箱', res)
        # for i in log_read.readlines():
        #     fr.file_write('<li>'+i+'</li>')
        # fr.write_end()
        # sht = xlrd.open_workbook('/Users/ted/Documents/testlog/testCase1.xlsx').sheet_by_name('sheet1')
        # print sht.row_values(1)[0].encode('utf-8')
        # for i in range(2, sht.nrows):
        #     params = sht.row_values(i)
        #     print params[2].encode('utf-8')
        #     print params[3].encode('utf-8')
        #     print params[4].encode('utf-8')
        #     print params[5].encode('utf-8')

        result = executetest.ExecuteTest().execute2('/Users/ted/Documents/testlog/testCase1.xlsx', 'sheet1')
        self.assertEqual(True, result, u'用例执行失败，请查看日志')  #111


if __name__ == '__main__':
    unittest.main()
