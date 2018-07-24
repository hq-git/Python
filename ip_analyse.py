#!/bin/env python

# cat www.edanzediting.co.jp-access_log-20180722 |awk '{print $1}' |sort |uniq -c |sort -k1nr |head -n 10

import sys


def get_record():
    '''
    get all access record from log file
    :return: 1 (if with less parameters)
    '''
    record = {}
    if len(sys.argv) == 1:
        print("usage: python %s logfile_name [num] [date]" % __file__)
        return 1

    filename = sys.argv[1]

    with open(filename, 'r') as f:
        for line in f:
            line_list = line.split(" ")
            ip = line_list[0]
            time = line_list[3].replace('[', '')
            time_list = time.split('/')
            month_d = '/'.join(time_list[:2])
            if month_d not in record:
                record[month_d] = {}
                record[month_d][ip] = 1
            else:
                if ip not in record[month_d]:
                    record[month_d][ip] = 1
                else:
                    record[month_d][ip] += 1
    print(record)


def record_sort(num,date=''):

    '''
    Sort result
    :return:
    '''

    pass


def get_result():
    '''
    Display previous data
    :return:
    '''
    pass


if __name__ == '__main__':
    get_record()
