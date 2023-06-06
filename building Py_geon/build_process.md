# Building Py_geon

This will be a short walkthrough of my buildprocess.


## [Frame + Motor's + ESC's](https://github.com/git-blame-BUK/Py_geon/blob/main/building%20Py_geon/Hardware.md#common-drone-electronics)

![IMG_1169](https://github.com/git-blame-BUK/Py_geon/assets/132343254/bc498c9b-ba8d-435e-9460-f87138e1af10)
<sub>The wiring on the bottom here is just the PWM-Pinout to steer the Motors (connects to Pixhawk-Port)</sub>

- [Flightcontroller](https://github.com/git-blame-BUK/Py_geon/blob/main/building%20Py_geon/Hardware.md#py_geons-nervous-system) is positioned upsidedown on the small platform.
- [Boardcomputer](https://github.com/git-blame-BUK/Py_geon/blob/main/building%20Py_geon/Hardware.md#py_geons-brain) is mounted on top of Py_geon with damping pads to reduce vibration.
- [Optical Flow and Proximity Sensor](https://github.com/git-blame-BUK/Py_geon/blob/main/building%20Py_geon/Hardware.md#py_geons-eyes) are mounted facing downwards, maximizing field  of view.
- [GPS](https://github.com/git-blame-BUK/Py_geon/blob/main/building%20Py_geon/Hardware.md#py_geons-map) and Telemtry Modules need to be mounted maximising distance, same goes for the wifi antenna.


## Mission Planner Setup

First Step would be to Download and Install your Flightcontroller Software of choice.
List of all Parameters set in Mission Planner (Ground Station)


Flightcontroller mounted upside Down:

AHRS_ORIENTATION = roll180

### Peripherals:
Telemetry1 Port (Serial1): Proximity Sensor
- SERIAL1_PROTOCOL = “11” (“Lidar360”) if using Serial1
- SERIAL1_BAUD = “115” if using Serial1
- PRX1_TYPE = “8” (LightwareSF45B)
- PRX1_ORIENT = “0” if mounted on the top of the vehicle, “1” if mounted upside-down on the bottom of the vehicle
- PRX1_IGN_ANG1 and PRX1_IGN_WID1 parameters allow defining zones around the vehicle that should be ignored. For example to avoid a 20deg area to the right, set PRX1_IGN_ANG1 to 90 and PRX1_IGN_WID1 to 20

Telemetry2 Port (Serial2): Telemetry Modul
- SERIAL2_PROTOCOL = 2 (MAVLink)
- SERIAL2_BAUD = 57

Telemetry3 Port (Serial5): Boardcomputer
- SERIAL5_PROTOCOL = 2 
- SERIAL5_BAUD = 57

CAN1 Port: Optical Flow
- Set FLOW_TYPE = 6 (DroneCAN)
- Set CAN_P1_DRIVER = 1 to enable DroneCAN
- Set CAN_D1_PROTOCOL = 1 (DroneCAN)
- Set RNGFND1_TYPE = 24 (DroneCAN)
- Set RNGFND1_MAX_CM = 300

GPS is configured out of the box

[Extended Kalman Filter Setup](https://ardupilot.org/copter/docs/common-apm-navigation-extended-kalman-filter-overview.html): EK3 

--> At this Point Py_geon understands the sensor output, but doesnt know what to do with these mesurements. Consequently we need to feed the EKF those parameters.
- Set EK3_SRC1_POSXY: 3 (GPS)
- Set EK3_SRC1_VELXY: 3 (set 5 for Optical FLow Primary) 
- Set EK3_SRC1_POSZ: 1 (Barometer)
- Set EK3_SRC1_VELZ: 3
- Set EK3_SRC1_YAW: 1 (Compass)
- Set EK3_SRC2_VELXY: 5 (Optical Flow/ Set 3 for Secondary GPS)
- Set EK£_SRC2_POSZ: 2 (Rangefinder)



(BatteryMonitoring Pixhawk 6c): Power1 Port
- BATT_MONITOR = 4
- BATT_VOLT_PIN = 8
- BATT_CURR_PIN = 4
- BATT_VOLT_MULT = 18.182
- BATT_AMP_PERVLT = 36.364

## Boardcomputer Setup:
- refer to this [Video](https://www.youtube.com/watch?v=nIuoCYauW3s)

Reference Videos:
- [JetsonNano Setup](https://www.youtube.com/watch?v=nIuoCYauW3s)
- [Pixhawk 6c Video Series](https://www.youtube.com/watch?v=WzM4J_qlEso&t=536s)

  
