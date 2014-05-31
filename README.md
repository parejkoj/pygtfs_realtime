pygtfs_realtime
===============

Python NMEA to GTFS-realtime converter, #hackday2014

Dependencies
============

All dependencies should be available via pip.

numpy
pynmea2 - https://github.com/Knio/pynmea2
transitfeed - https://code.google.com/p/googletransitdatafeed/wiki/TransitFeed
protobuf - https://developers.google.com/protocol-buffers/

Setup
=====

When setting up this application, we'll need to build the protocol buffer format:

protoc --python_out=./ gtfs-realtime.proto

