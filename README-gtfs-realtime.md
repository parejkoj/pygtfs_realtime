gtfs-realtime
===============

This is the pseudo-literal representing the protocol buffer that
we need to emit as part of the realtime feed.


    header {
      gtfs_realtime_version: "1.0"
      incrementality: FULL_DATASET
      timestamp: feed-creation-time
    }
    entity {
      id: "bus1"
      vehicle: {
        trip: {
          route_id: 1528            # union station shuttle
        }

        vehicle: {
          id: "bus1"                # system assigned
          label: "Bus 1"
          license_plate: "plate1"   
        }
        position: {
          latitude:   41.875928   # WGS-84
          longitude: -87.7010799  # WGS-84
          bearing:
          odometer:
          speed:
        }
      }
    }
    entity {
      id: "vehicle2"
      vehicle: {
        trip: {
          route_id: 1528            # union station shuttle
        }

        vehicle: {
          id: "bus-2"               # system assigned
          label: "Bus 2"
          license_plate: "plate2"   
        }
        position: {
          latitude:   41.875928   # WGS-84
          longitude: -87.7010799  # WGS-84
          bearing:
          odometer:
          speed:
        }
      }
    }
