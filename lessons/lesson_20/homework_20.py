from lessons.lesson_07.some_exercices import timestamp
import time
import logging
from datetime import timedelta, datetime

logging.basicConfig(
    filemode="w",
    filename="hb_test.log",
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

with open("hblog.txt", "r") as f:
    log = f.readlines()

filtered_log = []
for line in log:
    if line.__contains__("TSTFEED0300|7E3E|0400"):
        filtered_log.append(line)

time_array = []
for line in filtered_log:
    position = line.find("Timestamp ") + 9
    stamp_time = line[position:position + 9]
    time_array.append(stamp_time)

delta_time = []
delta_time_array = []
for i in range(len(time_array) - 1):
    t1 = datetime.strptime(time_array[i].strip(), "%H:%M:%S")
    t2 = datetime.strptime(time_array[i + 1].strip(), "%H:%M:%S")
    delta_time = (abs((t2 - t1).total_seconds()))
    delta_time_array.append(delta_time)
    if 31 < delta_time < 33:
        logging.warning(f'{time_array[i].strip()} delta {delta_time}')
    elif delta_time == 33:
        logging.error(f'{time_array[i].strip()} delta {delta_time}')

print('hi')
