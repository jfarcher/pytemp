#!/usr/bin/python
import os
import glob
import time
import redis
import datetime
import sys
import signal
from ConfigParser import SafeConfigParser
import paho.mqtt.client as mqtt


#make sure modules are loaded 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
def signal_handler(signal, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

parser = SafeConfigParser()
parser.read('/etc/boilermaster/boilermaster.conf')  

rbroker = parser.get('redis', 'broker')
mbroker = parser.get('mqtt', 'broker')
rtcpport = parser.get('redis', 'port')
mtcpport = parser.get('mqtt', 'port')
topic = parser.get('temps', 'topic')
mqttc = mqtt.Client()
devID="A2"
mypid = os.getpid()


#Connect to broker
redthis = redis.StrictRedis(host=rbroker,port=rtcpport, db=0)
mqttc.connect (mbroker, mtcpport, 60)

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp = round(float(temp_string) / 1000.0,1)
        return temp
	
while True:
	temp=read_temp()
	redthis.set(topic + devID + "/sensor",temp)
     	mqttc.publish(topic + devID + "/sensor",temp, retain=True)
	time.sleep(30)
