# -*- coding:utf-8 -*-

import xlrd
import xlwt
from config import column, headers, column_names


def modify(org_file):
    opt = org_file.split('.')[0].split('_')
    file = xlwt.Workbook()
    sheet = file.add_sheet(opt[0])
    if opt[0] != 'Finance':
        c = 0
        for header in headers[opt[0]]:
            sheet.write(0, c, header)
            c += 1
    if opt[0] == "Finance":
        modifyFinance(org_file, sheet, opt[0])
    elif opt[0] == "CDT":
        modifyCDT(org_file, sheet, opt[1])
    elif opt[0] == "MUS":
        modifyMUS(org_file, sheet)
    elif opt[0] == "CC":
        modifyCC(org_file, sheet)
    elif opt[0] == "LeftEmp":
        modifyLeftEmp(org_file, sheet)
    file.save('source/' + org_file.split('.')[0] + ".xls")
    return opt[0]


def modifyFinance(org_file, sheet, header_key):
    data = xlrd.open_workbook(org_file)
    table = data.sheets()[0]
    temp_row = map(lambda x: x.strip()[:7], table.row_values(30))
    temp_col = temp_row.index("Overall")
    cols = [x for x in range(0, temp_col)]
    for x in [2, 4, 5]:
        cols.remove(x)
    header_row = map(lambda x: x.strip()[:3], table.row_values(31))
    headers[header_key] = headers[header_key] + header_row[6:temp_col]
    c = 0
    for header in headers[header_key]:
        sheet.write(0, c, header)
        c += 1
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
    table = data.sheet_by_name(u'Source Data')
    # temp_row = table.row_values(0)
    # temp_col = temp_row.index(month)
    # ytd_col = temp_row.index("YTD")
    # cols = column['CDT1']
    # cols.append(temp_col)
    # cols.append(ytd_col)
    column_names['CDT1'].insert(-1, month)
    cols = getColumns(table.row_values(0), column_names['CDT1'])
    read_row = 1
    write_row = 1
    rownum = table.nrows
    while read_row < rownum:
        c = 0
        row_datas = table.row_values(read_row)
        if row_datas[1].strip() != '':
            for col in cols:
                sheet.write(write_row, c, row_datas[col])
                c += 1
            write_row += 1
        read_row += 1
    table2 = data.sheet_by_name(u'Unassigned&TTM')
    # temp_row2 = table2.row_values(0)
    # temp_col2 = temp_row2.index(month)
    # ytd_col2 = temp_row2.index("YTD")
    # cols2 = column['CDT2']
    # cols2.append(temp_col2)
    # cols2.append(ytd_col2)
    column_names['CDT2'].insert(-1, month)
    cols2 = getColumns(table2.row_values(0), column_names['CDT2'])
    rownum2 = table2.nrows
    read_row = 1
    while read_row < rownum2:
        c = 0
        row_datas2 = table2.row_values(read_row)
        if row_datas2[1].strip() != '':
            row_datas2[1] = row_datas2[1].replace('#', 'TTM')
            for col2 in cols2:
                sheet.write(write_row, c, row_datas2[col2])
                c += 1
            write_row += 1
        read_row += 1


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
            if col == 12:
                row_datas[col] = row_datas[col].strip()
            sheet.write(r, c, row_datas[col])
            c += 1
        r += 1


def modifyCC(org_file, sheet):
    data = xlrd.open_workbook(org_file)
    table = data.sheets()[0]
    cols = column['CC']
    rown = table.nrows
    i = 4
    while i < rown:
        c = 0
        row_datas = table.row_values(i)
        # row_datas[1] = row_datas[1].split(',')[0]
        for col in cols:
            sheet.write(i - 3, c, row_datas[col])
            c += 1
        i += 1


def modifyLeftEmp(org_file, sheet):
    data = xlrd.open_workbook(org_file, encoding_override='utf-8')
    table = data.sheets()[0]
    cols = [1, 2, 0]
    rown = table.nrows
    i = 1
    while i < rown:
        c = 0
        row_datas = table.row_values(i)
        for col in cols:
            if not isinstance(row_datas[col], float):
                row_datas[col] = row_datas[col].strip()
            sheet.write(i, c, row_datas[col])
            c += 1
        i += 1


def getColumns(row_value, column_names):
    columns = []
    for column_name in column_names:
        try:
            column = row_value.index(column_name)
            columns.append(column)
        except Exception, e:
            print "Can't find %s in current row." % column_name
            raise e
            return False
        row_value[column] = "dummy"
    return columns
