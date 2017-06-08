# -*- coding:utf-8 -*-

import xlrd
import xlwt
from config import column


headers = {'FA': ['Item', 'CostCenter', 'EmployeeGroup', 'Jan'],
           'CDT': ['Region', 'PersonnelNo', 'Name', 'Type', 'CostCenter', 'Hours'],
           'MUS': ['Date', 'Hours', 'Type', 'PersonnelNo', 'Name', 'CostCenter']}


def modify(org_file):
    opt = org_file.split('.')[0].split('_')
    file = xlwt.Workbook()
    sheet = file.add_sheet(opt[0])
    c = 0
    for header in headers[opt[0]]:
        sheet.write(0, c, header)
        c += 1
    if opt[0] == "FA":
        modifyFA(org_file, sheet)
    elif opt[0] == "CDT":
        modifyCDT(org_file, sheet)
    elif opt[0] == "MUS":
        modifyMUS(org_file, sheet)
    file.save('source/' + org_file)


def modifyFA(org_file, sheet2):
    data = xlrd.open_workbook(org_file)
    table = data.sheets()[0]
    cols = column['FA']
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
                sheet2.write(r, c, row_datas[col])
                c += 1
            r += 1
        i += 1


def modifyCDT(org_file, sheet):
    data = xlrd.open_workbook(org_file)
    table = data.sheets()[1]
    cols = column['CDT1']
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
    cols2 = column['CDT2']
    rown2 = rown + table2.nrows - 1
    while r < rown2:
        c = 0
        row_datas2 = table2.row_values(r + 1 - rown)
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
        row_datas[1] = row_datas[1].split(',')[0]
        for col in cols:
            sheet.write(r, c, row_datas[col])
            c += 1
        r += 1


# def main():
#     modify('FA_2017_Jan.xlsx')
#     modify('MUS_2017_Jan.xls')
#     modify('CDT_2017_Jan.xls')


# if __name__ == '__main__':
#     main()
