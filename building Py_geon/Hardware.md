## Hardware

Drone Frame:
- has to be caged for indoor use. Very sturdy and small (about 30 cm)
- enough space for the Jetson nano
- upgradeable in case of to much weight of the drone

![Lumenier-QAV-PRO-Whoop](https://user-images.githubusercontent.com/132343254/236219350-0d03d53f-6027-4b08-a7c0-212d61e7babc.jpg)



## Common Drone Electronics 
Motors:
Holybro --2206

--> Creates the drones thrust

ESC:(ElectronicSpeedController)
BLHeli 20A ESCS

--> Regulating motor speed

PDB:(PowerDistributionBoard)
Holybro PM06v2

--> Distributes power to e.g. ESC's or Flightcontroller

Battery:
Lipo 4s 2200mah

--> Power storage. Has to be handled with care (Deep Discharging is very Dangerous)

Telemetry:
Holybro FPV Telemetrie Set V3

--> Communication between flightcontroller and groundstation. Only for failsafe purposes

## Specific Drone Electronics


### Py_geon's Nervous System

Holybro pixhawk 6c - Flightcontroller

![Pixhawk6C](https://user-images.githubusercontent.com/132343254/235888053-6c7279e5-fbce-4cd0-9dac-f84b8f615978.png)

- Lightweight about 35g
- Highly customizable
- Precise docs on either PX4 or [Ardupilot](https://ardupilot.org/copter/index.html) Software.


### Py_geon's Brain

Nvidia Jetson Nano Developer Kit 4GB - B01

![jetson-nano-commercial-developer-kit-kv-2c50-d](https://user-images.githubusercontent.com/132343254/235887570-7a410b7c-e259-4acc-8224-0abd81ca78f7.jpg)

- State of the art embbeded linux
- lightweight given the capabilitys it provides
- insanely power efficency (5W on lowPowerMode)

### Py_geon's Eyes

Lightware SF45/B Lidar:
- A lidar is a laser based rangefinder
- Lidar's are leightweight, small and more relible then e.g. Sonars
- in this case a omnidirectional one --> Py_geon see's a 2 dimensional map within 50 m

![SF45-20Hero_V001_600x600](https://user-images.githubusercontent.com/132343254/235890863-76cda089-e446-4db2-8dc6-bc1332735bba.jpg)

