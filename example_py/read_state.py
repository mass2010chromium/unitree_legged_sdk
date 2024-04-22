#!/usr/bin/python

import sys
import time
import math

sys.path.append('../lib/python/amd64')
import robot_interface as sdk


if __name__ == '__main__':

    HIGHLEVEL = 0xee
    LOWLEVEL  = 0xff

    udp = sdk.UDP(HIGHLEVEL, 8080, "192.168.123.161", 8082)

    cmd = sdk.HighCmd()
    state = sdk.HighState()
    udp.InitCmdData(cmd)

    motiontime = 0
    while True:
        time.sleep(0.002)
        motiontime = motiontime + 1

        udp.Recv()
        udp.GetRecv(state)
        
        v_lin = state.velocity
        v_ang = state.yawSpeed
        print(f"{motiontime:05d} | Velocity: {v_lin}")
        print(f"{motiontime:05d} | Yaw rate: {v_ang}")

        udp.SetSend(cmd)
        udp.Send()
