import os
import sys
import json
import time
import random
import csv

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['POST'])
def webhook():
  #when a post is received, excecute the following
  data = request.get_json()
  log('Recieved {}'.format(data))
  # Don't reply to own messages or other bots
  if data['sender_type'] != 'bot' and random.randint(0,10)<3:
    inputString = data['text'] #Reads in message from GroupMe payload as a string
    words = inputString.lower().split(" ") 
    #make it all lowercase and split into individual words
    puns = csv.reader(open('puns.csv'), delimiter = '\n')
    #read in CSV file of puns
    punHolder = []

    for line in puns:
      punHolder.append(line[0].split(',')) 
      #detect the different columns in the CSV by splitting at the commas
      #and turning them into a 2D array
    tagHolder = [row[0] for row in punHolder] #Creates a 1D array out of the ta names

    for tag in punHolder:
      if tag[0] in words: #look for a tag in the message text
        if tagHolder.count(tag[0]) > 1: #Counts how many identical tags there are
          #randomly choose one of the matches
          indexes = [i for i, x in enumerate(tagHolder) if x == tag[0]]
          rando = random.randint(0,len(indexes) - 1)
          index = indexes[rando]

          send_message(punHolder[index][1]) #send the first part of the pun
          if len(punHolder[index]) == 3:    #if there is a second line to the pun
            send_message(punHolder[index][2]) #send the second line
          break
        else: #if there is only one matching pun
          send_message(tag[1])
          if len(tag) == 3: #check for a second part of the pun
            send_message(tag[2]) #send the second part
  
  return "ok", 200

def send_message(msg):
  time.sleep(random.randint(0,5)) 
  #have a delay so that it seems like the bot is thinking and doesn't respond too fast
  url  = 'https://api.groupme.com/v3/bots/post' #destination

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'), 
          #ID tored as an environmental variable in Heroku to protect the innocent
          'text'   : msg, #The reply
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()

@app.route('/', methods=['GET'])
def homepage():                 #Nobody should be visiting that URL anyway
      return "You got Punned!"  #but it's not longer an error

def log(msg):
  print(str(msg))
  sys.stdout.flush()