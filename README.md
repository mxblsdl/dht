# Temperature logging

Interface with the Adafruit DHT sensor and log values to a database

1) Run temp.py to start logging temp values
2) Start telegraf to push the temp log to the Influx DB

## Steps

Run these commands at start up:


python3 temp.py
telegraf --config temperatureLog.conf