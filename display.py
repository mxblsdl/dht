import i2c_driver
import time
import os
import Adafruit_DHT as adht

# Init the lcd object
mylcd = i2c_driver.LCD()

# Set time zone
os.environ["TZ"] = "America/Los_Angeles"
time.tzset()

while True:
    # Pull variables to display
    my_time = time.strftime("%I:%M:%S %p")
    my_date = time.strftime("%a %b %d, 20%y")

    # Pull temperature information
    h, t = adht.read_retry(adht.DHT22, 4)
    my_temp = (t * 9/5) + 32
    my_temp = str(round(my_temp, 1))

    # my_temp = str(round(check_time.convert_str(pos=1), 1))

    # send to LCD screen
    mylcd.lcd_display_string(my_time, 1)
    mylcd.lcd_display_string(my_date, 2)
    mylcd.lcd_display_string(my_temp + " Degrees", 3)
