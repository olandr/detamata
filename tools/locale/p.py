from selenium import webdriver
from selenium.webdriver.support.ui  import Select
from selenium.webdriver.common.keys import Keys
import time

# This link: https://cloud.timeedit.net/kth/web/public01/ri1f2XyQ0YvZ0YQ.html will preset the schedule Today --> On week
# This link is standard: https://cloud.timeedit.net/kth/web/public01/ri1Q2.html

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
    time.sleep(2)
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
            for day in daily:
                if day != []:
                    keeper.append(day.get_attribute("title"))
    # keeper is a nested array with each outer being a certain day (len=7), and the inner is the scheduled items.
    return keeper

driver = webdriver.Chrome()
#14/10 I need another link cuz it does not work correctly on sundays.
#driver.get("https://cloud.timeedit.net/kth/web/public01/ri1f2XyQ0YvZ0YQ.html")
driver.get("https://cloud.timeedit.net/kth/web/public01/ri15230QX09Z50Q5Yg6g0535y60Y6.html")
initialisation()

'''
This is the function that will be called by outside callers (main)

args:
room    Room to scrape

return  A list of unformatted data/info for each scheduled event.
'''
def scrape(room):
    localWeekDiv = fresh_get_locale(room)
    # I will ignore the dates for now, as the file regex.py handles spot finding with the use of date. Not this file.
    unformat = process_locale(localWeekDiv)
    reset_locale_search()
    return unformat
