# -*- coding:utf-8 -*-

import getopt
import sys
from dat.insert_data import insert
from dat.output import output, write
from dat.modify_table import modify

help = 'Usage: python DAT.py [OPTION]...\n\n'
help += '''Operation Mode options:
-i                                  Import mode
-o                                  Output mode
-h | --help                         Print help and exit.
\n'''
help += '''Import options: (with '-i' option)
-a | --init                     Whether create table, only used when the first time of import operation for each table
\n'''
help += '''Output options: (with '-o' option)
-r | --report                   Templates which will be included in the report, if more than one template,use ',' to seperate.
                                e.g: '-r 1000,1001,1002'
                                If all the templates need to be included use '-r ALL'
-t | --target                   Target hours for current month.
\n'''


def get_para(argv):
    para = {'__target__': '',
            '__init__': 0,
            '__mode__': 0,
            '__report__': ''}
    try:
        opts, args = getopt.getopt(
            argv, "hioat:r:",
            ['help', 'report', 'add', 'target'])
    except getopt.GetoptError:
        print "try 'DAT.py --help' or 'DAT.py -h' for more options"
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print 'python DAT.py -i <file> [-a]'
            print 'python DAT.py -o -r <report> -t <target_hours>'
            print help
            sys.exit()
        elif opt in ("-i", ):
            para['__mode__'] = 1
        elif opt in ("-o",):
            para['__mode__'] = 2
        elif opt in ("-a", "--add"):
            para['__init__'] = 1
        elif opt in ("-r", "--report"):
            para['__report__'] = arg
        elif opt in ("-t", "--target"):
            para['__target__'] = arg
    if len(args) > 0:
        para['__file__'] = args[0]
    return para


def main(para):
    if para['__mode__'] == 1:
        table = modify(para['__file__'])
        print "Start to import data to table %s ...\n" % table
        insert(para['__file__'], table, para['__init__'])
    elif para['__mode__'] == 2:
        write(output(para['__report__'], para['__target__']))


if __name__ == '__main__':
    para = get_para(sys.argv[1:])
    main(para)
