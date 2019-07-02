from django.shortcuts import render_to_response
from django.views.decorators import csrf
import os
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from pyltp import SentenceSplitter
from pyltp import Segmentor

from pyltp import NamedEntityRecognizer
from pyltp import Postagger

class recogentity(TemplateView):

   @csrf_exempt
   def recog_entity(request):
        biaodian=["。","？","！","，","、","；",'：','“', '”','’','‘','（','）','【','】','{','}','[',']','——','……', '．','—','·','<','>','《','》','_____']
        print("lkdjfsdjf")
        st=request.POST.get('user_text')
        # 分句操作
        sents = SentenceSplitter.split(st)  # 分句
        str1 = '<br>'.join(sents)

        # 分词操作
        LTP_DATA_DIR = './itpmodel'  # ltp模型目录的路径
        cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
        segmentor = Segmentor()  # 初始化实例
        segmentor.load(cws_model_path)  # 加载模型
        words = segmentor.segment(st)  # 分词
        segmentor.release()  # 释放模型

        #词性标注
        pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
        postagger = Postagger()  # 初始化实例
        postagger.load(pos_model_path)  # 加载模型
        postags = postagger.postag(words)  # 词性标注
        postagger.release()  # 释放模型

        #命名实体识别
        # -*- coding: utf-8 -*-
        ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
        recognizer = NamedEntityRecognizer()  # 初始化实例
        recognizer.load(ner_model_path)  # 加载模型
        netags = recognizer.recognize(words, postags)  # 命名实体识别
        str3='\t'.join(netags)
        recognizer.release()  # 释放模型

        s=""
        str2=""
        i=0
        j=0
        count=0
        wor=list(words)
        net=list(netags)
        #重组输入信息并添加链接(链接还未实现)
        while i < len(wor):
            if  net[i]!= 'O':
                s =s+ " <strong><small style='color:#02B7FE'>" + wor[i] + "</small></strong> "
            else:
                s =s+ wor[i]
            i+=1

        #处理分词结果
        while j < len(wor):
            if wor[j] in biaodian:
                j=j+1
            else:
                str2 =str2+"<h5 style='color:#FEB154;display: inline'>"+wor[j]+"</h5>"+"&nbsp&nbsp&nbsp"
                j=j+1
                count+=1
        return render_to_response('index.html', {'st':st,'rlt':s,"seg_word": "共计"+str(count)+"个：<br/>"+str2})

   @csrf_protect
   def index_view(request):
        return render_to_response("index.html")