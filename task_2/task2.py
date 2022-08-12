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
        for i in csv_reader:
            a = i[2]
            print(a)
            print(date[2])
            date[2] = str(int(date[2]) + int(a))
        csv_file.readline() 
        writer.writerow(date)