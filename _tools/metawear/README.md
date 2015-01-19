# Metawear Conversion Tool

The default metawear application allows you to email logged data to yourself.  It's not the best
solution for collecting this data, but it works well enough to not reinvent the wheel.

The python script in this directory reads a file as emailed from the metawear app and converts it to
the appropriate json format.  Subject is added via a command line option.  If left blank,
the script uses your git information to collect subject, and always uses git to add contributor.

## Usage

```
$ python metawear.py --subject "Russell Hay" test.txt

..........wrote 140 data points
```
