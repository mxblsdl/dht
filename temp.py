import Adafruit_DHT as adht
import logging
import time
import i2c_driver
import os


"""
Logs temperature and humidity to a log file every 30 seconds. 
"""
logging.basicConfig(
    filename="/home/pi/dht/temperature.log",
    filemode="a",
    format="%(created)1s %(message)s",
    level=logging.INFO,
)

# Init the lcd object
mylcd = i2c_driver.LCD()

# Set time zone
os.environ["TZ"] = "America/Los_Angeles"
time.tzset()


while True:
    h, t = adht.read_retry(adht.DHT22, 4)
    logging.info(f"Temp={round(t, 1)} C and Humidity={round(h, 1)}")

    # Pull variables to display
    my_time = time.strftime("%I:%M %p")
    my_date = time.strftime("%a %b %d, 20%y")

    my_temp = (t * 9 / 5) + 32
    my_temp = str(round(my_temp, 1))

    # send to LCD screen
    mylcd.lcd_display_string(my_time, 1)
    mylcd.lcd_display_string(my_date, 2)
    mylcd.lcd_display_string(my_temp + " Degrees", 3)

    # Turn the backlight on
    mylcd.backlight(1)

    # Sleep the system
    time.sleep(30)
