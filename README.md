# Temperature logging

Interface with the Adafruit DHT sensor and log values to a database. Runs on my Raspberry Pi3 with an adafruit DHT-22 sensor.

## Steps

These are run from the pi by editing the rc.local file and adding the lines:  

```
sudo nano /etc/rc.local

python3 temp.py &
telegraf --config temperatureLog.conf &
```
This runs the above commands at start up so the pi only needs to be plugged in and will automatically start logging values and pushing them to a remote database.

I wanted to periodically truncate the log file so it doesn't become too big and eat up memory. First I needed to change ownership of the `temperature.log` file that is created with the above python process so it can be modified by non-root. 

```
chown <user> -R temperature.log
```

Then I set up a cronjob to truncate the file daily by running the `truncate.sh` file.
