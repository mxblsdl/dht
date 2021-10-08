import Adafruit_DHT as adht 
import logging
import time

'''
Logs temperature and humidity to a log file every 30 seconds. 
'''
logging.basicConfig(filename='/home/pi/dht/temperature.log', filemode='a', format='%(created)1s %(message)s', level=logging.INFO) 

while True:     
    h,t = adht.read_retry(adht.DHT22, 4)
    logging.info(f'Temp={round(t, 1)} C and Humidity={round(h, 1)}')
    time.sleep(30)
