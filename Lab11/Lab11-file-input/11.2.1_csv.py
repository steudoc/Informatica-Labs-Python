from csv import reader

fp = open("rawdata.csv", "r")
csv_reader = reader(fp)
next(csv_reader)
reddito = {}

for row in csv_reader:
    key = row[1]
    print(key)
