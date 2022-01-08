from datetime import datetime
import re
import subprocess

"""
Read the last lines of the temperature log file. 
Used to check the outputs for the correct time and temperature.
"""

# Split the last line and take given position
# 0 is time, 1 is temp, 2 is humidity
def extract_str(l, pos):
    l = l.split(" ")[pos]
    l_result = re.sub("[^0-9.]", "", l)
    l_result = float(l_result)
    return l_result


# Call shell command on log file to get last line
def convert_str(pos):
    proc = subprocess.Popen(
        "tail -1 /home/pi/dht/temperature.log", stdout=subprocess.PIPE, shell=True
    )
    out, err = proc.communicate()
    out = out.decode("utf-8")

    l_result = extract_str(out, pos)

    if pos == 1:
        l_result = (l_result * 9 / 5) + 32
        return l_result

    return datetime.utcfromtimestamp(l_result).strftime("%Y-%m-%d %H:%M:%S")


# print(convert_str(1))
