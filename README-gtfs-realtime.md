gtfs-realtime
===============

This is the pseudo-literal representing the protocol buffer that
we need to emit as part of the realtime feed.

FeedMessage {
    FeedHeader {
      gtfs_realtime_version: "1.0"
      timestamp: feed-creation-time
    }
    FeedEntity {
      id: "bus1"
      VehiclePosition: {
        TripDescriptor: {
          route_id: 1528            # union station shuttle
        }
        VehicleDescriptor: {
          id: "bus1"                # system assigned
          label: "Bus 1"
          license_plate: "plate1"   
        }
        Position: {
          latitude:   41.875928   # WGS-84
          longitude: -87.7010799  # WGS-84
          bearing:
          odometer:
          speed:
        }
      }
    }
    FeedEntity {
      id: "vehicle2"
      VehiclePosition: {
        TripDescriptor: {
          route_id: 1528            # union station shuttle
        }

        VehicleDescriptor: {
          id: "bus-2"               # system assigned
          label: "Bus 2"
          license_plate: "plate2"   
        }
        Position: {
          latitude:   41.875928   # WGS-84
          longitude: -87.7010799  # WGS-84
          bearing:
          odometer:
          speed:
        }
      }
    }
