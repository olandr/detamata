import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.support.ui  import Select
from selenium.webdriver.common.keys import Keys

import time

# This link: https://cloud.timeedit.net/kth/web/public01/ri1f2XyQ0YvZ0YQ.html will preset the schedule Today --> On week
# This link is standard: https://cloud.timeedit.net/kth/web/public01/ri1Q2.html

# I will only start by looking at Q rooms (prototyping)
relevantRooms = ["Q11", "Q13", "Q15", "Q17", "Q21", "Q22", "Q24", "Q26", "Q31", "Q33", "Q34", "Q36"]

# This will initialise the dropdown to the correct dropdown option 'Lokal'.
def initialisation():
    # This will select the correct option in the dropdown
    dropDown = driver.find_element_by_id("fancytypeselector")
    dropDown.click()              # Default: Program/klass
    dropDown.send_keys(Keys.DOWN) # Kurstillfälle
    dropDown.send_keys(Keys.DOWN) # Personal
    dropDown.send_keys(Keys.DOWN) # Lokal
    dropDown.send_keys(Keys.RETURN)

# After we have searched for some room we need to reset the state.
def reset_locale_search():
    reopenSearch = driver.find_element_by_id("openSearchButton")
    reopenSearch.click()
    time.sleep(1)
    removeOldLocale = driver.find_element_by_id("leftclearbutton")
    removeOldLocale.click()
    time.sleep(1)

'''
This will search for some room. It requries that the state is untouched, i.e. either the first call or after a reset_locale_search().

args:
local   The room to check availability for.

return  A selenium item that has all sub-divs that has the scheduled events. This is basically jibbrish that selenium can handle.
'''
def fresh_get_locale(locale):

    searchBox = driver.find_element_by_id("ffsearchname")
    searchButton = driver.find_element_by_xpath("//*[@id=\"searchDivContent2\"]/div[2]/h2[2]/div/input[2]")
    # We select one room at the time (in the prototyp I select the first room)
    searchBox.send_keys(locale)
    time.sleep(1)
    searchButton.click()
    time.sleep(1)
    # The resulting room shall be selected and clicked on
    resultRoom = driver.find_element_by_id("objectsearchresult")
    resultRoom.click()
    time.sleep(1)

    # Click to get schedule
    getScheduleButton = driver.find_element_by_id("objectbasketgo")
    getScheduleButton.click()
    time.sleep(1)
    # The structure for the schedule output is //*[@id="contents"]/div[1]/div[4]/div[3]/div[8] (contents/weekContainer/weekDay/weekDiv/<no id>)
    # Where the last has the title.
    weekContainer = driver.find_element_by_class_name("weekContainer")
    return weekContainer.find_elements_by_class_name("weekDiv")
'''
Once we have gotten all the scheduled items we basically just want to get the title (start/end time) info.
I iterate throuhgh all possible weekDivs (each day) and then add them to a 'keeper'.

args:
weekDiv     This is the selenium object that has the scheduled events (see return of fresh_get_locale()).

return      An array of ALL info for the scheduled events. I.e. Course code, attendees, time-interval etc.
'''
def process_locale(weekDiv):
    keeper = []
    for day in weekDiv:
        daily = day.find_elements_by_class_name("bookingDiv")
        if daily != []:
            keeper.append(daily)
    # keeper is a nested array with each outer being a certain day (len=7), and the inner is the scheduled items.
    return keeper

'''
WILL REMOVE THIS FUNCTION AND USE THE ONE IN regex.py.
I only care for some info in the gathered data. Namely the starttime and endtime.

'''
def format_schedule(dframe, unformat, room):
    eventdate = []
    eventtime = []
    for day in unformat:
        for thing in day:
            # The title has a lot of fluff that we are not interested in. This is formatted with regex.
            uf = thing.get_attribute("title")
            day = re.sub(r'.*(\d\d\d\d-\d\d-\d\d) \d\d:\d\d - \d\d:\d\d.*', r'\1', uf)
            period = re.sub(r'.*\d\d\d\d-\d\d-\d\d (\d\d):\d\d - (\d\d):\d\d.*', r'\1\2', uf)
            #f = re.sub(r'\' (\d\d\d\d-\d\d-\d\d \d\d:\d\d - \d\d:\d\d).*\'', r'\1' , uf)
            temp = pd.DataFrame({'room': [room], 'date': [day], 'hour': [period]})
            dframe = dframe.append(temp)
    return dframe


superFrame = pd.DataFrame(columns=['room', 'date', 'hour'])
driver = webdriver.Chrome()
driver.get("https://cloud.timeedit.net/kth/web/public01/ri1f2XyQ0YvZ0YQ.html")
initialisation()
# prototyping:
i = 0
while i < 2:
    localWeekDiv = fresh_get_locale(relevantRooms[i])
    # I will ignore the dates for now, as the file regex.py handles spot finding with the use of date. Not this file.
    superFrame = format_schedule(superFrame, process_locale(localWeekDiv), relevantRooms[i])
    time.sleep(1)
    reset_locale_search()
    i += 1

print(superFrame)
