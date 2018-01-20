import time
import random

inputString = input("Input ")
words =  inputString.lower().split(' ')
puns = open('puns.csv')
for line in puns:
  tag=line.split(',')
  found = []
  for w in words:
    if w in tag:
      found = [found,tag]
if len(found)>1:
  choice = random.randint(0,len(found)-1)
  msg=found[choice][1]
  time.sleep(2)
  print(msg)
  if len(found[choice])==3:
      msg = (found[choice][2])
      time.sleep(2)
      print(msg)
else:
  msg=tag[1]
  time.sleep(2)
  print(msg)
  if len(tag)==3:
    msg=tag[2]
    time.sleep(2)
    print(msg)
