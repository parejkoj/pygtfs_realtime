#!/usr/bin/env python
"""
Listen for nmea data and produce a GTFS-realtime output.
"""

from future import print_function, division, unicode_literals

import pynmea2
import transitfeed

import urllib

class GTFSrealtimeNMEA(object):
    """Output a new GTFS-realtime from NMEA input."""

    def __init__(nmea_stream, gtfs_stream):
        with open(nmea_stream) as input_tream:
            stream = pynmea2.NMEAStreamReader(input_stream)
            self.stream = stream
        with open(gtfs_file) as gtfs:


    def get_next_position():
        """Return the lat/long of the bus."""
        data = self.stream.next()
        return data[0].longitude, data[0].latitude

    def __call__():
        """Return a gtfs-realtime protocol buffer string."""
        return None

gtfsrt = GTFSrealtimeNMEA("../data/sample-nmea.txt"):
