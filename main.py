from calendar import week, weekday
from urllib import request
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime
from ics import Calendar
import requests, json
from pytz import timezone
import pytz

app = Flask(__name__, template_folder='template')

app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


def switch(num):
  if num == 1:
    return "Måndag"
  elif num == 2:
    return "Tisdag"
  elif num == 3:
    return "Onsdag"
  elif num == 4:
    return "Torsdag"
  elif num == 5:
    return "Fredag"


def mat():
  url = "https://mpi.mashie.com/public/icalendar/V%C3%A4xj%C3%B6%20kommun%20ny/6f5fa240.ics"

  list1 = []
  c = Calendar(requests.get(url).text)

  for event in c.events:
    list1.append(
      [event.description,
       event.begin.timestamp(),
       event.begin.isocalendar()])

  list1.sort(key=lambda x: x[1])

  global weeklist

  tine = datetime.now(timezone('Europe/Stockholm')).isocalendar()[2]
  if tine <= 5:
    print(tine)
    weeklist = list1[tine - 1:5]
  else:

    weeklist = list1[5:10]
    print(weeklist)

  for element in weeklist:
    element = element.append(switch(element[2][2]))

  for element in weeklist:
    a = element[0].split('\n', -1)
    element[0] = [a[0], a[1]]

  for element in weeklist:
    pass

  return weeklist


matsedel = mat()

for mat in matsedel:
  #print(mat[2])
  pass


@app.route('/', methods=['POST', 'GET'])
def index():
  data = requests.get('http://ip-api.com/json/' +
                      str(request.remote_addr)).json()
  listof = []
  if data['status'] == 'success':
    listof = [
      data['country'], data['region'], data['regionName'], data['city'],
      data['lat'], data['lon'], data['timezone'], data['isp']
    ]
  else:
    listof = "Status: " + data['status'] + " Message: " + data['message']
  x = 'ip:' + request.environ[
    'HTTP_X_FORWARDED_FOR'] + '       Browser: ' + request.user_agent.string + '       Date: ' + str(
      datetime.now(timezone('Europe/Stockholm'))) + " " + str(listof) + '\n'
  with open('datadontopen.txt', 'a') as w:
    w.write(str(x))

  return render_template('index.html', matsedel=matsedel)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
