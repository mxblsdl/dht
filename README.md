# Temperature logging

Interface with the Adafruit DHT sensor and log values to a database. Runs on my Raspberry Pi3 with an adafruit DHT-22 sensor.

1) Run temp.py to start logging temp values
2) Start telegraf to push the temp log to the Influx DB

## Steps

Run these commands at start up:

python3 temp.py

telegraf --config temperatureLog.conf

## TODOs
1) Create startup service to run bash command on startup
2) ~~Create bash script to run python logging and telegraf~~
    - Created a bash script, `run.sh` that calls python
    - Create a bash script, `run_telegraf.sh` that calls telegraf
        - run `chmod 744 run.sh & chmod 744 run_telegraf.sh` to make them executable
    - Run with `~/dht/run.sh` or `~/dht/run_telegraf.sh`
3) Write python to connect to postgres DB
    - Push influsxDB to postgres
4) Tester
