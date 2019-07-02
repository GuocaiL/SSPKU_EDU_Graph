from django.shortcuts import render_to_response
from Model.neo4j_class import Neo4j
import json

def search_entity(request):
    ctx={}
    # 根据传入的实体名称搜索出关系
    if (request.GET):
        entity = request.GET['user_text']
        # 连接数据库
        db = Neo4j()
        db.connectDB()
        entityRelation = db.getEntityRelationByEntity(entity)
        if len(entityRelation) == 0:
            # 若数据库中无法找到该实体，则返回数据库中无该实体
            ctx = {'title': '<h1>数据库中暂未添加该实体</h1>'}
            return render_to_response('entity.html', {'ctx': json.dumps(entityRelation, ensure_ascii=False)})
        else:
            # 返回查询结果
            # 将查询结果按照"关系出现次数"的统计结果进行排序
            # entityRelation = sortDict(entityRelation)
            return render_to_response('entity.html',{'entityRelation':  json.dumps(entityRelation,  ensure_ascii=False)})
    return render_to_response('entity.html', {'ctx':ctx})

def search_relation(request):
    ctx={}
    if (request.GET):
        db = Neo4j()
        db.connectDB()
        entity1 = request.GET['entity1_text']
        relation = request.GET['relation_name_text']
        entity2 = request.GET['entity2_text']
        relation = relation.lower()
        searchResult = {}
        # 若只输入entity1,则输出与entity1有直接关系的实体和关系
        if (len(entity1) != 0 and len(relation) == 0 and len(entity2) == 0):
            searchResult = db.findRelationByEntity(entity1)
            # searchResult = sortDict(searchResult)
            if (len(searchResult) > 0):
                return render_to_response('relation.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})

        # 若只输入entity2则,则输出与entity2有直接关系的实体和关系
        if (len(entity2) != 0 and len(relation) == 0 and len(entity1) == 0):
            searchResult = db.findRelationByEntity2(entity2)
            # searchResult = sortDict(searchResult)
            if (len(searchResult) > 0):
                return render_to_response( 'relation.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})
        # 若输入entity1和relation，则输出与entity1具有relation关系的其他实体
        if (len(entity1) != 0 and len(relation) != 0 and len(entity2) == 0):
            searchResult = db.findOtherEntities(entity1, relation)
            # searchResult = sortDict(searchResult)
            if (len(searchResult) > 0):
                return render_to_response( 'relation.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})
        # 若输入entity2和relation，则输出与entity2具有relation关系的其他实体
        if (len(entity2) != 0 and len(relation) != 0 and len(entity1) == 0):
            searchResult = db.findOtherEntities2(entity2, relation)
            # searchResult = sortDict(searchResult)
            if (len(searchResult) > 0):
                return render_to_response('relation.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})
        # 若输入entity1和entity2,则输出entity1和entity2之间的最短路径
        if (len(entity1) != 0 and len(relation) == 0 and len(entity2) != 0):
            searchResult = db.findRelationByEntities(entity1, entity2)
            if (len(searchResult) > 0):
                print(searchResult)
                # searchResult = sortDict(searchResult)
                return render_to_response('relation.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})
        # 若输入entity1,entity2和relation,则输出entity1、entity2是否具有相应的关系
        if (len(entity1) != 0 and len(entity2) != 0 and len(relation) != 0):
            searchResult = db.findEntityRelation(entity1, relation, entity2)
            # searchResult = sortDict(searchResult)
            if (len(searchResult) > 0):
                return render_to_response('relation.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})
        # 全为空
        if (len(entity1) != 0 and len(relation) != 0 and len(entity2) != 0):
            pass
        ctx = {'title': '<h1>暂未找到相应的匹配</h1>'}
        return render_to_response('relation.html', {'ctx': ctx})

    return render_to_response('relation.html', {'ctx': ctx})