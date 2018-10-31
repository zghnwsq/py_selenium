# coding=utf-8
# from selenium.webdriver.chrome.webdriver import WebDriver
# import logging


class Keywords:

    def __init__(self, dr, kwd, arg1, arg2, cmt, log, rtn=None):
        self.dr = dr
        self.rtn = rtn
        self.kwd = kwd
        self.arg1 = arg1
        self.arg2 = arg2
        self.cmt = cmt
        self.log = log

    def locator(self, locator):
        # 根据表达式决定调用selenium元素定位的方法,并返回WebElement
        if "id=" in locator:
            return self.dr.find_element_by_id(locator.replace('id=', '').strip())
        elif "name=" in locator:
            return self.dr.find_element_by_name(locator.replace('name=', '').strip())
        elif "class=" in locator:
            return self.dr.find_element_by_class_name(locator.replace('class=', '').strip())
        elif "css=" in locator:
            return self.dr.find_element_by_css_selector(locator.replace('css=', '').strip())
        elif "xpath=" in locator:
            return self.dr.find_element_by_xpath(locator.replace('xpath=', '').strip())
        # 没有匹配的则抛异常
        else:
            return None
            raise Exception("Invalid element locator!", locator)

    def execute_keyword(self):
        # 执行打开网页
        if self.kwd == "打开网页":
            try:
                # 输出当前执行任务
                if self.cmt != '':
                    self.log.write('开始执行:' + self.cmt, 'info')
                self.dr.get(self.arg1)
            # 报错则写入异常信息
            except Exception as e:
                self.log.write('self.dr.get("'+self.arg1+'"):FAIL', 'error')
                self.log.write(e, 'error')
                # self.log.exception(Argument, 'error')
                # 返回此步骤状态
                return False
            # 通过则写入执行历史
            else:
                self.log.write('self.dr.get("' + self.arg1 + '"):PASS', 'info')
                # 返回此步骤状态
                return True
        # 执行输入文本
        elif self.kwd == "输入文本":
            try:
                # 输出当前执行任务
                if self.cmt != '':
                    self.log.write('开始执行:' + self.cmt, 'info')
                # 根据表达式决定调用selenium元素定位的方法
                if "id=" in self.arg1:
                    self.locator(self.arg1).send_keys(self.arg2)
                elif "name=" in self.arg1:
                    self.locator(self.arg1).send_keys(self.arg2)
                elif "class=" in self.arg1:
                    self.locator(self.arg1).send_keys(self.arg2)
                elif "css=" in self.arg1:
                    self.locator(self.arg1).send_keys(self.arg2)
                elif "xpath=" in self.arg1:
                    self.dr.locator(self.arg1).send_keys(self.arg2)
            except Exception as e:
                self.log.write('self.dr.find_element_by("'+self.arg1+'").send_keys("'+self.arg2+'"):FAIL', 'error')
                self.log.write(e, 'error')
                # self.log.exception(Argument, 'error')
                # 返回此步骤状态
                return False
            else:
                self.log.write('self.dr.find_element_by("'+self.arg1+'").send_keys("'+self.arg2+'"):PASS', 'info')
                # 返回此步骤状态
                return True
        # 执行点击
        elif self.kwd == "点击":
            try:
                # 输出当前执行任务
                if self.cmt != '':
                    self.log.write('开始执行:' + self.cmt, 'info')
                self.locator(self.arg1).click()
            except Exception as e:
                self.log.write('self.dr.find_element_by("'+self.arg1+'").click():FAIL', 'error')
                self.log.write(e, 'error')
                # self.log.exception(Argument, 'error')
                # 返回此步骤状态
                return False
            else:
                self.log.write('self.dr.find_element_by("'+self.arg1+'").click():PASS', 'info')
                # 返回此步骤状态
                return True
        # 关键字不匹配则报错
        else:
            return False
            raise Exception("Invalid Keywords!", self.kwd)
