from ics import Calendar
import requests
url = "https://mpi.mashie.com/public/icalendar/V%C3%A4xj%C3%B6%20kommun%20ny/6f5fa240.ics"

list1 = []
c = Calendar(requests.get(url).text)

for event in c.events:
    list1.append([event.description, event.begin.timestamp(), event.begin.ctime()])

list1.sort(key = lambda x: x[1])

weeklist = list1[:5]

for element in weeklist:
    print(element)