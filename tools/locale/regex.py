import re
times = [
  ['0810', '1012', '1517', '0810', '1315', '1012', '1517', '1720', '1618', '1012', '1315', '0809', '0910', '1012'],
  [
    '0810', '1517', '0810', '1315', '1517', '1012', '1315', '1517', '1720', '1618', '0812', '1315', '0809', '0910', '1012', '1315']
  ]

def format_schedule(unformat):
    date = []
    eventtime = []
    for uf in unformat:
        day = re.sub(r'.*(\d\d\d\d-\d\d-\d\d) \d\d:\d\d - \d\d:\d\d.*', r'\1', uf)
        period = re.sub(r'.*\d\d\d\d-\d\d-\d\d (\d\d):\d\d - (\d\d):\d\d.*', r'\1\2', uf)
        #f = re.sub(r'\' (\d\d\d\d-\d\d-\d\d \d\d:\d\d - \d\d:\d\d).*\'', r'\1' , uf)
        date.append(day)
        eventtime.append(period)
    return date, eventtime
