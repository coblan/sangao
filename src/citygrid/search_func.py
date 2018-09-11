
from .models import TInfoMain,TInsCaseMain,TKeeperstrack,TTaskinfo,TInfoSolving
from . import models as citygrid_models
from django.forms.models import model_to_dict
from django.db.models.aggregates import Count,Sum
from django.db.models import Q,Exists, OuterRef,Func,F,Case,When,IntegerField,FloatField
from django.db.models.functions import Cast
from  django.utils.timezone import datetime,timedelta
from django.db import connection
from  .zhaoxiang_report_sql import hotline_shouli,hotline_2_you

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
        dc = model_to_dict(item,exclude=['deptcode'])
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

def zhaoxiang_hotline_report(start,end):
    dc ={
        'start_time':start,
        'end_time':end
    }
    cursor = connection.cursor()
    cursor.execute(hotline_shouli%dc )
    a1 = []
    for i in cursor:
        a1.append(i)
    cursor.execute(hotline_2_you%dc)
    a2=[]
    for i in cursor:
        a2.append(i)  
    
    return {
        'a1':a1,
        'a2':a2
    }


def zhaoxiang_hotline_report_old(start,end,):
    """
    @start:2018-06-01 00:00:00
    @start:2018-06-30 23:59:59

    SELECT
	TASKID 任务号,
	TO_CHAR ( PERCREATETIME, 'yyyy-mm-dd hh24:mi' ) 受理时间,
	HOTLINESN 热线 12345工单编号,
	CITYGRID.F_TASK_ISAPPROACH ( APPROACH ) 热线 12345工单类型,
	CITYGRID.F_SMRX_HOTJS_TYPE_BYID ( taskid ) 热线 12345业务类型,
	CITYGRID.F_SMRX_HOTJS_SOURCE_BYID ( taskid ) 热线 12345工单来源,
	CITYGRID.F_SMRX_HOTJS_ISREPEAT ( taskid ) 热线 12345工单是否重复,
	CITYGRID.F_SMRX_HOTJS_REWPID ( taskid ) 热线 12345重复工单号,
	CITYGRID.F_REC_MAINDEPTNAME ( EXECUTEDEPTCODE, DEPTCODE, TASKID ) 主责部门,
	CITYGRID.F_REC_THREEDEPTNAME ( EXECUTEDEPTCODE, DEPTCODE, TASKID ) 三级主责部门,
CASE
	ISFIRSTCONTACT 
	WHEN 1 THEN
	'是' 
	WHEN 0 THEN
	'否' 
	WHEN 2 THEN
	'未评价' 
	END 先行联系,
	ResultTypename_bf 解决情况,
	ALLMANYINAME_BF 综合满意度,
	CaseValuationName 结案评判 
FROM
	CITYGRID.T_TASKINFO main 
WHERE
	1 = 1 
	AND discovertime BETWEEN TO_DATE ( '2018-06-01 00:00:00', 'yyyy-MM-dd HH24:mi:ss' ) 
	AND TO_DATE ( '2018-06-30 23:59:59', 'yyyy-MM-dd HH24:mi:ss' ) 
	AND InfoSourceid IN ( 10, 68 ) 
	AND (
	EXISTS (
SELECT
	1 
FROM
	CITYGRID.t_info_solving ts 
WHERE
	( ts.executedeptcode = '20601' OR ts.DeptCode= '20601' ) 
	AND ts.taskid= main.taskid 
	AND ts.status != 3 
	) 
	OR main.deptcode = '20601')
    """
    """  居委   村委     ratio * 5 """
    sovle= TInfoSolving.objects.filter(
        taskid=OuterRef('pk')).filter(
        Q(executedeptcode='20601')|Q(deptcode='20601')).exclude(status=3).only('id')
    
    q1 = TTaskinfo.objects.filter(discovertime__gte=start,discovertime__lte=end,).filter(infosourceid__in=[10,68],)\
        .annotate(is_ok=Exists(sovle ))\
        .filter( Q(deptcode='20601')| Q(is_ok=True))
    q1 = q1.annotate(three = Func(F('executedeptcode'), F('deptcode'),F('taskid'),function='F_REC_THREEDEPTNAME'))
    
    a1 =q1.values('three').annotate(shou_li = Count('three'))
    
  
    q2 = TTaskinfo.objects.filter(endtime__gte=start,endtime__lte=end,).filter(infosourceid__in=[10,68],)\
        .annotate(is_ok=Exists(sovle ))\
        .filter( Q(deptcode='20601')| Q(is_ok=True))
    
    q2 = q2.annotate(three = Func(F('executedeptcode'), F('deptcode'),F('taskid'),function='F_REC_THREEDEPTNAME'))
    
    
    a2_1=q2.values('three').annotate(sou_count =Count('three'))

    a2_2 =a2_1.annotate(first_yes=Sum( Case(When(isfirstcontact=1, then=1),default=0 ,output_field=IntegerField()) )) \
        .annotate(first_no =Sum( Case(When(isfirstcontact=0, then=1),default=0 ,output_field=IntegerField()) ))
        #.annotate(first_total = F('first_yes')+F('first_no'))\
        #.annotate(first_ratio=Case(When(first_total=0, then=1),default=F('first_yes')/F('first_total'),output_field=FloatField() ))
    
    a2_4= a2_2.annotate(real_solve=Sum(Case(When(casevaluationname='实际解决',then=1),default=0,output_field=IntegerField())))\
        .annotate(jie_solve=Sum(Case(When(casevaluationname='解释说明',then=1),default=0,output_field=IntegerField())))
        #.annotate(total_solve=F('real_solve')+F('jie_solve'))\
        #.annotate(real_solve_ratio=Case(When(total_solve=0,then=0),default= F('real_solve')/ F('total_solve'),output_field=FloatField() ))\
        #.annotate(jie_solve_ratio=Case(When(total_solve=0,then=0),default= F('jie_solve')/ F('total_solve'),output_field=FloatField() ))
    
    a2_5 =a2_4.annotate(man_yi=Sum(Case(When(allmanyiname_bf='满意',then=1),\
                                        When(allmanyiname_bf='基本满意', then=0.8),
                                        When( allmanyiname_bf='一般',then=0.6 ),
                                        default=0, output_field=FloatField()  )))\
        .annotate( man_yi_total=Sum(Case(When( allmanyiname_bf__in=['满意','基本满意','一般','不满意'] ,then=1  ),default=0  ,output_field=IntegerField() )) ) \
        #.annotate(man_yi_ratio = Case(When(man_yi_total=0,then=0),default= F('man_yi')/F('man_yi_total') , output_field=FloatField() ))
    a1=list(a1)
    a2=list(a2_5)
    
    out_dict = {
        'a1':a1,
        'a2':a2
    }

    return out_dict

    
def zhaoxiang_grid_report(datestr):
    """
    """
    first_day_str = datetime.strptime(datestr,'%Y-%m-%d').replace(day=1).strftime('%Y-%m-%d')
    crt_day_start = datestr+' 00:00:00'
    crt_day_end =datestr+' 23:59:59'
    first_day_start=first_day_str+' 00:00:00'
    
    sovle= TInfoSolving.objects.filter(
        taskid=OuterRef('pk')).filter(
        Q(executedeptcode='20601')|Q(deptcode='20601')).exclude(status=3).only('id')
    
    q1 = TTaskinfo.objects.filter(discovertime__gte=crt_day_start,discovertime__lte=crt_day_end)\
        .filter(streetcode='1806',infosourceid=1)\
        .filter(status__in=[3, 4, 5, 6, 7, 8, 9,100])\
        .annotate(is_exist=Exists(sovle )).filter(is_exist=True)
    
    q1 = q1.annotate(three = Func(F('executedeptcode'), F('deptcode'),F('taskid'),function='F_REC_THREEDEPTNAME'))
    a1 = q1.values('three')\
        .annotate(count_all = Count(1))\
        .annotate(count_bu = Sum(Case( When(infotypename='部件',then=1),default=0), output_field=IntegerField() ) ) \
        .annotate(count_shi = Sum(Case(When(infotypename='事件', then=1),default=0 ),  output_field=IntegerField() ))
    
    q2=TTaskinfo.objects.filter(discovertime__gte=first_day_start,discovertime__lte=crt_day_end)\
        .filter(streetcode='1806')\
        .filter(status__in=[3, 4, 5, 6, 7, 8, 9,100])\
        .annotate(is_exist=Exists(sovle )).filter(is_exist=True)
    
    q2 = q2.annotate(three = Func(F('executedeptcode'), F('deptcode'),F('taskid'),function='F_REC_THREEDEPTNAME'))
    
    a2=q2 .filter(infosourceid= 36).values('three')\
        .annotate(count_cun=Count(1  ))
    
    a3=q2.filter(infosourceid= 61).filter(three__isnull=True).values('reporter')\
        .annotate(count_wei= Count(1)  )
    
    a4=q2.filter(infosourceid= 1).values('upkeepername')\
        .annotate(count_keeper=Count(1))
    
    a1=list(a1)
    a2=list(a2)
    a3=list(a3)
    a4=list(a4)
    out_dict = {
        'a1':a1,
        'a2':a2,
        'a3':a3,
        'a4':a4
    }
    return out_dict