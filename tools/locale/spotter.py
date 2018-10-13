import re
# Output from p.py
dates = [
  [
    '2018-10-08', '2018-10-08', '2018-10-08', '2018-10-09', '2018-10-09', '2018-10-10', '2018-10-10', '2018-10-10', '2018-10-11', '2018-10-11', '2018-10-11', '2018-10-12', '2018-10-12', '2018-10-12'],
  [
    '2018-10-08', '2018-10-08', '2018-10-09', '2018-10-09', '2018-10-09', '2018-10-10', '2018-10-10', '2018-10-10', '2018-10-10', '2018-10-11', '2018-10-11', '2018-10-11', '2018-10-12', '2018-10-12', '2018-10-12', '2018-10-12'
    ]
]

times = [
  [
    '0810', '1012', '1517', '0810', '1315', '1012', '1517', '1720', '1618', '1012', '1315', '0809', '0910', '1012'],
  [
    '0810', '1517', '0810', '1315', '1517', '1012', '1315', '1517', '1720', '1618', '0812', '1315', '0809', '0910', '1012', '1315']
  ]

# This function will, given the two vector:
# dateVector This has all dates that has something scheduled).
# timeVector This has the start and end times (on a specific format: concat(startTime, endTime)) of each event.
# One find a bijection with the elements which fulfills: dateVector[i] ---> timeVector[i], event on day dateVector[i] starts at time timeVector[i].
def group_daily_schedule(dateVector, timeVector):
    daily = []
    temp = []
    index = 1
    jndex = 0
    # This will basically find the bijection and group each element of timeVector accordingly.
    while index <= len(dateVector):
        previous = index-1
        temp.append(timeVector[jndex])
        if index < len(dateVector):
            if dateVector[previous] != dateVector[index]:
                daily.append(temp)
                temp = []
        # When we have reached the final element, we need to append the grouping to the daily-output. I.e. the friday.
        # This could possibly be moved around to be a bit more "beautiful".
        else:
            daily.append(temp)
        index += 1
        jndex += 1
    return daily

# This function will find empty spots by crossing out those times that has been scheduled.
# Returns a matrix whose cols are days and rows are empty hour.

def find_empty_spots(daily):
    emptyDays = []
    for day in daily:
        emptySchedule = list(range(8,21))
        for thing in day:
            interval = range(int(thing[0:2]), int(thing[2:4]))
            for x in interval:
                emptySchedule.remove(x)
        emptyDays.append(emptySchedule)
    return emptyDays

# Dates will have both Q11, Q13. So we need to take both disjunctions seperately
room = 0
allEmpty = []
while room < len(dates):
    daily = group_daily_schedule(dates[room], times[room])
    emptySpotsPerDay = find_empty_spots(daily)
    allEmpty.append(emptySpotsPerDay)
    room += 1

print(allEmpty)
