import json
import datetime
from datetime import datetime

this_time = datetime.now()

message = f'Crawl finish: {this_time} \n'

print(message)

with open('mylog.txt', 'a') as mylog:
    mylog.write(message)