#!/usr/bin/env python
"""
Listen for nmea data and produce a GTFS-realtime output.
"""

from __future__ import print_function, division, unicode_literals

import time
import urllib

import pynmea2

# this is built from the gtfs_realtime protocol buffer file via protoc.
import gtfs_realtime_pb2 as gtfs_rt

# The nmea data comes from our verizon hotpoint
nmea_hotpoint = "http://192.168.0.1:8889/"
gtfs_newhaven = "../data/nh_transit/googlenh_transit.zip"

class GTFSrealtimeNMEA(object):
    """Output a new GTFS-realtime from NMEA input."""

    def __init__(self, nmea_stream, gtfs_file=None):
        if 'http' in nmea_stream:
            input_stream = urllib.urlopen(nmea_stream)
            stream = pynmea2.NMEAStreamReader(input_stream)
            self.stream = stream

        if gtfs_file is not None:
            with open(gtfs_file) as gtfs:
                self.gtfs = gtfs

    def next_pvt(self):
        """Return the lat/long/velocity/bearing of the bus, waiting until we get the next packet."""
        # TBD: there's gotta be a better way to do this.
        while True:
            data = self.stream.next()
            # NOTE: we can get the identifier from another field (maybe TPI?)
            if data is None:
                return None
            else:
                try:
                    # GPGGA is the satellite fix.
                    if data[0].sentence_type == 'RMC':
                        break
                except AttributeError:
                    # PCPTI is a proprietary string that we can't parse with pynmea.
                    time.sleep(0.1)
        try:
            data = data[0]
            return data.latitude, data.longitude, data.spd_over_grnd, data.true_course
        except AttributeError as e:
            print(data[0],type(data[0]))
            return None

    def make_message(self):
        """Make a full gtfs_realtime message with a header and entities."""
        lat,long,spd,bearing = self.next_pvt()
        self.make_header()
        self.make_one_entity(lat,long,spd,bearing)
        message = gtfs_rt.FeedMessage()
        message.header.CopyFrom(self.header)
        # TBD: let this loop over many entities.
        message.entity.extend([self.entity,])
        self.message = message

    def make_header(self):
        """Create a gtfs header"""
        header = gtfs_rt.FeedHeader()
        header.gtfs_realtime_version = "1.0"
        header.timestamp = long(time.time())
        self.header = header

    def make_one_entity(self, lat, long, speed, bearing, busid="somebus"):
        """Create a gtfs entity for a bus."""
        fe = gtfs_rt.FeedEntity(id=busid)
        fe.vehicle.trip.route_id = "1528"
        fe.vehicle.vehicle.id = busid
        fe.vehicle.vehicle.label = busid
        fe.vehicle.vehicle.license_plate = busid
        fe.vehicle.position.longitude = lat
        fe.vehicle.position.latitude = long
        fe.vehicle.position.speed = speed
        # fe.vehicle.position.bearing = bearing 
        self.entity = fe

    def __call__(self):
        """Return a gtfs-realtime protocol buffer string."""
        self.make_message()
        return self.message#.SerializeToString()


onebus = GTFSrealtimeNMEA(nmea_hotpoint, gtfs_newhaven)
while True:
    bus_string = onebus()
    print(bus_string)

#while True:
#    print(onebus.next_pvt())

