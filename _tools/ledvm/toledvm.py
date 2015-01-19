#!/usr/bin/env python

import sys
import argparse
import subprocess
import os.path
import csv
import json

FIELDS = ("metawear.x", "metawear.y", "metawear.z")

class Counter(object):
    def __init__(self):
        self._count = 0

    def __call__(self):
        self._count += 1
        if (self._count % 10 == 0):
            sys.stdout.write('.')
            sys.stdout.flush()
        return self._count

    @property
    def count(self):
        return self._count

def usage(args):
    parser = argparse.ArgumentParser(description="Convert json file to simulator csv")
    parser.add_argument("input_file")

    return parser.parse_args(args)

def fixup_row(row, counter):

    return [counter()] + [row[x] for x in FIELDS]

def write(inp, out):
    writer = csv.writer(out)
    data = json.load(inp)['data']

    count = Counter()
    rows = (fixup_row(x, count) for x in data)
    writer.writerow(("index",) + FIELDS)
    writer.writerows(rows)

    print("Wrote {0} rows".format(count.count))

def main(args=sys.argv[1:]):
    args = usage(args)

    output_filename = "".join((os.path.splitext(args.input_file)[0], ".csv"))

    with open(args.input_file, "rb") as inp:
        with open(output_filename, "w") as out:
            write(inp, out)

if __name__ == "__main__":
    main()
