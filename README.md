pytemp
------


Takes the output from a Dallas DS18B20 sensor attached to 3v, GND and GPIO 4 (3v and GPIO have 4.7k resistor attached) and publishes the values to a topic on a redis and mqtt stream.

Relies on boilermaster config file to exist.

extra feature of boilermaster/PiThermostat project.
