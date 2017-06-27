# -*- coding:utf-8 -*-

import MySQLdb


def createtable(table, headers):
    sql = "create table %s ( `id` smallint not null auto_increment," % table
    for header in headers:
        if header == "Hours" or header == "ManagerHC":
            sql = sql + " `%s` int," % header
        else:
            sql = sql + " `%s` varchar(50)," % header
    sql = sql + "primary key (`id`)) engine=innodb default charset=utf8"
    db = MySQLdb.connect("localhost", "root", "root", "Data")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS %s" % table)
    cursor.execute(sql)
    cursor.execute("DESC %s" % table)
    # results = cursor.fetchall()
    # print results
    db.close()
