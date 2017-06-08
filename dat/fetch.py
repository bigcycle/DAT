# -*- coding:utf-8 -*-

import xml.etree.ElementTree as ET
import MySQLdb


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


def fetch(sqls):
    db = MySQLdb.connect("localhost", "root", "root", "Data")
    cursor = db.cursor()
    for sql in sqls:
        try:
            cursor.execute(sql)
            # print "curret sql:", sql
        except Exception, e:
            print "SQL Error:", sql
            raise e
    results = cursor.fetchall()
    db.close()
    return results


def fetch_1001(sqls):
    db = MySQLdb.connect("localhost", "root", "root", "Data")
    cursor = db.cursor()
    results = []
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
        results += [()]
    db.close()
    return results
