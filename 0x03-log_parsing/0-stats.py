#!/usr/bin/python3
"""
Task

0. Log parsing

Write a script that reads stdin line by line and computes metrics:

    - Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size> (if the format is not this one, the line must be
    skipped)
    - After every 10 lines and/or a keyboard interruption (CTRL + C), print
    these statistics from the beginning:
        * Total file size: File size: <total size>
        * where <total size> is the sum of all previous <file size> (see input
        format above)
        * Number of lines by status code:
            - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            - if a status code doesn’t appear or is not an integer, don’t print
            anything for this status code
            - format: <status code>: <number>
            - status codes should be printed in ascending order
Warning: In this sample, you will have random value - it’s normal to not have
the same output as this one.
"""
import sys
from datetime import date, time
import re


def validateLine(line):
    """
    Validates line by returning True or False based on whether or not  it
    matches the specfified pattern
    """
    valid = re.compile(
            r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
            r'\[[^\]]+\] "GET /projects/260 HTTP/1.1" \d{3} \d+')
    if valid.match(line):
        e_time = line.split('[')[1].split(']')[0]
        e_date = e_time.split()[0]
        e_time = e_time.split()[1]
        try:
            if ((isinstance(date.fromisoformat(e_date), date)) and
                    (isinstance(time.fromisoformat(e_time), time))):
                return True
        except ValueError:
            return False


count = size = 0
status_num = {}
status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
try:
    for line in sys.stdin:
        count += 1
        tokens = line.split()
        if validateLine(line):
            if len(tokens) > 7:
                try:
                    status = int(tokens[7])
                except ValueError:
                    status = None
                size += int(tokens[8])

            if status is not None:
                if str(status) in status_num:
                    status_num[str(status)] += 1
                else:
                    status_num[str(status)] = 1
        else:
            if len(tokens) >= 2:
                tmp_status = tokens[len(tokens) - 2]
                if tmp_status in status_codes:
                    if tmp_status in status_num:
                        status_num[tmp_status] += 1
                    else:
                        status_num[tmp_status] = 1
            try:
                tmp_size = int(tokens[len(tokens) - 1])
                size += tmp_size
            except ValueError:
                pass
        if count == 10:
            print('File size: {}'.format(size))
            for status in status_codes:
                if status in status_num:
                    print('{}: {}'.format(status,
                                          status_num[str(status)]))
            count = 0
    print('File size: {}'.format(size))
    for status in status_codes:
        if status in status_num:
            print('{}: {}'.format(status, status_num[str(status)]))
except KeyboardInterrupt as e:
    print('File size: {}'.format(size))
    print(e)
