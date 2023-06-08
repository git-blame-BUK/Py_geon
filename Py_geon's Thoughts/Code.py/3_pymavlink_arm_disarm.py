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

#arming/disarming command
the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,0,
         int(input("input arming mode(arm=1 disarm=0): ")), 0, 0, 0, 0, 0, 0)

msg = the_connection.recv_match(type="COMMAND_ACK",blocking=True)
print(msg)
