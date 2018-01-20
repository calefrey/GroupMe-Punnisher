import os
import sys
import json
import time
import random

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  # We don't want to reply to ourselves!
  if data['sender_type'] != 'bot':
    inputString = data['text']
    words = inputString.lower().split(" ")
    puns = open('puns.csv')
    for line in puns:
      tag=line.split(',')
      for w in words:
        if w in tag:
          msg = tag[1]
          time.sleep(2)
          send_message(msg)
          if len(tag)==3
            msg = tag[2]
            time.sleep(2)
            send_message(msg)

  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  
@app.route('/home', methods=['GET'])
def home:
  return "It worked"
def log(msg):
  print(str(msg))
  sys.stdout.flush()