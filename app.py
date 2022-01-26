import csv
import time
from datetime import datetime, date, timedelta

def main(file_name: str) -> str:

    bikes = {}
    journey_duration = 0
    tomorrow = date.today() + timedelta(days=1)

    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for line in reader:

            bike = line[1]
            arrived = line[2]
            departed = line[3]

            if bike not in bikes:
                bikes[bike] = {
                        'arrivals': [],
                        'departures': [],
                        'starts_docked': False,
                        'ends_docked': False
                }

            if arrived:
                dt = datetime.strptime(arrived, "%Y%m%dT%H:%M:%S")
                seconds = (dt - datetime(1900, 1, 1)).total_seconds()
                bikes[bike]['arrivals'].append(seconds)
            else:
                bikes[bike]['starts_docked'] = True

            if departed:
                dt = datetime.strptime(departed, "%Y%m%dT%H:%M:%S")
                seconds = (dt - datetime(1900, 1, 1)).total_seconds()
                bikes[bike]['departures'].append(seconds)
            else:
                bikes[bike]['ends_docked'] = True


            

    for bike in bikes.values():

        bike['arrivals'].sort()
        bike['departures'].sort()

        if not bike['starts_docked']:
            del bike['arrivals'][0]
        
        if not bike['ends_docked']:
            bike['departures'].pop()

        journey_duration += sum(bike['arrivals']) - sum(bike['departures'])


    mean_journey_duration = journey_duration//len(bikes)
    formatted_duration = time.strftime('%H:%M:%S', time.gmtime(mean_journey_duration))
    return formatted_duration

if __name__ == "__main__":
    print(main('data.csv'))
