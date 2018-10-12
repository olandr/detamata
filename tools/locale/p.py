import re
from selenium import webdriver
from selenium.webdriver.support.ui  import Select
from selenium.webdriver.common.keys import Keys

import time
# This link: https://cloud.timeedit.net/kth/web/public01/ri1f2XyQ0YvZ0YQ.html will preset the schedule Today --> On week
# This link is standard: https://cloud.timeedit.net/kth/web/public01/ri1Q2.html

# I will only start by looking at Q rooms (prototyping)
relevantRooms = ["Q11", "Q13", "Q15", "Q17", "Q21", "Q22", "Q24", "Q26", "Q31", "Q33", "Q34", "Q36"]

driver = webdriver.Chrome()


driver.get("https://cloud.timeedit.net/kth/web/public01/ri1f2XyQ0YvZ0YQ.html")
dropDown = driver.find_element_by_id("fancytypeselector")
searchBox = driver.find_element_by_id("ffsearchname")
searchButton = driver.find_element_by_xpath("//*[@id=\"searchDivContent2\"]/div[2]/h2[2]/div/input[2]")

# This will select the correct option in the dropdown
dropDown.click()              # Default: Program/klass
dropDown.send_keys(Keys.DOWN) # Kurstillfälle
dropDown.send_keys(Keys.DOWN) # Personal
dropDown.send_keys(Keys.DOWN) # Lokal
dropDown.send_keys(Keys.RETURN)

# We select one room at the time (in the prototyp I select the first room)
searchBox.send_keys(relevantRooms[0])
searchButton.click()

# The resulting room shall be selected and clicked on
resultRoom = driver.find_element_by_id("objectsearchresult")
resultRoom.click()

time.sleep(1)

# Click to get schedule
getScheduleButton = driver.find_element_by_id("objectbasketgo")
getScheduleButton.click()

# The structure for the schedule output is //*[@id="contents"]/div[1]/div[4]/div[3]/div[8] (contents/weekContainer/weekDay/weekDiv/<no id>)
# Where the last has the title.
weekContainer = driver.find_element_by_class_name("weekContainer")
weekDiv = weekContainer.find_elements_by_class_name("weekDiv")

# Once we have gotten all the scheduled items we basically just want to get the title (start/end time) info.

# I iterate throuhgh all possible weekDivs (each day) and then add them to a 'keeper'
keeper = []
for day in weekDiv:
    daily = day.find_elements_by_class_name("bookingDiv")
    if daily != []:
        keeper.append(daily)

# keeper is a nested array with each outer being a certain day (len=7), and the inner is the scheduled items.
titles = []
for day in keeper:
    for thing in day:
        # The title has a lot of fluff that we are not interested in. This is formatted with regex.
        unformattedTitle = thing.get_attribute("title")
        formattedTitle = re.sub(r'.*(\d\d\d\d-\d\d-\d\d \d\d:\d\d - \d\d:\d\d).*', r'\1', unformattedTitle)
        titles.append(formattedTitle)

print(titles)
