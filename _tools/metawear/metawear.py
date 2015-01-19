#!/usr/bin/env python

import sys
import argparse
import subprocess
import os.path
import csv
import json

_git_name = None
_git_email = None

def usage(args):
    parser = argparse.ArgumentParser(description="Convert metawear text file into approved json format")
    parser.add_argument("--subject", "-s", default=full_name())
    parser.add_argument("input_file")
    parser.add_argument("activity")
    parser.add_argument("move", help="The name of the move")

    return parser.parse_args(args)

def git_name():
    global _git_name

    if _git_name is not None:
        return _git_name

    process = subprocess.Popen("git config user.name", shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    out, err = process.communicate()
    errcode = process.returncode

    if errcode:
        return "Unknown"

    _git_name = out.strip()
    return _git_name

def git_email():
    global _git_email

    if _git_email is not None:
        return _git_email

    process = subprocess.Popen("git config user.email", shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    out, err = process.communicate()
    errcode = process.returncode

    if errcode:
        return "Unknown"

    _git_email = out.strip()
    return _git_email

def full_name():
    return "{0} <{1}>".format(git_name(), git_email())

def write(inp, out, contributor, subject, activity, name):
    reader = csv.reader(inp)
    data = {
            "metadata": {
                "activity": activity,
                "name": name,
                "contributor": contributor,
                "subject": subject,
                "sensors": [ "metawear" ]
            },
            "data": [
            ]
    }

    count = 0
    for row in reader:
        converted_row = (float(x) for x in row)
        converted_row = dict(zip(("timestamp", "metawear.x", "metawear.y", "metawear.z"), converted_row))
        data['data'].append(converted_row)
        count += 1
        if count % 10 == 0:
            sys.stdout.write(".")
            sys.stdout.flush()

    json.dump(data, out, indent=2)
    print("Wrote {0} data points".format(count))

def main(args=sys.argv[1:]):
    args = usage(args)

    output_filename = "".join((os.path.splitext(args.input_file)[0], ".json"))

    with open(args.input_file, "rb") as inp:
        with open(output_filename, "w") as out:
            write(inp, out, full_name(), args.subject, args.activity, args.move)

if __name__ == "__main__":
    main()
