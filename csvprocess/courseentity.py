import csv

with open('./graphcsv/courseentity.csv','w',newline='') as f :
    writer=csv.writer(f)
    writer.writerow(['courses_name','reference'])
    with open('./filecsv/course.csv','r',encoding='UTF-8') as f:
        reader = csv.reader(f)
        for row in reader:
            writer.writerow([row[1],row[3]])


