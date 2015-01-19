# movement
Freely available accelerometer data for analysis and other uses.

This is my repository for movement data that I've collected from various activities.  Each top level directory ~~is~~ will be
the type of activity, and the individual files will be based on the different movements within that activity.

Licensed under the MIT License, but if you use the data for something, it would be awesome if you let me know so I
can tell what's useful and what isn't.

Also, if you'd like to contribute data, please feel free to send a pull request.  I ask that the data is provided in the file format
listed below

# file format

The files are formatted as a json file in the following form:

```json
{
   "metadata": {
      "contributor": "Russell Hay",
      "activity": "parkour",
      "name": "parkour roll",
      "sensors": [
          "metawear"
      ]
   },
   "data": [
      { "timestamp": "12345",
        "metawear.x": "123.0",
        "metawear.y": "123.0",
        "metawear.z": "123.0"
      }
   ]
}

```

The metadata section just describes the type of data collected, and correlates mostly with the file structure, but adds contributor and
information about the sensor used to collect the data.

The data section is an array of dictionaries with a required element of timestamp, which should be a monotonically increasing number
(int or float) that represents the progression of time for ordering purposes.

The rest of the dictionary is dependent on the sensors.  If the sensor has multiple DOF, you will construct a common name for the data point
in the form of ```[sensor name].[degree]```.  As in the example above, the metawear sensor has x,y, and z, so we include an x,y,z.  
Each dictionary in the array should have the same set of keys.
