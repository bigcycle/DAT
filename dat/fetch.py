# -*- coding:utf-8 -*-

import xml.etree.ElementTree as ET
import MySQLdb
from config import database, months


def parse(file):
    tree = ET.parse(file)
    root = tree.getroot()
    sqls = []
    elems = root.findall("./data/sql")
    sheetName = root.find("./data/sheetName").text
    for elem in elems:
        if elem.text is not None:
            sqls.append(elem.text)
    data = {'sheetName': sheetName, 'sqls': sqls}
    return data


def fetch(sqls, target):
    db = MySQLdb.connect("localhost", "root", "root", database)
    cursor = db.cursor()
    for sql in sqls:
        sql = sql.replace('target_hours', str(months[target]))
        sql = sql.replace('.Hours', '.' + target)
        try:
            cursor.execute(sql)
            # print "curret sql:", sql
        except Exception, e:
            print "SQL Error:", sql
            raise e
    results = cursor.fetchall()
    db.close()
    return results


def fetch2(sqls, target):
    db = MySQLdb.connect("localhost", "root", "root", database)
    cursor = db.cursor()
    results = []
    sqls[3] = sqls[3].replace('target_hours', str(months[target]))
    try:
        row = cursor.execute(sqls[0])
    except Exception, e:
        print "SQL Error:", sqls[0]
        raise e
    try:
        cursor.execute(sqls[1])
    except Exception, e:
        print "SQL Error:", sqls[1]
        raise e
    try:
        cursor.execute(sqls[2])
    except Exception, e:
        print "SQL Error:", sqls[2]
        raise e
    # row = cursor.fetchall()
    for i in range(0, row):
        try:
            cursor.execute(sqls[3] % str(i))
        except Exception, e:
            print "SQL Error:", sqls[3] % str(i)
            raise e
        results += cursor.fetchall()
    db.close()
    return results


def fetch3():
    db = MySQLdb.connect("localhost", "root", "root", database)
    cursor = db.cursor()
    sql = "DESC Finance"
    try:
        cursor.execute(sql)
    except Exception, e:
        print "SQL Error:", sql
        raise e
    sqls = """create temporary table tempFA
select
f1.CostCenter AS Cost_Center,
"""
    sqls2 = "select "
    keys = [x[0] for x in cursor.fetchall()[4:]]
    for key in keys:
        sqls += """f1.month AS month,
((f2.month - CC.ManagerHC) * """.replace('month', key) + str(months[key]) + """) AS month_Target_Hours,""".replace('month', key)
        sqls2 += """(SUM(month) / SUM(month_Target_Hours)) AS month_UR,""".replace('month', key)
    sqls += """CC.Manager AS Manager
from
(select * from Finance where CostCenter in (select CostCenter from CC) AND Item="Total Chargeable hours (All resources)" AND EmployeeGroup='1') f1
inner join
(select * from Finance where CostCenter in (select CostCenter from CC) AND Item="Average Headcount" AND EmployeeGroup='1') f2 on f2.CostCenter = f1.CostCenter
inner join CC on f1.CostCenter = CC.CostCenter
"""
    sqls2 += "("
    sqls2 += " + ".join(map(lambda x: "SUM(month)".replace('month', x), keys))
    sqls2 += ") / ("
    sqls2 += " + ".join(map(lambda x: "SUM(month_Target_Hours)".replace('month', x), keys))
    sqls2 += ") AS YTD_UR,"
    sqls2 += """GROUP_CONCAT(Cost_Center SEPARATOR ' ') AS Cost_Centers,
Manager
from tempFA group by Manager order by YTD_UR DESC
"""
    try:
        cursor.execute(sqls)
        cursor.execute(sqls2)
    except Exception, e:
        print "SQL Error:", sqls
        raise e
    results = cursor.fetchall()
    headers = [key + "_UR" for key in keys]
    headers += ['YTD_UR', 'Cost_Centers', 'Manager']
    db.close()
    return [headers, results]
