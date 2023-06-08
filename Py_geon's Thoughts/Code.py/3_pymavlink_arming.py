


#arming command
the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,0,
         int(input("input arming mode(arm=1 disarm=0): ")), 0, 0, 0, 0, 0, 0)

msg = the_connection.recv_match(type="COMMAND_ACK",blocking=True)
print(msg)
