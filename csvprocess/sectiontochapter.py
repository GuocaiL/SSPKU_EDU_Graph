import csv


#section to chapter
with open('./graphcsv/PKUEntityRelation.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['entity1','label1','label2','label3','label4','label5','label6','relation','entity2','label7','label8','label9','label10','label11','label12'])
    with open('./graphcsv/section2.csv','r',encoding='GBK') as f:
        reader=csv.reader(f)
        for row in reader:
            writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],'belong',row[2],'chapter',row[4],row[5],row[6]])



#konwledge to chapter