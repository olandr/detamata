import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

from p import scrape, reset_locale_search
from regex import format_schedule
from spotter import get_free_dataframe

# I will only start by looking at Q rooms (prototyping)
relevantRooms = ["Q11", "Q13", "Q15", "Q17", "Q21", "Q22", "Q24", "Q26", "Q31", "Q33", "Q34", "Q36"]

def present():
    sns.set(style="whitegrid")
    ax = sns.catplot(x='date', y='hour', hue ="room",data=superFrame)
    plt.show()

i = 0
superFrame = pd.DataFrame(columns=['room', 'date', 'hour'])
# This loop iterates thru the the list of rooms, scrapes and formtts the information.
while i < 2:
    room = relevantRooms[i]
    print("Starting scraper for:", room, "...")
    listWithUnformattedEvents = scrape(room)
    print("Done scraping.\nStarting formatter...")
    superFrame = format_schedule(superFrame, listWithUnformattedEvents, room)
    print("Formatting done for room:", room)
    print("----")
    i += 1

print("Starting empty-spot-finding-service...")
# We find the empty spots and store to the superFrame.
superFrame = get_free_dataframe(superFrame)
print("Empty spots service done!")
print("Presenting...")
# We are done! Just presentation left.
present()
