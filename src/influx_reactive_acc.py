#!/usr/bin/env python3
'''
Based on RuuviTagReactive to fetch Acceleration data from RuuviTag
and store in local InfluxDB
'''

from ruuvitag_sensor.ruuvi_rx import RuuviTagReactive
from influxdb import InfluxDBClient


tags = {
    'E1:01:A3:68:9A:0E': 'Kitchen',
    'E5:D4:32:DB:C8:09': 'Bicycle'
}

class Acceleration(RuuviTagReactive):


    def store_sensor_data(data):
        print(data['acceleration'])

        json_body = [
            {
                "measurement": "Acceleration",
                "tags": {
                    "sensornamn": "Kitchen",
                },
                "fields": {
                    "acceleration_x": data['acceleration_x'],
                    "acceleration_y": data['acceleration_y'],
                    "acceleration_z": data['acceleration_z']
                }
            }
        ]
        client = InfluxDBClient('localhost', 8086, 'root', 'root', 'db_ruuvitag')
        client.write_points(json_body)

#print(list(tags.keys()))

ruuvi_rx = RuuviTagReactive(list(tags.keys()))

# Execute only every time when acceleration changes
ruuvi_rx.get_subject().\
    filter(lambda x: x[0] == 'E1:01:A3:68:9A:0E').\
    distinct_until_changed(lambda x: x[1]['acceleration']).\
    subscribe(lambda x: Acceleration.store_sensor_data(x[1]))
