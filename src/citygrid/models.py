# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from . model_pkg.taskinfo import TTaskinfo,TInfoSolving

class TInfoMain(models.Model):
    """监督员案件"""
    #id = models.FloatField()
    taskid = models.CharField(primary_key=True, max_length=20)
    streetcode = models.CharField(max_length=4, blank=True, null=True)
    communitycode = models.CharField(max_length=8, blank=True, null=True)
    keepersn = models.CharField(max_length=12, blank=True, null=True)
    gridcode = models.CharField(max_length=12, blank=True, null=True)
    infobccode = models.CharField(max_length=2)
    infosccode = models.CharField(max_length=2)
    infotypeid = models.FloatField()
    description = models.CharField(max_length=2000, blank=True, null=True)
    partsn = models.CharField(max_length=14, blank=True, null=True)
    coordx = models.FloatField(blank=True, null=True)
    coordy = models.FloatField(blank=True, null=True)
    status = models.FloatField()
    casesn = models.CharField(max_length=100, blank=True, null=True)
    discovertime = models.DateField(blank=True, null=True)
    createtime = models.DateField(blank=True, null=True)
    dispatchtime = models.DateField(blank=True, null=True)
    solvingtime = models.DateField(blank=True, null=True)
    endtime = models.DateField(blank=True, null=True)
    inserttime = models.DateField()
    insertuser = models.CharField(max_length=100, blank=True, null=True)
    updatetime = models.DateField()
    updateuser = models.CharField(max_length=100, blank=True, null=True)
    pri = models.NullBooleanField()
    tag = models.CharField(max_length=1)
    partstate = models.CharField(max_length=10, blank=True, null=True)
    imagefilename = models.CharField(max_length=3000, blank=True, null=True)
    wavfilename = models.CharField(max_length=500, blank=True, null=True)
    checkimage = models.CharField(max_length=3000, blank=True, null=True)
    checkwav = models.CharField(max_length=500, blank=True, null=True)
    infosourceid = models.IntegerField()
    address = models.CharField(max_length=1000, blank=True, null=True)
    hotlinesn = models.CharField(max_length=100, blank=True, null=True)
    lastarrivetime = models.DateField(blank=True, null=True)
    lastsolvingtime = models.DateField(blank=True, null=True)
    supervisetime = models.DateField(blank=True, null=True)
    #deptcode = models.CharField(max_length=10)
    deptcode = models.ForeignKey(to='TDeptsinfo',db_constraint=False,to_field='deptcode',db_column='DEPTCODE', blank=True, null=True)
    haslead = models.BooleanField()
    hasback = models.BooleanField()
    verifyresult = models.BooleanField()
    checkresult = models.BooleanField()
    reporter = models.CharField(max_length=50, blank=True, null=True)
    contactinfo = models.CharField(max_length=100, blank=True, null=True)
    heshi = models.FloatField(blank=True, null=True)
    hecha = models.FloatField(blank=True, null=True)
    ispriorityarea = models.CharField(max_length=1, blank=True, null=True)
    priorityarea = models.CharField(max_length=100, blank=True, null=True)
    approach = models.IntegerField(blank=True, null=True)
    urgentdegree = models.IntegerField(blank=True, null=True)
    servicetype = models.CharField(max_length=30, blank=True, null=True)
    infozccode = models.CharField(max_length=2, blank=True, null=True)
    executedeptcode = models.CharField(max_length=20, blank=True, null=True)
    ordersn = models.FloatField(blank=True, null=True)
    infoatcode = models.CharField(max_length=20, blank=True, null=True)
    hasleadtype = models.FloatField(blank=True, null=True)
    similarcasesn = models.CharField(max_length=20, blank=True, null=True)
    limit_time = models.CharField(max_length=30, blank=True, null=True)
    userevaluate = models.FloatField(blank=True, null=True)
    issolving = models.FloatField(blank=True, null=True)
    telasktype = models.FloatField(blank=True, null=True)
    allmiddletime = models.DateField(blank=True, null=True)
    allimportanttime = models.DateField(blank=True, null=True)
    allendtime = models.DateField(blank=True, null=True)
    isrepeat = models.CharField(max_length=20, blank=True, null=True)
    ishuifang = models.FloatField(blank=True, null=True)
    contactmode = models.CharField(max_length=50, blank=True, null=True)
    sessionid = models.FloatField(blank=True, null=True)
    reportperson = models.CharField(max_length=20, blank=True, null=True)
    callnumber = models.CharField(max_length=20, blank=True, null=True)
    isanonymity = models.FloatField(blank=True, null=True)
    area = models.CharField(max_length=20, blank=True, null=True)
    urge_count = models.FloatField(blank=True, null=True)
    caseend = models.FloatField(blank=True, null=True)
    technologicalindex = models.FloatField(blank=True, null=True)
    firsthanddeptcode = models.CharField(max_length=50, blank=True, null=True)
    hasleadtypecount = models.FloatField(blank=True, null=True)
    trackhandtype = models.FloatField(blank=True, null=True)
    trackhandtypecount = models.FloatField(blank=True, null=True)
    checkhandtype = models.FloatField(blank=True, null=True)
    checkhandtypecount = models.FloatField(blank=True, null=True)
    leaderhandtype = models.FloatField(blank=True, null=True)
    leaderhandtypecount = models.FloatField(blank=True, null=True)
    hastentype = models.FloatField(blank=True, null=True)
    hastentypecount = models.FloatField(blank=True, null=True)
    isnt = models.FloatField(blank=True, null=True)
    middlesolvingtime = models.DateField(blank=True, null=True)
    importantsolvingtime = models.DateField(blank=True, null=True)
    querycode = models.CharField(max_length=10, blank=True, null=True)
    isendcaseback = models.FloatField(blank=True, null=True)
    du_limit = models.CharField(max_length=10, blank=True, null=True)
    isfeedbak = models.FloatField(blank=True, null=True)
    is_weixian = models.FloatField(blank=True, null=True)
    hechacount = models.FloatField(blank=True, null=True)
    heshicount = models.FloatField(blank=True, null=True)
    callback_flag = models.CharField(max_length=2, blank=True, null=True)
    isspotcheck = models.FloatField(blank=True, null=True)
    ishasmsg = models.FloatField(blank=True, null=True)
    spotcheckresult = models.CharField(max_length=100, blank=True, null=True)
    risklevel = models.FloatField(blank=True, null=True)
    percreatetime = models.DateField(blank=True, null=True)
    isreward = models.BigIntegerField(blank=True, null=True)
    plots = models.CharField(max_length=20, blank=True, null=True)
    reptheme = models.CharField(max_length=500, blank=True, null=True)
    source = models.CharField(max_length=5, blank=True, null=True)
    reportsource = models.FloatField(blank=True, null=True)
    reportdept = models.FloatField(blank=True, null=True)
    reportindustry = models.FloatField(blank=True, null=True)
    banliresult = models.FloatField(blank=True, null=True)
    isthreatened = models.NullBooleanField()
    isvisit = models.FloatField(blank=True, null=True)
    isscenery = models.FloatField(blank=True, null=True)
    casevaluation = models.FloatField(blank=True, null=True)
    visitcount = models.FloatField(blank=True, null=True)
    isstubborn = models.FloatField(blank=True, null=True)
    istypical = models.FloatField(blank=True, null=True)
    scenerycode = models.CharField(max_length=20, blank=True, null=True)
    speicalsign = models.CharField(max_length=500, blank=True, null=True)
    hotpoint = models.CharField(max_length=500, blank=True, null=True)
    singledeptbacktimes = models.FloatField(blank=True, null=True)
    severaldeptbacktimes = models.FloatField(blank=True, null=True)
    isrework = models.NullBooleanField()
    jzaudittype = models.FloatField(blank=True, null=True)
    dubanzt = models.FloatField(blank=True, null=True)
    caseendbccode = models.CharField(max_length=20, blank=True, null=True)
    caseendsccode = models.CharField(max_length=20, blank=True, null=True)
    assignhotlinetaskid = models.CharField(max_length=20, blank=True, null=True)
    isfast = models.FloatField(blank=True, null=True)
    isdelaystreet = models.FloatField(blank=True, null=True)
    taskupcode = models.CharField(max_length=50, blank=True, null=True)
    back_count = models.FloatField(blank=True, null=True)
    assign_flag = models.FloatField(blank=True, null=True)
    wp_source = models.CharField(max_length=50, blank=True, null=True)
    isproblem = models.CharField(max_length=1, blank=True, null=True)
    newgridcode = models.CharField(max_length=50, blank=True, null=True)
    newworkgridcode = models.CharField(max_length=50, blank=True, null=True)
    newstreetcode = models.CharField(max_length=50, blank=True, null=True)
    documenttype = models.FloatField(blank=True, null=True)
    documentnumber = models.CharField(max_length=100, blank=True, null=True)
    contactaddress = models.CharField(max_length=1000, blank=True, null=True)
    stubborndescription = models.CharField(max_length=1000, blank=True, null=True)
    isunlock = models.FloatField(blank=True, null=True)
    wgcallback_flag = models.CharField(max_length=2, blank=True, null=True)
    isreportauthority = models.FloatField(blank=True, null=True)
    reminder = models.FloatField(blank=True, null=True)
    allbacktime = models.DateField(blank=True, null=True)
    alldelaytime = models.DateField(blank=True, null=True)
    hashotlinereminders = models.FloatField(blank=True, null=True)
    casebrief = models.CharField(max_length=1000, blank=True, null=True)
    hftu_flag = models.CharField(max_length=2, blank=True, null=True)
    sections = models.CharField(max_length=80, blank=True, null=True)
    untrueworkorder = models.FloatField(blank=True, null=True)
    isareafuhe = models.FloatField(blank=True, null=True)
    isfollowup = models.FloatField(blank=True, null=True)
    isliehide = models.FloatField(blank=True, null=True)
    isthreensatisfied = models.FloatField(blank=True, null=True)
    housingestate = models.CharField(max_length=100, blank=True, null=True)
    isstreetvist = models.FloatField(blank=True, null=True)
    isendcaseverify = models.FloatField(blank=True, null=True)
    ishotlineduban = models.CharField(max_length=10, blank=True, null=True)
    rivercode = models.CharField(max_length=20, blank=True, null=True)
    isdefined = models.FloatField(blank=True, null=True)
    oldtaskid = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_INFO_MAIN'


    
class TInsCaseMain(models.Model):
    #id = models.BigIntegerField(primary_key=True)
    planid = models.IntegerField(blank=True, null=True)
    taskid = models.CharField(max_length=100, blank=True, null=True)
    infotypeid = models.IntegerField(blank=True, null=True)
    infobccode = models.CharField(max_length=2, blank=True, null=True)
    infosccode = models.CharField(max_length=2, blank=True, null=True)
    streetcode = models.CharField(max_length=4, blank=True, null=True)
    communitycode = models.CharField(max_length=8, blank=True, null=True)
    discovertime = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    coordx = models.FloatField(blank=True, null=True)
    coordy = models.FloatField(blank=True, null=True)
    keepersn = models.CharField(max_length=30, blank=True, null=True)
    remark = models.CharField(max_length=1000, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    infosourceid = models.IntegerField(blank=True, null=True)
    imagefilename = models.CharField(max_length=3000, blank=True, null=True)
    wavfilename = models.CharField(max_length=500, blank=True, null=True)
    checkimage = models.CharField(max_length=3000, blank=True, null=True)
    checkwav = models.CharField(max_length=500, blank=True, null=True)
    isreturn = models.NullBooleanField()
    isauditreturn = models.NullBooleanField()
    checkstatus = models.NullBooleanField()
    isdisclose = models.NullBooleanField()
    checktime = models.DateField(blank=True, null=True)
    checkmethod = models.CharField(max_length=30, blank=True, null=True)
    rejectreason = models.CharField(max_length=100, blank=True, null=True)
    reftaskid = models.CharField(max_length=50, blank=True, null=True)
    reportttime = models.DateField(blank=True, null=True)
    chkkeeperoptime = models.DateField(blank=True, null=True)
    chkkeepersn = models.CharField(max_length=30, blank=True, null=True)
    canceltime = models.DateField(blank=True, null=True)
    feedbackday = models.IntegerField(blank=True, null=True)
    feedbacktime = models.DateField(blank=True, null=True)
    valid = models.NullBooleanField()
    insertuser = models.CharField(max_length=100, blank=True, null=True)
    inserttime = models.DateField()
    updateuser = models.CharField(max_length=100, blank=True, null=True)
    updatetime = models.DateField()
    gridcode = models.CharField(max_length=50, blank=True, null=True)
    verifyresult = models.NullBooleanField()
    heshi = models.NullBooleanField()
    duban = models.NullBooleanField()
    dubanreason = models.CharField(max_length=10, blank=True, null=True)
    isreview = models.NullBooleanField()
    streetfeedbacktime = models.DateField(blank=True, null=True)
    astepstatus = models.IntegerField(blank=True, null=True)
    if_extended = models.CharField(max_length=10, blank=True, null=True)
    receivemethod = models.CharField(max_length=30, blank=True, null=True)
    frejectreason = models.CharField(max_length=100, blank=True, null=True)
    freftaskid = models.CharField(max_length=50, blank=True, null=True)
    partsn = models.CharField(max_length=14, blank=True, null=True)
    iscaseback = models.IntegerField(blank=True, null=True)
    priorityarea = models.CharField(max_length=100, blank=True, null=True)
    sections = models.CharField(max_length=80, blank=True, null=True)
    weixinaward = models.FloatField(blank=True, null=True)
    streetkeepername = models.CharField(max_length=10, blank=True, null=True)
    iscityback = models.FloatField(blank=True, null=True)
    reasonsfornotcreateother = models.CharField(max_length=200, blank=True, null=True)
    hotlinesn = models.CharField(max_length=100, blank=True, null=True)
    duedate = models.DateField(blank=True, null=True)
    duedatenote = models.CharField(max_length=500, blank=True, null=True)
    turntracking = models.CharField(max_length=20, blank=True, null=True)
    dueresult = models.CharField(max_length=20, blank=True, null=True)
    awardamount = models.IntegerField(blank=True, null=True)
    hascreatedfromturntrack = models.CharField(max_length=20, blank=True, null=True)
    #deptcode = models.CharField(max_length=20, blank=True, null=True)
    deptcode = models.ForeignKey(to='TDeptsinfo',db_constraint=False,to_field='deptcode',db_column='DEPTCODE', blank=True, null=True)
    fromusername = models.CharField(max_length=100, blank=True, null=True)
    isrediscuss = models.CharField(max_length=10, blank=True, null=True)
    isintervened = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_INS_CASE_MAIN'
        
        
    
class TClassinfo(models.Model):
    #id = models.FloatField()
    classcode = models.CharField(max_length=2, blank=True, null=True)
    classname = models.CharField(max_length=10, blank=True, null=True)
    infotypeid = models.CharField(max_length=2, blank=True, null=True)
    infotypename = models.CharField(max_length=50, blank=True, null=True)
    infobccode = models.CharField(max_length=2, blank=True, null=True)
    infobcname = models.CharField(max_length=50, blank=True, null=True)
    infosccode = models.CharField(max_length=2, blank=True, null=True)
    infoscname = models.CharField(max_length=100, blank=True, null=True)
    infozccode = models.CharField(max_length=50, blank=True, null=True)
    infozcname = models.CharField(max_length=200, blank=True, null=True)
    csolvingtime = models.FloatField(blank=True, null=True)
    carrivetime = models.FloatField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    alltime = models.FloatField(blank=True, null=True)
    deptcode = models.CharField(max_length=100, blank=True, null=True)
    inserttime = models.DateField(blank=True, null=True)
    isstandard = models.FloatField(blank=True, null=True)
    grouptype = models.FloatField(blank=True, null=True)
    solvingtimelist = models.CharField(max_length=200, blank=True, null=True)
    arrivetimelist = models.CharField(max_length=200, blank=True, null=True)
    remark = models.CharField(max_length=1000, blank=True, null=True)
    createthreeimage = models.CharField(max_length=100, blank=True, null=True)
    createtwoimage = models.CharField(max_length=100, blank=True, null=True)
    createoneimage = models.CharField(max_length=100, blank=True, null=True)
    createzeroimage = models.CharField(max_length=100, blank=True, null=True)
    createimage = models.TextField(blank=True, null=True)
    createimagenum = models.FloatField(blank=True, null=True)
    endthreeimage = models.CharField(max_length=100, blank=True, null=True)
    endtwoimage = models.CharField(max_length=100, blank=True, null=True)
    endoneimage = models.CharField(max_length=100, blank=True, null=True)
    endzeroimage = models.CharField(max_length=100, blank=True, null=True)
    endimage = models.TextField(blank=True, null=True)
    endimagenum = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_CLASSINFO'
        
        
        
    
class TKeeperstrack(models.Model):
    """监督员轨迹"""
    #id = models.IntegerField()
    keepersn = models.CharField(max_length=30)
    tracktime = models.DateTimeField()
    coordx = models.FloatField()
    coordy = models.FloatField()
    workgridcode = models.CharField(max_length=8, blank=True, null=True)
    inserttime = models.DateTimeField()
    errordesc = models.CharField(max_length=1000, blank=True, null=True)
    errorcode = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_KEEPERSTRACK'
        


class TDeptsinfo(models.Model):
    """
    tinfomain 中的  deptcode 外键  主者部门
    """
    #id = models.IntegerField()
    deptcode = models.CharField(max_length=10,unique=True)
    deptname = models.CharField(max_length=100, blank=True, null=True)
    deptaddress = models.CharField(max_length=200, blank=True, null=True)
    phoneno = models.CharField(max_length=30, blank=True, null=True)
    linkman = models.CharField(max_length=20, blank=True, null=True)
    depttype = models.NullBooleanField()
    note = models.CharField(max_length=500, blank=True, null=True)
    inserttime = models.DateField()
    status = models.CharField(max_length=1)
    linkmanid = models.CharField(max_length=100, blank=True, null=True)
    ordercode = models.BigIntegerField()
    platformid = models.FloatField()
    visible = models.FloatField()
    streetcode = models.CharField(max_length=20, blank=True, null=True)
    authorizeheshi = models.CharField(max_length=1)
    authorizehecha = models.CharField(max_length=1)
    sort = models.FloatField(blank=True, null=True)
    upcode = models.CharField(max_length=20, blank=True, null=True)
    self = models.CharField(max_length=20, blank=True, null=True)
    authorizetuijin = models.CharField(max_length=1, blank=True, null=True)
    tag = models.CharField(max_length=2, blank=True, null=True)
    iscountalltime = models.FloatField(blank=True, null=True)
    collectdeptlimits = models.CharField(max_length=20, blank=True, null=True)
    ishotlinedept = models.FloatField(blank=True, null=True)
    population = models.CharField(max_length=30, blank=True, null=True)
    iscommunity = models.FloatField(blank=True, null=True)
    relationunit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_DEPTSINFO'


