import csv

with open('data.csv',mode='a', encoding='utf-8',newline='') as csv_file:
    csv_reader = csv.writer(csv_file)
    csv_reader.writerow(['tom','c',50])

    list = [['lily','c',70],['lily','python',57],['lily','java',90]]
    csv_reader.writerows(list)