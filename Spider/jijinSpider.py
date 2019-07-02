import urllib.request,csv,time,socket

socket.setdefaulttimeout(60)
heards={'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
error=''

with open('D:\software\jijin.csv','w',newline='')  as f,open('D:\software\error.csv','w',newline='') as j:
    error=csv.writer(j)
    writer=csv.writer(f)
    writer.writerow(['题目','负责人','单位','单位金额（万）','项目编号','项目类型','所属学部','批准年份','学科分类'])
    # money=1
    for year in range(1997,2019):
        money=0
        while money<10000:
        #for money in range(0,10000,0.5):
            response=''
            html1=''
            result1=''
            try:
                # response1 = urllib.request.Request('http://www.letpub.com.cn/?page=grant&name=&person=&no=&company=&addcomment_s1=553&addcomment_s2=0&addcomment_s3=0&money1=' + str(
                #     money) + '&money2=' + str(money + 0.5) + '&startTime=' + str(year) + '&endTime=' + str(
                #     year) + '&subcategory=&searchsubmit=true&submit.x=56&submit.y=12#fundlisttable', heards=heards)
                # html1 = urllib.request.urlopen(response)
                # result1 = html1.read().decode('utf-8')

                response1 = urllib.request.urlopen('http://www.letpub.com.cn/?page=grant&name=&person=&no=&company=&addcomment_s1=553&addcomment_s2=0&addcomment_s3=0&money1='+str(money)+'&money2='+str(money+0.5)+'&startTime='+str(year)+'&endTime='+str(year)+'&subcategory=&searchsubmit=true&submit.x=56&submit.y=12#fundlisttable')
                result1 = response1.read().decode("utf-8")
            except BaseException:
                error.writerow(["第" + str(year) + "年，" + str(money) + '万元->' + str(money + 0.5) + '万元-------------------------------------------------------------------------------出错'])
                print("第" + str(year) + "年，" + str(money) + '万元->' + str(money + 0.5) + '万元-------------------------------------------------------------------------------出错')
            else:
                page = int(result1.split("页，共")[1].split("页。结果最多显示")[0])
                # print(page)
                for p in range(1, page + 1):
                    response = ''
                    result = ''
                    try:
                        # response = urllib.request.Request(
                        #     'http://www.letpub.com.cn/index.php?page=grant&name=&person=&no=&company='
                        #     '&startTime=' + str(year) + '&endTime=' + str(year) + '&money1=' + str(
                        #         money) + '&money2=' + str(
                        #         money + 0.5) + '&subcategory=&addcomment_s1=0&addcomment_s2=0&addcomment_s3=0'
                        #                        '&currentpage=' + str(p) + '#fundlisttable', heards=heards)
                        # html = urllib.request.urlopen(response)
                        # result = html1.read().decode('utf-8')

                        response = urllib.request.urlopen(
                            'http://www.letpub.com.cn/index.php?page=grant&name=&person=&no=&company=&startTime='+str(year)+'&endTime='+str(year)+'&money1='+str(money)+'&money2='+str(money+0.5)+'&subcategory=&addcomment_s1=553&addcomment_s2=0&addcomment_s3=0&currentpage='+str(p)+'#fundlisttable')
                        result = response.read().decode("utf-8")
                    except BaseException:
                        error.writerow(["第" + str(year) + "年，" + str(money) + '万元->' + str(money + 0.5) + '万元，第' + str(
                            p) + '页--------------------------------------------------------出错'])
                        print("第" + str(year) + "年，" + str(money) + '万元->' + str(money + 0.5) + '万元，第' + str(
                            p) + '页--------------------------------------------------------出错')
                    else:


                        # 将每一个记录切分
                        str1 = result.split("<tr style=\"background:#EFEFEF;\">")
                        # print(str1)
                        # 处理每一个记录
                        if len(str1) > 0:
                            # print(len(str1))
                            for m in range(1, len(str1)):
                                # print(str1[m])
                                print("第" + str(year) + "年，" + str(money) + '万元->' + str(money + 0.5) + '万元，第' + str(
                                    p) + '页，第' + str(m) + '条')
                                # if m !=(len(str)-1):
                                # 处理第一个小表格
                                tabel1 = str1[m].split("</tr><tr>")[0].split(";\">")
                                name = tabel1[1].split("</td>")[0]
                                part = tabel1[2].split("</td>")[0]
                                money1 = tabel1[3].split("</td>")[0]
                                itemId = tabel1[4].split("</td>")[0]
                                itemType = tabel1[5].split("</td>")[0]
                                belongPart = tabel1[6].split("</td>")[0]
                                agreeYear = tabel1[7].split("</td>")[0]

                                # 第二个小表格
                                Topic = str1[m].split("</tr><tr>")[1].split("colspan=\"6\">")[1].split("</td>")[0]

                                # 第三个小表格
                                Type = str1[m].split("</tr><tr>")[2].split("colspan=\"6\">")[1].split("</td>")[0]
                                # time.sleep(1)
                                writer.writerow([Topic, name,part, money1, itemId, itemType, belongPart, agreeYear, Type])
       # print(year)
            money=money+0.5




