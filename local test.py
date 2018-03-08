import os
import sys
import time
import random
import csv
from bees import script

def run(inputString):
    words = inputString.lower().split(" ")
    if "bees" in words:
        send_message(script)
        return
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
def send_message(msg):
    time.sleep(random.randint(0,5))
    print(msg);
for _ in range(5):
    run(input('Message Text: '))
