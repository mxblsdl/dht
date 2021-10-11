# Temperature logging

Interface with the Adafruit DHT sensor and log values to a database. Runs on my Raspberry Pi3 with an adafruit DHT-22 sensor.

1) Run temp.py to start logging temp values
2) Start telegraf to push the temp log to the Influx DB

## Steps

These are run from the pi by editing the rc.local file and adding the lines:  

```
sudo nano /etc/rc.local

python3 temp.py &
telegraf --config temperatureLog.conf &
```

## TODOS
- Change the user that runs startup commands
  - This will cause the log file to be created by user `pi`
- Create a cron job that runs truncate.sh periodically
  - Can only truncate file that user created
  - Would rather run truncate as non-root
