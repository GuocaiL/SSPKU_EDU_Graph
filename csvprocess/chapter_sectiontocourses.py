import csv

data1=['王立福，孙艳春，刘学','齐治昌','陈越']
data2=['beidawlf','guofangkedaqzc','zhedacy']
with open('./graphcsv/chapterentity.csv','r',encoding='UTF-8') as m:
    reader1=csv.reader(m)
    f=open('./graphcsv/chapter_sectiontocourses.csv','w',newline='')
    writer=csv.writer(f)
    writer.writerow(['name','chapter_section','relation','courses_name','reference'])
    for a in reader1:
        if a[0]==data2[0]:
           writer.writerow([a[0],a[1],'subclass','软件工程',data1[0]])
        if a[0]==data2[1]:
           writer.writerow([a[0],a[1],'subclass','软件工程',data1[1]])
        if a[0]==data2[2]:
           writer.writerow([a[0],a[1],'subclass','软件工程',data1[2]])