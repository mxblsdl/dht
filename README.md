# Temperature logging

Interface with the Adafruit DHT sensor and log values to a database. Runs on my Raspberry Pi3 with an adafruit DHT-22 sensor.

1) Run temp.py to start logging temp values
2) Start telegraf to push the temp log to the Influx DB

These are accomplished through the conf file that connects to the influx DB and the python file that reads data from the temp sensor.

The data will be read and visualized through a TBD project

## Steps

These are run from the pi by editing the rc.local file and adding the lines:  

```
sudo nano /etc/rc.local

python3 temp.py &
telegraf --config temperatureLog.conf &
```

The ampersands are added to make the processes non-blocking.

Could also be run with:

    - Created a bash script, `run.sh` that calls python
    - Create a bash script, `run_telegraf.sh` that calls telegraf
        - run `chmod 744 run.sh & chmod 744 run_telegraf.sh` to make them executable
    - Run with `~/dht/run.sh` or `~/dht/run_telegraf.sh`
