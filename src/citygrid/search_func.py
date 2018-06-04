
from .models import TInfoMain,TInsCaseMain
from django.forms.models import model_to_dict

def get_ducha(page=1,perpage=200):
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


def append_cat(query,model_name):
    #return query.extra(select={'bcname':'"T_CLASSINFO"."infobcname"','scname':'T_CLASSINFO.infoscname'},
    #tables=['T_CLASSINFO'],where=['"T_CLASSINFO"."infotypeid"="T_INFO_MAIN"."infotypeid"',
    #'"T_CLASSINFO"."infobccode"="T_INFO_MAIN"."infobccode"'])    
    return query.extra(select={'bcname':'T_CLASSINFO.infobcname','scname':'T_CLASSINFO.infoscname'},
                       tables=['T_CLASSINFO'],where=['T_CLASSINFO.infotypeid=%s.infotypeid'%model_name,
                                                    'T_CLASSINFO.infobccode=%s.infobccode'%model_name,
                                                    'T_CLASSINFO.infosccode=%s.infosccode'%model_name])