import pandas as pd
import re

'''
This function will format the output from the selenuiumscraping of title-attribute. The event name.
I only want to keep the date and the starttime endtime.
args:
dframe      The DataFrame that I will append to.
unformat    The unformatted data/strings/array.
room        The room for this unformatted data. I need this to map correctly in the DataFrame.
'''
def format_schedule(dframe, unformat, room):
    for uf in unformat:
        # The title has a lot of fluff that we are not interested in. This is formatted with regex.
        day = re.sub(r'.*(\d\d\d\d-\d\d-\d\d) \d\d:\d\d - \d\d:\d\d.*', r'\1', uf)
        period = re.sub(r'.*\d\d\d\d-\d\d-\d\d (\d\d):\d\d - (\d\d):\d\d.*', r'\1\2', uf)
        #f = re.sub(r'\' (\d\d\d\d-\d\d-\d\d \d\d:\d\d - \d\d:\d\d).*\'', r'\1' , uf)
        #print(day, period)
        temp = pd.DataFrame({'room': [room], 'date': [day], 'hour': [period]})
        dframe = dframe.append(temp)
    return dframe
