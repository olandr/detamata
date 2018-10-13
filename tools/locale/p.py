import re
from selenium import webdriver
from selenium.webdriver.support.ui  import Select
from selenium.webdriver.common.keys import Keys

import time

# This link: https://cloud.timeedit.net/kth/web/public01/ri1f2XyQ0YvZ0YQ.html will preset the schedule Today --> On week
# This link is standard: https://cloud.timeedit.net/kth/web/public01/ri1Q2.html

# I will only start by looking at Q rooms (prototyping)
relevantRooms = ["Q11", "Q13", "Q15", "Q17", "Q21", "Q22", "Q24", "Q26", "Q31", "Q33", "Q34", "Q36"]

def initialisation():
    # This will select the correct option in the dropdown
    dropDown = driver.find_element_by_id("fancytypeselector")
    dropDown.click()              # Default: Program/klass
    dropDown.send_keys(Keys.DOWN) # Kurstillfälle
    dropDown.send_keys(Keys.DOWN) # Personal
    dropDown.send_keys(Keys.DOWN) # Lokal
    dropDown.send_keys(Keys.RETURN)


'''
args:
driver Driver for selenium
local The room to check availability for
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

    # Once we have gotten all the scheduled items we basically just want to get the title (start/end time) info.
    # I iterate throuhgh all possible weekDivs (each day) and then add them to a 'keeper'
def process_locale(weekDiv):
    keeper = []
    for day in weekDiv:
        daily = day.find_elements_by_class_name("bookingDiv")
        if daily != []:
            keeper.append(daily)
    # keeper is a nested array with each outer being a certain day (len=7), and the inner is the scheduled items.
    return keeper

def format_schedule(unformat):
    eventdate = []
    eventtime = []
    for day in unformat:
        for thing in day:
            # The title has a lot of fluff that we are not interested in. This is formatted with regex.
            uf = thing.get_attribute("title")
            day = re.sub(r'.*(\d\d\d\d-\d\d-\d\d) \d\d:\d\d - \d\d:\d\d.*', r'\1', uf)
            period = re.sub(r'.*\d\d\d\d-\d\d-\d\d (\d\d):\d\d - (\d\d):\d\d.*', r'\1\2', uf)
            #f = re.sub(r'\' (\d\d\d\d-\d\d-\d\d \d\d:\d\d - \d\d:\d\d).*\'', r'\1' , uf)
            eventdate.append(day)
            eventtime.append(period)
    return eventdate, eventtime

def reset_locale_search():
    reopenSearch = driver.find_element_by_id("openSearchButton")
    reopenSearch.click()
    time.sleep(1)
    removeOldLocale = driver.find_element_by_id("leftclearbutton")
    removeOldLocale.click()
    time.sleep(1)


allLocaleDates = []
allLocaleTimes = []
driver = webdriver.Chrome()
driver.get("https://cloud.timeedit.net/kth/web/public01/ri1f2XyQ0YvZ0YQ.html")
initialisation()

localWeekDiv = fresh_get_locale(relevantRooms[0])
# I will ignore the dates for now, as the file regex.py handles spot finding with the use of date. Not this file.
dates, times = format_schedule(process_locale(localWeekDiv))
allLocaleDates.append(dates)
allLocaleTimes.append(times)

time.sleep(1)
reset_locale_search()

localWeekDiv = fresh_get_locale(relevantRooms[1])
dates, times = format_schedule(process_locale(localWeekDiv))
allLocaleDates.append(dates)
allLocaleTimes.append(times)

print(allLocaleDates)
print(allLocaleTimes)
