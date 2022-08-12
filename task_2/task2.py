import csv
from datetime import datetime




with open('csv/original.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    writer = csv.writer(open('csv/result.csv', 'w', newline=''))
    date_time = datetime.now()
    writer.writerow(["year", "region", "value"])
    next(csv_reader,None)
    for date in csv_reader:
        date[0] = date_time.strftime(("%d-%m-%Y"))
        print(date)
        a = input('what is the current population ?')
        date[2] = a
        csv_file.readline() 
        writer.writerow(date)