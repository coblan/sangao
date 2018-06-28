
from .models import TInfoMain,TInsCaseMain,TKeeperstrack
from django.forms.models import model_to_dict

def get_ducha(page=1,perpage=200):
    """获取赵巷的督查员案件"""
    qu = TInsCaseMain.objects.filter(status__in=[3 ,-2,-1],streetcode =1806).order_by('-discovertime').distinct()
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

def get_jiandu(start,end,page=1,perpage=200):
    """获取赵巷的监督员案件"""
    qu = TInfoMain.objects.filter(status__in=[0,1,2,3,4,5,6,7,8,15,16,17],
                                  discovertime__gt=start,
                                  discovertime__lte=end,
                                  streetcode =1806)\
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

def keeperTrack(keepers,startTime,endTime):
    dc={}
    for keeper in TKeeperstrack.objects.filter(keepersn__in=keepers,tracktime__gte=startTime,tracktime__lte=endTime).order_by('tracktime'):
        if keeper.keepersn not in dc:
            dc[keeper.keepersn]=[]
        dc[keeper.keepersn].append(model_to_dict(keeper))
    return dc
    


def append_cat(query,model_name):
    #return query.extra(select={'bcname':'"T_CLASSINFO"."infobcname"','scname':'T_CLASSINFO.infoscname'},
    #tables=['T_CLASSINFO'],where=['"T_CLASSINFO"."infotypeid"="T_INFO_MAIN"."infotypeid"',
    #'"T_CLASSINFO"."infobccode"="T_INFO_MAIN"."infobccode"'])    
    return query.extra(select={'bcname':'T_CLASSINFO.infobcname','scname':'T_CLASSINFO.infoscname'},
                       tables=['T_CLASSINFO'],where=['T_CLASSINFO.infotypeid=%s.infotypeid'%model_name,
                                                    'T_CLASSINFO.infobccode=%s.infobccode'%model_name,
                                                    'T_CLASSINFO.infosccode=%s.infosccode'%model_name])