import csv

with open('./graphcsv/knowledgevideoentity.csv','w',newline='') as f :
    writer=csv.writer(f)
    writer.writerow(['name','starttime','endtime'])
    with open('./filecsv/section.csv','r',encoding='UTF-8') as f:
        reader = csv.reader(f)
        for row in reader:
            writer.writerow([row[4],row[2],row[3]])