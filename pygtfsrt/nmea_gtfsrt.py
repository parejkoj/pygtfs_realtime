#!/usr/bin/env python
"""
Listen for nmea data and produce a GTFS-realtime output.
"""

from future import print_function, division, unicode_literals

import pynmea2

testfile = "../data/sample-nmea.txt"

with open(testfile, 'r') as test_data:
    nmea_stream = pynmea2.NMEAStreamReader(stream_obj=test_data)
    data = nmea_stream.next()
    lat,lon = data[0].longitude, data[0].latitude
