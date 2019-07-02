import csv

with open('./graphcsv/partentity.csv','w',newline='') as f :
    writer=csv.writer(f)
    writer.writerow(['school'])
    with open('./filecsv/course.csv','r',encoding='UTF-8') as f:
        reader = csv.reader(f)
        for row in reader:
            writer.writerow([row[2]])


