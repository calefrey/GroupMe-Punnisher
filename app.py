import os
import sys
import json
import time
import random
import csv

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

puns = csv.reader(open('puns.csv'), delimiter = '\n')

app = Flask(__name__)
@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  # We don't want to reply to ourselves!
  if data['sender_type'] != 'bot':
    inputString = data['text']
    words = inputString.lower().split(" ")
    punHolder = []

    for line in puns:
      punHolder.append(line[0].split(','))
    tagHolder = [row[0] for row in punHolder]

    for tag in punHolder:
      if tag[0] in words:
        if tagHolder.count(tag[0]) > 1:
          indexes = [i for i, x in enumerate(tagHolder) if x == tag[0]]
          rando = random.randint(0,len(indexes) - 1)
          index = indexes[rando]
          send_message(punHolder[index][1])
          if len(punHolder[index]) == 3:
            send_message(punHolder[index][2])
          break
        else:
          msg = tag[1]
          send_message(msg)
          if len(tag) == 3:
            msg = tag[2]
            send_message(msg)


  return "ok", 200

def send_message(msg):
  time.sleep(2)
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  
#@app.route('/', methods=['GET'])
def home():
  return "You have been PUNNED!"
def log(msg):
  print(str(msg))
  sys.stdout.flush()