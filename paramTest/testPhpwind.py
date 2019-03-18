# coding:utf-8
import unittest
from selenium.webdriver.ie.webdriver import WebDriver as ie
from selenium.webdriver.remote.webdriver import WebDriver as remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions
import HTMLTestRunnerCN
# from selenium.webdriver.common.action_chains import ActionChains
import TestLogin
import ddt
import readXls

data = readXls.readXls().read_data_by_sheet_name('./testcase/1.xlsx', 'phpwind')


@ddt.ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.dc = DesiredCapabilities.CHROME
        self.re = remote('http://127.0.0.1:4444/wd/hub', desired_capabilities=self.dc)
        self.dr = ie()
        self.dr.set_page_load_timeout(30)
        self.wait = WebDriverWait(self.dr, 30)
        self.dr.get('http://localhost:80/phpwind/upload/')
        self.dr.maximize_window()

    def tearDown(self):
        self.dr.close()
        self.dr.quit()

    # 登录密码为空
    @unittest.skipIf(data[0]['skip'] == 'yes', 'test skip if')
    @ddt.data(*data)
    def test_login_pwd_empty(self, data):
        print u'登录密码为空'
        self.wait.until(lambda x: x.find_element_by_id('nav_pwuser').is_displayed())
        self.dr.find_element_by_id('nav_pwuser').send_keys(data['username'])
        self.dr.find_element_by_name('head_login').click()
        self.wait.until(lambda x: x.find_element_by_xpath('//*[@id="pw_content"]/div/div[2]/div/div/div/p[1]').is_displayed())
        msg = self.dr.find_element_by_xpath('//*[@id="pw_content"]/div/div[2]/div/div/div/p[1]').text
        flag = msg.find(u'用户名或密码为空') != -1
        self.assertEqual(flag, True, u'提示信息错误: actual:' + msg)

    # 登录用户名为空
    @ddt.data(*data)
    def test_login_user_empty(self, data):
        print u'登录用户名为空'
        self.wait.until(lambda x: x.find_element_by_id('showpwd').is_displayed())
        self.dr.find_element_by_id('showpwd').send_keys(data['password'])
        self.dr.find_element_by_name('head_login').click()
        self.wait.until(lambda x:x.find_element_by_xpath('//*[@id="pw_content"]/div/div[2]/div/div/div/p[1]').is_displayed())
        msg = self.dr.find_element_by_xpath('//*[@id="pw_content"]/div/div[2]/div/div/div/p[1]').text
        flag = msg.find(u'用户"输入用户名"不存在') != -1
        self.assertEqual(flag, True, u'提示信息错误: actual:' + msg)

    # 注册用户名一个字符
    @ddt.data(*data)
    def test_register_username_one_char(self, data):
        print u'注册用户名一个字符'
        self.wait.until(lambda x: x.find_element_by_id('showpwd').is_displayed())
        self.dr.find_element_by_xpath(u"//button[text()='注册']").click()
        self.wait.until(lambda x: x.find_element_by_id('regbutton').is_displayed())
        self.dr.find_element_by_id('regbutton').click()
        self.dr.find_element_by_id('regname').send_keys(data['one_char'])
        self.dr.find_element_by_id('regpwd').click()
        self.wait.until(lambda x: x.find_element_by_id('regname_info').text.find(u'检测中') == -1)
        msg = self.dr.find_element_by_id('regname_info').text
        flag = msg.find(u'用户名长度错误') != -1
        self.assertEqual(flag, True, u'提示信息错误: actual:' + msg)
        # ActionChains(self.dr).drag_and_drop_by_offset()

    # 注册用户名2个字符
    @ddt.data(*data)
    def test_register_username_two_char(self, data):
        print u'注册用户名2个字符'
        self.wait.until(lambda x: x.find_element_by_id('showpwd').is_displayed())
        self.dr.find_element_by_xpath(u"//button[text()='注册']").click()
        self.wait.until(lambda x: x.find_element_by_id('regbutton').is_displayed())
        self.dr.find_element_by_id('regbutton').click()
        self.dr.find_element_by_id('regname').send_keys(data['two_char'])
        self.dr.find_element_by_id('regpwd').click()
        self.wait.until(lambda x: x.find_element_by_id('regname_info').text.find(u'检测中') == -1)
        msg = self.dr.find_element_by_id('regname_info').text
        flag = msg.find(u'用户名长度错误') != -1
        self.assertEqual(flag, True, u'提示信息错误: actual:' + msg)

    # 注册用户名13个字符
    @ddt.data(*data)
    def test_register_username_thirteen_char(self, data):
        print u'注册用户名13个字符'
        self.wait.until(lambda x: x.find_element_by_id('showpwd').is_displayed())
        self.dr.find_element_by_xpath(u"//button[text()='注册']").click()
        self.wait.until(lambda x: x.find_element_by_id('regbutton').is_displayed())
        self.dr.find_element_by_id('regbutton').click()
        self.dr.find_element_by_id('regname').send_keys(data['thirteen_char'])
        self.dr.find_element_by_id('regpwd').click()
        self.wait.until(lambda x: x.find_element_by_id('regname_info').text.find(u'检测中') == -1)
        msg = self.dr.find_element_by_id('regname').get_attribute('value')
        self.assertEqual(len(msg), 12, u'错误: actual:' + msg)

    # 注册用户名为空
    def test_register_username_empty(self):
        print u'注册用户名为空'
        self.wait.until(lambda x: x.find_element_by_id('showpwd').is_displayed())
        self.dr.find_element_by_xpath(u"//button[text()='注册']").click()
        self.wait.until(lambda x: x.find_element_by_id('regbutton').is_displayed())
        self.dr.find_element_by_id('regbutton').click()
        self.dr.find_element_by_id('regname').click()
        self.dr.find_element_by_id('regpwd').click()
        self.wait.until(lambda x: x.find_element_by_id('regname_info').text.find(u'检测中') == -1)
        msg = self.dr.find_element_by_id('regname_info').text
        flag = msg.find(u'用户名不能为空') != -1
        self.assertEqual(flag, True, u'提示信息错误: actual:' + msg)

    # 注册用户名含空格
    @ddt.data(*data)
    def test_register_username_space(self, data):
        print u'注册用户名包含空格'
        self.wait.until(lambda x: x.find_element_by_id('showpwd').is_displayed())
        self.dr.find_element_by_xpath(u"//button[text()='注册']").click()
        self.wait.until(lambda x: x.find_element_by_id('regbutton').is_displayed())
        self.dr.find_element_by_id('regbutton').click()
        self.dr.find_element_by_id('regname').send_keys(data['username_space'])
        self.dr.find_element_by_id('regpwd').click()
        self.wait.until(lambda x: x.find_element_by_id('regname_info').text.find(u'检测中') == -1)
        msg = self.dr.find_element_by_id('regname_info').text
        flag = msg.find(u'包含不可接受字符或被管理员屏蔽') != -1
        self.assertEqual(flag, True, u'提示信息错误: actual:' + msg)

    # 注册用户名含非法字符
    @ddt.data(*data)
    def test_register_username_illegal_char(self, data):
        print u'注册用户名包含非法字符'
        self.wait.until(lambda x: x.find_element_by_id('showpwd').is_displayed())
        self.dr.find_element_by_xpath(u"//button[text()='注册']").click()
        self.wait.until(lambda x: x.find_element_by_id('regbutton').is_displayed())
        self.dr.find_element_by_id('regbutton').click()
        self.dr.find_element_by_id('regname').send_keys(data['username_illegal_char'])
        self.dr.find_element_by_id('regpwd').click()
        self.wait.until(lambda x: x.find_element_by_id('regname_info').text.find(u'检测中') == -1)
        msg = self.dr.find_element_by_id('regname_info').text
        flag = msg.find(u'包含不可接受字符或被管理员屏蔽') != -1
        self.assertEqual(flag, True, u'提示信息错误: actual:' + msg)

    # 注册密码为空
    @ddt.data(*data)
    def test_register_pwd_empty(self, data):
        print u'注册密码为空'
        self.wait.until(lambda x: x.find_element_by_id('showpwd').is_displayed())
        self.dr.find_element_by_xpath(u"//button[text()='注册']").click()
        self.wait.until(lambda x: x.find_element_by_id('regbutton').is_displayed())
        self.dr.find_element_by_id('regbutton').click()
        self.dr.find_element_by_id('regname').send_keys(data['username'])
        self.dr.find_element_by_id('regpwd').click()
        self.dr.find_element_by_id('regpwdrepeat').click()
        self.wait.until(lambda x: x.find_element_by_id('pwd_info').text.find(u'检测中') == -1)
        msg = self.dr.find_element_by_id('pwd_info').text
        flag = (msg.find(u'密码设置错误') != -1) and (msg.find(u'密码长度过小') != -1)
        self.assertEqual(flag, True, u'提示信息错误: actual:' + msg)

    # 注册密码5位字符
    @ddt.data(*data)
    def test_register_pwd_five_char(self, data):
        print u'注册密码5位字符'
        self.wait.until(lambda x: x.find_element_by_id('showpwd').is_displayed())
        self.dr.find_element_by_xpath(u"//button[text()='注册']").click()
        self.wait.until(lambda x: x.find_element_by_id('regbutton').is_displayed())
        self.dr.find_element_by_id('regbutton').click()
        self.dr.find_element_by_id('regname').send_keys(data['username'])
        self.dr.find_element_by_id('regpwd').send_keys(data['pwd_five_char'])
        self.dr.find_element_by_id('regpwdrepeat').click()
        self.wait.until(lambda x: x.find_element_by_id('pwd_info').text.find(u'检测中') == -1)
        msg = self.dr.find_element_by_id('pwd_info').text
        flag = (msg.find(u'密码设置错误') != -1) and (msg.find(u'密码长度过小') != -1)
        self.assertEqual(flag, True, u'提示信息错误: actual:' + msg)

    # 注册密码17位字符
    @ddt.data(*data)
    def test_register_pwd_seventeen_char(self, data):
        print u'注册密码17位字符'
        self.wait.until(lambda x: x.find_element_by_id('showpwd').is_displayed())
        self.dr.find_element_by_xpath(u"//button[text()='注册']").click()
        self.wait.until(lambda x: x.find_element_by_id('regbutton').is_displayed())
        self.dr.find_element_by_id('regbutton').click()
        self.dr.find_element_by_id('regname').send_keys(data['username'])
        self.dr.find_element_by_id('regpwd').send_keys(data['pwd_seventeen_char'])
        self.dr.find_element_by_id('regpwdrepeat').click()
        self.wait.until(lambda x: x.find_element_by_id('pwd_info').text.find(u'检测中') == -1)
        msg = self.dr.find_element_by_id('pwd_info').text
        flag = (msg.find(u'密码设置错误') != -1) and (msg.find(u'密码过长') != -1)
        self.assertEqual(flag, True, u'提示信息错误: actual:' + msg)


if __name__ == '__main__':
    # unittest.main()
    # fileBase = 'C:/Users/Administrator/PycharmProjects/selenium'
    # 利用web服务,提供报告的网页浏览
    # fileBase = 'C:/wamp/www'
    fileBase = '.'  # 分布式执行报告目录
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fileBase,
        title='{ Test Report }',
        description=u'phpwind登录和注册',
        tester='ted'
    )
    suit = unittest.TestSuite()
    suit1 = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    suit2 = unittest.TestLoader().loadTestsFromTestCase(TestLogin.TestLogin)
    suit.addTest(suit1)
    suit.addTest(suit2)
    # test_cases = [MyTestCase('test_login_pwd_empty'), MyTestCase('test_login_user_empty'),
    #               MyTestCase('test_register_username_one_char'), MyTestCase('test_register_username_tow_char'),
    #               MyTestCase('test_register_username_thirteen_char'), MyTestCase('test_register_username_empty'),
    #               MyTestCase('test_register_pwd_empty'), MyTestCase('test_register_pwd_five_char'),
    #               MyTestCase('test_register_pwd_seventeen_char'), MyTestCase('test_register_username_space'),
    #               MyTestCase('test_register_username_illegal_char'), TestLogin.TestLogin('test_a')]
    # suit.addTests(test_cases)
    runner.run(suit)


