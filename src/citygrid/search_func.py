
from .models import TInfoMain,TInsCaseMain,TKeeperstrack
from . import models as citygrid_models
from django.forms.models import model_to_dict

def get_query(model,page=1,perpage=200,filters={}):
    
    model_cls = getattr ( citygrid_models,model)
    query = model_cls.objects.filter(**filters)
    
    start= (page-1) * perpage
    end = page*perpage
    ls =[]
    for item in query[start:end]:
        dc = model_to_dict(item)
        ls.append(dc)
    return ls  


def get_ducha(page=1,perpage=200,streetcode =1806):
    """获取赵巷的督查员案件
    @streetcode:1806是赵巷
    """
    qu = TInsCaseMain.objects.filter(status__in=[3 ,-2,-1],streetcode =streetcode).order_by('-discovertime').distinct()
    qu= append_cat(qu, 'T_INS_CASE_MAIN')
    
    start= (page-1) * perpage
    end = page*perpage
    ls =[]
    for item in qu[start:end]:
        dc = model_to_dict(item)
        dc.update({
            'bcname':item.bcname,
            'scname':item.scname,
        })
        ls.append(dc)
    return ls

def get_jiandu(start,end,page=1,perpage=200,streetcode =1806):
    """获取监督员案件
    @streetcode: 1086 是赵巷
    
    status__in=[0,1,2,3,4,5,6,7,8,15,16,17],
    
    """
    qu = TInfoMain.objects.filter( discovertime__gt=start,
                                  discovertime__lte=end,
                                  streetcode=streetcode)\
        .order_by('-discovertime').distinct()
    qu= append_cat(qu, 'T_INFO_MAIN')
    
    start= (page-1) * perpage
    end = page*perpage
    ls =[]
    for item in qu[start:end]:
        dc = model_to_dict(item)
        dc.update({
            'bcname':item.bcname,
            'scname':item.scname,
        })
        ls.append(dc)
    return ls    

def jianduTask(taskids): 
    """批量获取监督员案件信息
    @taskids:['23124','23255']
    """
    query =  TInfoMain.objects.filter(taskid__in = taskids)
    ls = []
    for item in query:
        dc = model_to_dict(item)
        ls.append(dc)
    return ls 

def keeperTrack(keeper,startTime,endTime):
    ls=[]
    for track in TKeeperstrack.objects.filter(keepersn=keeper,tracktime__gte=startTime,tracktime__lte=endTime).order_by('tracktime'):
        ls.append({
            'coordx':track.coordx,
            'coordy':track.coordy,
            'tracktime':track.tracktime.strftime('%Y-%m-%d %H:%M:%S')
        })
    return ls
    


def append_cat(query,model_name):
    #return query.extra(select={'bcname':'"T_CLASSINFO"."infobcname"','scname':'T_CLASSINFO.infoscname'},
    #tables=['T_CLASSINFO'],where=['"T_CLASSINFO"."infotypeid"="T_INFO_MAIN"."infotypeid"',
    #'"T_CLASSINFO"."infobccode"="T_INFO_MAIN"."infobccode"'])    
    return query.extra(select={'bcname':'T_CLASSINFO.infobcname','scname':'T_CLASSINFO.infoscname'},
                       tables=['T_CLASSINFO'],where=['T_CLASSINFO.infotypeid=%s.infotypeid'%model_name,
                                                    'T_CLASSINFO.infobccode=%s.infobccode'%model_name,
                                                    'T_CLASSINFO.infosccode=%s.infosccode'%model_name])