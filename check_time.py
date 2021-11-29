from datetime import datetime

def get_line(f = open("temperature.log")): 
    for line in f:
        pass
    return line[:-1]

def convert_time():
    l = get_line()
    l = float(l.split(" ")[0])

    print(datetime.utcfromtimestamp(l).strftime("%Y-%m-%d %H:%M:%S"))

convert_time()
