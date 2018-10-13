import pandas as pd
from regex import get_full_frame

superFrame = get_full_frame()
emptySpotFrame = pd.DataFrame(columns=['room', 'date', 'hour'])


'''
This function will iterate through all lines in a DataFrame of scheduled rooms and return a new DataFrame with only emptySpots.

args:
inputFrame  The input DataFrame of scheduled events for all queried rooms.

return      A DataFrame with only empty spots, mapped to rooms and date.

'''
def find_empty_spots(inputFrame):
    outFrame = pd.DataFrame(columns=['room', 'date', 'hour'])
    for room in inputFrame.room.unique():
        for date in inputFrame.date.unique():
            emptySchedule = list(range(8,25))
            for index, row in inputFrame.iterrows():
                if date != row['date'] or room != row['room']:
                    continue
                # I iterate through distinct rooms. Done by an outer-distinct-selection + inner-break.
                interval = range(int(row['hour'][0:2]), int(row['hour'][2:4]))
                for x in interval:
                    emptySchedule.remove(x)
            outFrame = outFrame.append(empty_spot_frame(room, date, emptySchedule))
    return outFrame

'''
This is a helper function that will, given an array of emptySpots, append that to a DataFrame mapped to a room and date.

args:
room        Room to map the empty spot to.
date        Date to map the empty spot to.
emptySpots  Array of empty spots (hours).
'''
def empty_spot_frame(room, date, emptySpots):
    out = pd.DataFrame(columns=['room', 'date', 'hour'])
    for spot in emptySpots:
        temp = pd.DataFrame({'room': [room], 'date': [date], 'hour': [spot]})
        out = out.append(temp)

    return out

def get_free_dataframe():
    return find_empty_spots(superFrame)
