# -*- coding:utf-8 -*-

from fetch import fetch, parse, fetch_1001
import xlwt
import time


sheetName = {'1000': 'CC UR Top 10',
             '1001': 'Individual UR top 5 per CC',
             '1002': 'Top 50 individual UR in IT&C',
             '1003': 'Nightshift data per CC',
             '1004': 'Individual nightshift in IT&C',
             '1005': 'Remote percentage',
             '1006': 'Service delivery to per region',
             '1007': 'Remote percentage to per region'}

sheetHeader = {'1000': ['Cost_Center', 'Total_Chargable_Hours', 'Headcount', 'Target_Hours', 'UR'],
               '1001': ['Individual_Total_Hours', 'PersonnelRecord', 'PersonnelRecord2', 'SenderCostCenter', 'UR'],
               '1002': ['Individual_Total_Hours', 'PersonnelRecord', 'PersonnelRecord2', 'SenderCostCenter', 'UR'],
               '1003': ['Total_NS_Hours', 'Send_CCtr'],
               '1004': ['Total_NS_Hours', 'Pers_No_', 'Employee_app_name', 'Send_CCtr'],
               '1005': ['Total_HC_Hours', 'Total_Hours', 'Remote_Percentage'],
               '1006': ['ReceivingRegion', 'Region_Hours', 'Percentage'],
               '1007': ['ReceivingRegion', 'Region_HC_Hours', 'Region_Hours', 'Region_Remote_Percentage']}


def output(reports):
    results = {}
    if reports == "ALL":
        reports = "1000,1001,1002,1003,1004,1005,1006,1007"
    templates = reports.split(',')
    for template in templates:
        data = parse('template/%s.xml' % template)
        if template == '1001':
            results[template] = fetch_1001(data['sqls'])
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
