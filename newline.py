#!/usr/bin/env python

import sys
import json


def fix_dict(d):
    n = {}
    for key in d.keys():
        new_key = key.replace(' ', '_').replace('-', '_')
        if isinstance(d[key], dict):
            k = d[key]
            n[new_key] = fix_dict(d[key])
        else:
            n[new_key] = d[key]
    return n


with open(sys.argv[1], 'r') as f:
    file_list = f.readlines()

for filename in file_list:
    with open(filename.rstrip(), 'r') as f, open('./newlinedelimited.json', 'a') as o:
        try:
            j = json.loads(f.read())
            k = fix_dict(j)
            print(filename.rstrip())
            o.write(str(k) + '\n')
        except Exception as e:
            continue
