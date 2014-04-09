#!/usr/bin/python

import json
import re

def main(data_1pif_file_name):
    hosts = set()
    with open(data_1pif_file_name, 'rb') as data_1pif:
        for line in data_1pif:
            for host in re.findall(r'location":"https:\\/\\/([^\/\\\"\:\#]+)(?:[\/\\\"\#\:])', line):
                hosts.add(host)

    for h in sorted(hosts):
       print(h)

if __name__ == '__main__':
    main('data.1pif');
