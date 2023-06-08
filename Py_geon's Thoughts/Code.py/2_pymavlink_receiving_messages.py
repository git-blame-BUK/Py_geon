########################## Py_geon #####################
## Author: BUK
## listen for mavlink Heartbeats
from pymavlink import mavutil

# Start a conncection listening on corresponding serial interface 
# Baudrate(57600) can vary depending on your connected Serial flightcontroller Port (might be e.g. 115 200)
the_connection = mavutil.mavlink_connection("/dev/ttyTHS1", 57600)

# wait for Heartbeat( sets SystemID and ComponentID)
the_connection.wait_heartbeat()
  print(f"Heartbeat from system (SystemID: {the_connection.target_system}, ComponentID: {the_conenction.target_component})")

# receive mavlink Messages(e.g. Attitude)
while 1:
  msg = the_connection.recv_match(type="ATTITUDE", blocking=True)
