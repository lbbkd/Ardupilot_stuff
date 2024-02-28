#!/usr/bin/env python3
from pymavlink import mavutil

# Initialize a connection listening on a UDP port

master = mavutil.mavlink_connection('udpout:127.0.0.1:14550')

# Wait for a heartbeat, setiing the system component ID of remote system for the link
master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component)
