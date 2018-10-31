# coding=utf-8


class FileWrite:

    def __init__(self, filepath):
        self.filepath = filepath

    def file_write(self, msg):
        # 追加方式打开文件
        fr = open(self.filepath, 'a')
        # 写入信息
        fr.write(msg)
        # 关闭文件
        fr.close()

    def write_head(self, testcase, result=False):
        if result:
            self.file_write('''<html>
                                    <head>
                                        <title></title>
                                    </head>
                                    <body>
                                    <h1>Report</h1>
                                    <table border="1" cellspacing="0" width="50%" height="5%">
                                        <thead>
                                            <td>TestcaseName</td>
                                            <td>Result</td>
                                        </thead>
                                            <tr>
                                                <td>'''+testcase+'''</td>
                                                <td style="color:green">PASS</td>
                                            </tr>
                                    </table>
                                    <br/>
                                    <br/>
                                    <h2>Log:</h2>''')
        else:
            self.file_write('''<html>
                                    <head>
                                        <title></title>
                                    </head>
                                    <body>
                                    <table border="1" cellspacing="0" width="50%" height="5%">
                                        <thead>
                                            <td>TestcaseName</td>
                                            <td>Result</td>
                                        </thead>
                                            <tr>
                                                <td>'''+testcase+'''</td>
                                                <td style="color:red">FAIL</td>
                                            </tr>
                                    </table>
                                    <br/>
                                    <br/>
                                    <h2>Log:</h2>''')

    def write_head2(self, result):
        # 用例集结果头
        self.file_write('''<html>
                                    <head>
                                        <title></title>
                                    </head>
                                    <body>
                                    <h1>Report</h1>
                                    <table border="1" cellspacing="0" width="50%" height="5%">
                                        <thead>
                                            <td>TestcaseName</td>
                                            <td>Result</td>
                                        </thead>''')
        for i in result:
            # 用例结果
            if i[2]:
                self.file_write('''
                                                <tr>
                                                    <td>'''+i[1].encode('utf-8')+'''</td>
                                                    <td style="color:green">PASS</td>
                                                </tr>
                                ''')
            else:
                self.file_write('''
                                                <tr>
                                                    <td>'''+i[1].encode('utf-8')+'''</td>
                                                    <td style="color:red">FAIL</td>
                                                </tr>
                                ''')
        # 用例集结果尾
        self.file_write('''
                                    </table>
                        <br/>
                        <br/>
                        <h2>Log:</h2>''')

    def write_end(self):
        self.file_write('''             
                                    </body>
                                </html>
        ''')
