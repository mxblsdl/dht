# Temperature logging

Interface with the Adafruit DHT sensor and log values to a database. Runs on my Raspberry Pi3 with an adafruit DHT-22 sensor.

## Steps

These are run from the pi by editing the rc.local file and adding the lines:  

```
sudo nano /etc/rc.local

python3 temp.py &
telegraf --config temperatureLog.conf &
```
This runs the above commands at start up so the pi only needs to be plugged in and will automatically start logging values and pushing them to a remote database. The `temperatureLog.conf` file runs Telegraf which has been configured to push these values to an InfluxDB. 

I wanted to periodically truncate the log file so it doesn't become too big and eat up memory. First I needed to change ownership of the `temperature.log` file that is created with the above python process so it can be modified by non-root. 

```
chown <user> -R temperature.log
```

Then I set up a cronjob to truncate the file daily by running the `truncate.sh` file.

## LED Display

An LED display screen was added so I could see the current temperature making this a much more interactive device. The `temp.py` script was altered to also update the LED screen with the most recent temp reading. This updates every 30 seconds.

I used [these](https://www.amazon.com/dp/B086VVT4NH?psc=1&ref=ppx_yo2_dt_b_product_details) displays and they have worked great. I use the i2c_driver to interface with the screen as tutorialed [here](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c). The copy of `i2c_driver.py` in this repo does have some changes to better allow for toggling the backlight screen.
