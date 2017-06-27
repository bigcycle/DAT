# -*- coding:utf-8 -*-

import xlrd
import xlwt
from config import column, headers


def modify(org_file):
    opt = org_file.split('.')[0].split('_')
    file = xlwt.Workbook()
    sheet = file.add_sheet(opt[0])
    c = 0
    for header in headers[opt[0]]:
        sheet.write(0, c, header)
        c += 1
    if opt[0] == "Finance":
        modifyFinance(org_file, sheet, opt[1])
    elif opt[0] == "CDT":
        modifyCDT(org_file, sheet, opt[1])
    elif opt[0] == "MUS":
        modifyMUS(org_file, sheet)
    file.save('source/' + org_file)
    return opt[0]


def modifyFinance(org_file, sheet, month):
    data = xlrd.open_workbook(org_file)
    table = data.sheets()[0]
    temp_row = map(lambda x: x.strip()[:3], table.row_values(31))
    temp_col = temp_row.index(month)
    cols = column['Finance']
    cols.append(temp_col)
    i = 33
    r = 1
    rown = table.nrows
    while i < rown:
        c = 0
        row_datas = table.row_values(i)
        if "Result" not in row_datas and "Overall Result" not in row_datas and\
            ("Total Chargeable hours (All resources)" in row_datas or
             "Average Headcount" in row_datas):
            for col in cols:
                sheet.write(r, c, row_datas[col])
                c += 1
            r += 1
        i += 1


def modifyCDT(org_file, sheet, month):
    data = xlrd.open_workbook(org_file)
    table = data.sheets()[1]
    temp_row = table.row_values(0)
    temp_col = temp_row.index(month)
    cols = column['CDT1']
    cols.append(temp_col)
    r = 1
    rown = table.nrows
    while r < rown:
        c = 0
        row_datas = table.row_values(r)
        for col in cols:
            sheet.write(r, c, row_datas[col])
            c += 1
        r += 1
    table2 = data.sheets()[2]
    temp_row2 = table2.row_values(0)
    temp_col2 = temp_row2.index(month)
    cols2 = column['CDT2']
    cols2.append(temp_col2)
    rown2 = rown + table2.nrows - 1
    while r < rown2:
        c = 0
        row_datas2 = table2.row_values(r + 1 - rown)
        row_datas2[1] = row_datas2[1].replace('#', 'TTM')
        for col2 in cols2:
            sheet.write(r, c, row_datas2[col2])
            c += 1
        r += 1


def modifyMUS(org_file, sheet):
    data = xlrd.open_workbook(org_file)
    table = data.sheets()[0]
    cols = column['MUS']
    r = 1
    rown = table.nrows
    while r < rown:
        c = 0
        row_datas = table.row_values(r)
        # row_datas[1] = row_datas[1].split(',')[0]
        for col in cols:
            sheet.write(r, c, row_datas[col])
            c += 1
        r += 1

# def main():
#     modify('Finance_2017_Jan.xlsx')
#     modify('MUS_2017_Jan.xls')
#     modify('CDT_2017_Jan.xls')


# if __name__ == '__main__':
#     main()
