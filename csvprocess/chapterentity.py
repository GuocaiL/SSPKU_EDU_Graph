import csv

res_list=[]
with open('./graphcsv/section2.csv','w',newline='') as f :
    writer=csv.writer(f)
    writer.writerow(['title','label1','label2','label3','label4','label5','label6'])
    #label1:section、label2:chapter、label3:description、label4:course、label5:school、label6:reference
    with open('./filecsv/section.csv','r',encoding='UTF-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0].split('_')[0]+'_'+row[0].split('_')[1]+'_'+row[0].split("_")[2] not in res_list:
                if row[0].split('_')[0] =="beidawlf":
                    writer.writerow(['第'+row[0].split('_')[2]+'节','section',
                                     '第'+row[0].split('_')[1].split('_')[0]+'章',row[4],'软件工程','北京大学','王立福，孙艳春，刘学'])
                if row[0].split('_')[0] =="guofangkedaqzc":
                    writer.writerow(['第'+row[0].split('_')[2]+'节', 'section',
                                     '第'+row[0].split('_')[1].split('_')[0]+'章', row[4], '软件工程', '国防科技大学', '齐治昌'])
                if row[0].split('_')[0] =="zhedacy":
                    #writer.writerow([row[0].split('_')[1].split('_')[0],'section','软件工程','浙江大学','陈越','',''])
                    writer.writerow(['第'+row[0].split('_')[2]+'节', 'section',
                                     '第'+row[0].split('_')[1].split('_')[0]+'章', row[4], '软件工程', '浙江大学', '陈越'])
                res_list.append(row[0].split('_')[0]+'_'+row[0].split('_')[1]+'_'+row[0].split("_")[2])
                print(row[0].split('_')[0]+'_'+row[0].split('_')[1]+'_'+row[0].split("_")[2])

