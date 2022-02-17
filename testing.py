from time import sleep
from datetime import datetime
for i in range(10000):
    print(i, datetime.now())
    sleep(1)