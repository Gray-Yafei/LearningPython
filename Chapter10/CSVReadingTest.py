import csv

with open('data.csv',mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # 获取表头
    scores = []
    for row in csv_reader:
        scores.append(int(row[2]))
    print(sum(scores)/len(scores))