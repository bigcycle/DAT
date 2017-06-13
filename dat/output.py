# -*- coding:utf-8 -*-

from fetch import fetch, parse, fetch2
import xlwt
import time
from config import sheetHeader, sheetName


def output(reports):
    results = {}
    if reports == "ALL":
        reports = "1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010"
    templates = reports.split(',')
    for template in templates:
        data = parse('template/%s.xml' % template)
        if template == '1007' or template == '1008':
            results[template] = fetch2(data['sqls'])
        else:
            results[template] = fetch(data['sqls'])
    # for k, v in results.items():
    #     print k, v, '\n'
    return results


def write(results):
    file = xlwt.Workbook()
    for k, v in results.items():
        table = file.add_sheet(sheetName[k])
        r = 1
        c = 0
        for header in sheetHeader[k]:
            table.write(0, c, header)
            c += 1
        for row in v:
            c = 0
            for cell in row:
                table.write(r, c, cell)
                c += 1
            r += 1
    file.save('report/DAT_report_%s.xls' %
              time.strftime('%Y%m%d', time.localtime()))
