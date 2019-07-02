import csv

with open('./graphcsv/knowledgevideoentity.csv','r',encoding='GBK') as m,open('./graphcsv/chapterentity.csv','r',encoding='GBK') as n:
    reader1=csv.reader(m)
    reader2=csv.reader(n)
    f=open('./graphcsv/knowledgetoname.csv','w',newline='')
    writer=csv.writer(f)
    writer.writerow(['name','relation','chapter_name','chapter_section'])
    for (a,b) in zip(reader1,reader2):
        writer.writerow([a[0],'subclass',b[0],b[1]])
