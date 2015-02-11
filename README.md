pytemp
------
Python script which runs on a Raspberry Pi, taking the output from a Dallas DS18B20 sensor attached to 3v, GND and GPIO 4 (3v and GPIO have 4.7k resistor attached) and publishes the values to a topic on a redis and mqtt stream.

Relies on boilermaster config file to exist. (/etc/boilermaster/boilermaster.conf)
Installation
------------
Take the pytemp.py file and drop it in /usr/local/bin, make sure it is writeable
Next copy the pytemp.conf file to /etc/init
Make sure the boilermaster config file exists and contains details 

```
[mqtt]
broker=brokerserver
port=1883
[redis]
broker=brokerserver
port=6379
[temps]
topic=temp/sensor/topic
```

```
start pytemp
```

Will start the script as a service - it will also auto start on boot.

extra feature of boilermaster/PiThermostat project.
