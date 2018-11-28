# coding=utf-8

# import ddt
import xlrd


class dataRead:

    def __init__(self):
        pass

    def read_data(self, path, index):
        sheet = xlrd.open_workbook(path).sheet_by_index(index)
        row = sheet.nrows  # 总行数
        col = sheet.ncols  # 总列数
        col_name = sheet.row_values(0)  # 列名
        data = []
        for i in range(1, row, 1):
            row_data = {}
            for j in range(1, col, 1):
                # print type(sheet.row_values(i)[j])
                # row_data[col_name[j]] = sheet.cell(i, j).value
                row_data[col_name[j]] = str(sheet.row_values(i)[j])
                # row_data[col_name[j]] = sheet.cell_value(i, j).encode('utf-8')
                # print row_data
            data.append(row_data)
        # print data
        return data
