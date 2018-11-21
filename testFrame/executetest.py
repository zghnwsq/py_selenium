# coding=utf-8
import xlrd
import keywords, log, time, filewrite
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome


class ExecuteTest:

    def __init__(self):
        pass

    def execute(self, filepath, sheet, dr):
        # 开始时间戳
        time_stamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        # 根据时间戳生成log对象
        # lg =  log.Log('/Users/ted/Documents/testlog/'+time_stamp+'.txt', "info")
        lg = log.Log('/Users/ted/Documents/testlog' + time_stamp + '.txt', "info")
        # 打开excel文件
        sht = xlrd.open_workbook(filepath).sheet_by_name(sheet)
        # 读取用例名
        test_case_name = sht.row_values(1)[0].encode('utf-8')
        # 初始化结果变量
        res = False
        # 逐行执行语句
        for i in range(2, sht.nrows):
            params = sht.row_values(i)
            if keywords.Keywords(dr,
                                 params[2].encode('utf-8'),
                                 params[3].encode('utf-8'),
                                 params[4].encode('utf-8'),
                                 params[5].encode('utf-8'),
                                 lg).execute_keyword():
                res = True
            else:
                res = False
        # 执行结束写入报告
        # log_read = open('/Users/ted/Documents/testlog/'+time_stamp+'.txt', 'r')
        log_read = open('/Users/ted/Documents/testlog' + time_stamp + '.txt', 'r')
        # fr = filewrite.FileWrite('/Users/ted/Documents/testlog/'+time_stamp+'.html')
        fr = filewrite.FileWrite('/Users/ted/Documents/testlog' + time_stamp + '.html')
        fr.write_head(test_case_name, res)
        for i in log_read.readlines():
            if i.find("PASS") != -1:
                fr.file_write('<li style="color:green">'+i+'</li>')
            else:
                fr.file_write('<li style="color:red">' + i + '</li>')
        fr.write_end()
        return res

    def execute2(self, filepath, sheet):
        # 开始时间戳
        time_stamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        # 根据时间戳生成log对象
        # lg =  log.Log('/Users/ted/Documents/testlog/'+time_stamp+'.txt', "info")
        # lg = log.Log('/Users/Shared/Jenkins/Home/workspace/selenium/'+time_stamp+'.txt', "info")
        # 打开excel文件
        sht = xlrd.open_workbook(filepath).sheet_by_name(sheet)
        # 获取用例范围
        test_case_count = 0
        beg = 0
        end = 0
        test_case = []
        test_case_name = ''
        for i in range(1, sht.nrows, 1):
            # 如果是第一个用例的名字
            if (sht.row_values(i)[0].encode('utf-8') != '') and (i == 1):
                test_case_count = test_case_count+1
                beg = i+1  # 用例开始的行数
                test_case_name = sht.row_values(i)[0]  # 该用例名
                # print test_case_name
            # 如果是非第一个用例的名字
            elif (sht.row_values(i)[0].encode('utf-8') != '') and (i != 1):
                # print sht.row_values(i)[0].encode('utf-8')
                test_case.append([test_case_count, test_case_name, beg, end])
                test_case_name = sht.row_values(i)[0]
                # print test_case_name
                beg = i+1
                test_case_count = test_case_count + 1
            # 如果到末尾
            elif i == sht.nrows-1:
                end = i
                test_case.append([test_case_count, test_case_name, beg, end])
            else:
                end = i
                # print sht.row_values(i)[2].encode('utf-8')
        # 执行用例集
        res = []  # 用例集结果集合
        print test_case
        for j in test_case:
            lg = log.Log('/Users/ted/Documents/testlog/' + time_stamp + '_' + str(j[0]) + '.txt', "info")
            case_res = True
            dr = Chrome()
            dr.set_page_load_timeout(30)
            for k in range(j[2], j[3]+1, 1):
                params = sht.row_values(k)
                case_res = case_res and keywords.Keywords(dr,
                                                          params[2].encode('utf-8'),
                                                          params[3].encode('utf-8'),
                                                          params[4].encode('utf-8'),
                                                          params[5].encode('utf-8'),
                                                          lg).execute_keyword()
            res.append([j[0], j[1], case_res])
            dr.close()
            dr.quit()
            lg.logger.removeHandler(lg.handler)
        # 写入报告
        # 写入报告头
        fr = filewrite.FileWrite('/Users/ted/Documents/testlog/' + 'Report_' + time_stamp + '.html')
        print res
        fr.write_head2(res)
        result = True  # 用例集最终结果
        # 写入log
        for n in res:
            log_read = open('/Users/ted/Documents/testlog/' + time_stamp + '_' + str(n[0]) + '.txt', 'r')
            fr.file_write('<h3>'+n[1].encode('utf-8')+'</h3><ul>')
            for i in log_read.readlines():
                fr.file_write('<li>' + i + '</li>')
            fr.file_write('</ul>')
            result = result and n[2]
        fr.write_end()
        return result


