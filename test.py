import csv
import pprint
import random

inputString = input("Input ")
words =  inputString.lower().split(' ')
puns = csv.reader(open('Master_Pun_List.csv'), delimiter = '\n')
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
			print(punHolder[index][1])
			if len(punHolder[index]) == 3:
				print(punHolder[index][2])
			break
		else:
			msg = tag[1]
			print(msg)
			if len(tag) == 3:
				msg = tag[2]
				print(msg)
