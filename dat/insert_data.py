# -*- coding:utf-8 -*-

import MySQLdb
import xlrd
from config import database, months
from .createtable import createtable


def insertdb(table, db, cursor, _headers, __table__):
    rows = table.nrows
    print "%d records founds, start to insert to table.\n" % (rows - 1)
    col = ""
    he = ', '.join(_headers)
    i = 1
    while i < rows:
        row_datas = table.row_values(i)
        for _header in _headers:
            if _header in months.keys() + ["Hours", "ManagerHC", "YTD", "R3M"]:
                if row_datas[_headers.index(_header)] != '':
                    col = col + \
                        "%d, " % int(row_datas[_headers.index(_header)])
                else:
                    col = col + "%d, " % 0
            else:
                if isinstance(row_datas[_headers.index(_header)], float):
                    row_datas[_headers.index(_header)] = int(
                        row_datas[_headers.index(_header)])
                else:
                    row_datas[_headers.index(_header)] = row_datas[_headers.index(_header)].strip()
                col = col + '"%s", ' % row_datas[_headers.index(_header)]
        # col = modify_data(col)
        sql_insert = "insert into %s (%s) values (%s)" % (
            __table__, he, col[:-2])
        try:
            cursor.execute(sql_insert)
            db.commit()
        except Exception, e:
            print 'error', sql_insert, '\n'
            raise e
            db.rollback()
        col = ""
        if i % 500 == 0:
            print "%d records has been inserted..." % i
        i += 1
    print "%d records have been inserted..." % (i - 1)


def insert(file, table, init):
    data = xlrd.open_workbook('source/%s' % file.split('.')[0] + ".xls")
    sheet_data = data.sheets()[0]
    headers = []
    headers.extend(sheet_data.row_values(0))
    # headers = modify_header(_headers)
    if init == 0:
        print "Initialize the table for the first import...\n"
        createtable(table, headers)
    else:
        print "Add data to table %s \n" % table
    db = MySQLdb.connect("localhost", "root", "root", database)
    cursor = db.cursor()
    insertdb(sheet_data, db, cursor, headers, table)
    db.close()
