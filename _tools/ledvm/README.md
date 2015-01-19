# LedVm Converter

This script takes the normal json format and converts it to a simple csv file format for using
with the ledvm simulator.

I'm lazy and didn't want to have to write a json parser in c++, so I use a very simple csv
file format to enable loading the files.

## Usage

```
$ python toledvm.py test.json
........Write 140 rows
```
