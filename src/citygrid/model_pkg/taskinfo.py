# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class TTaskinfo(models.Model):
    #id = models.FloatField()
    taskid = models.CharField(primary_key=True, max_length=20)
    casesn = models.CharField(max_length=100, blank=True, null=True)
    infosourceid = models.FloatField()
    discovertime = models.DateTimeField(blank=True, null=True)
    percreatetime = models.DateField(blank=True, null=True)
    createtime = models.DateField(blank=True, null=True)
    dispatchtime = models.DateField(blank=True, null=True)
    solvingtime = models.DateField(blank=True, null=True)
    stime = models.DateField(blank=True, null=True)
    supervisetime = models.DateField(blank=True, null=True)
    delaytime = models.DateField(blank=True, null=True)
    deptbacktime = models.DateField(blank=True, null=True)
    checkdelaytime = models.DateField(blank=True, null=True)
    checkdeptbacktime = models.DateField(blank=True, null=True)
    xiafaheshitime = models.DateField(blank=True, null=True)
    shangbaoheshitime = models.DateField(blank=True, null=True)
    xiafahechatime = models.DateField(blank=True, null=True)
    shangbaohechatime = models.DateField(blank=True, null=True)
    telasktime = models.DateField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    streetcode = models.CharField(max_length=4, blank=True, null=True)
    communitycode = models.CharField(max_length=8, blank=True, null=True)
    gridcode = models.CharField(max_length=20, blank=True, null=True)
    plots = models.CharField(max_length=20, blank=True, null=True)
    coordx = models.FloatField(blank=True, null=True)
    coordy = models.FloatField(blank=True, null=True)
    sections = models.CharField(max_length=200, blank=True, null=True)
    starsections = models.CharField(max_length=100, blank=True, null=True)
    endsections = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    infotypeid = models.FloatField(blank=True, null=True)
    infobccode = models.CharField(max_length=2, blank=True, null=True)
    infosccode = models.CharField(max_length=2, blank=True, null=True)
    infozccode = models.CharField(max_length=2, blank=True, null=True)
    infoatcode = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    solvingstatus = models.FloatField(blank=True, null=True)
    deptcode = models.CharField(max_length=20, blank=True, null=True)
    executedeptcode = models.CharField(max_length=20, blank=True, null=True)
    insertdeptcode = models.CharField(max_length=20, blank=True, null=True)
    keepersn = models.CharField(max_length=12, blank=True, null=True)
    insertuser = models.CharField(max_length=20, blank=True, null=True)
    percreateuser = models.CharField(max_length=20, blank=True, null=True)
    createuser = models.CharField(max_length=20, blank=True, null=True)
    dispatchuser = models.CharField(max_length=20, blank=True, null=True)
    solvinguser = models.CharField(max_length=100, blank=True, null=True)
    superviseuser = models.CharField(max_length=50, blank=True, null=True)
    xiafaheshiuser = models.CharField(max_length=20, blank=True, null=True)
    xiafahechauser = models.CharField(max_length=20, blank=True, null=True)
    heshikeepersn = models.CharField(max_length=20, blank=True, null=True)
    hechakeepersn = models.CharField(max_length=20, blank=True, null=True)
    telaskuser = models.CharField(max_length=20, blank=True, null=True)
    enduser = models.CharField(max_length=20, blank=True, null=True)
    canceluser = models.CharField(max_length=20, blank=True, null=True)
    urgentdegree = models.FloatField(blank=True, null=True)
    approach = models.FloatField(blank=True, null=True)
    similarcasesn = models.CharField(max_length=20, blank=True, null=True)
    servicetype = models.CharField(max_length=30, blank=True, null=True)
    isanonymity = models.FloatField(blank=True, null=True)
    risklevel = models.FloatField(blank=True, null=True)
    userevaluate = models.FloatField(blank=True, null=True)
    allmiddletime = models.DateField(blank=True, null=True)
    allimportanttime = models.DateField(blank=True, null=True)
    allendtime = models.DateField(blank=True, null=True)
    middlesolvingtime = models.DateField(blank=True, null=True)
    importantsolvingtime = models.DateField(blank=True, null=True)
    lastsolvingtime = models.DateField(blank=True, null=True)
    lastarrivetime = models.DateField(blank=True, null=True)
    callback_flag = models.FloatField(blank=True, null=True)
    urge_count = models.FloatField(blank=True, null=True)
    du_limit = models.CharField(max_length=10, blank=True, null=True)
    telasktype = models.FloatField(blank=True, null=True)
    reportsource = models.FloatField(blank=True, null=True)
    reportdept = models.FloatField(blank=True, null=True)
    reportindustry = models.FloatField(blank=True, null=True)
    issolving = models.FloatField(blank=True, null=True)
    caseend = models.FloatField(blank=True, null=True)
    isfeedbak = models.FloatField(blank=True, null=True)
    isreward = models.FloatField(blank=True, null=True)
    ishuifang = models.FloatField(blank=True, null=True)
    banliresult = models.FloatField(blank=True, null=True)
    endresult = models.FloatField(blank=True, null=True)
    verifyresult = models.FloatField(blank=True, null=True)
    checkresult = models.FloatField(blank=True, null=True)
    priorityarea = models.CharField(max_length=50, blank=True, null=True)
    callnumber = models.CharField(max_length=20, blank=True, null=True)
    contactmode = models.CharField(max_length=50, blank=True, null=True)
    discovernum = models.FloatField()
    percreatenum = models.FloatField()
    createnum = models.FloatField()
    dispatchnum = models.FloatField()
    fangongnum = models.FloatField()
    solvingnum = models.FloatField()
    jsarrivenum = models.FloatField()
    jscompletenum = models.FloatField()
    cqsolvingnum = models.FloatField()
    delaycount = models.FloatField()
    deptdelaycount = models.FloatField()
    backcount = models.FloatField()
    deptbackcount = models.FloatField()
    endnum = models.FloatField()
    huifangmanyi = models.FloatField(blank=True, null=True)
    heshicount = models.FloatField()
    hechacount = models.FloatField()
    huifangcount = models.FloatField()
    hasleadtypecount = models.FloatField()
    hastentypecount = models.FloatField()
    leaderhandtypecount = models.FloatField()
    trackhandtypecount = models.FloatField()
    checkhandtypecount = models.FloatField()
    spotcheckcount = models.FloatField()
    hotlinesn = models.CharField(max_length=100, blank=True, null=True)
    workgrid = models.CharField(max_length=12, blank=True, null=True)
    xexecutedeptcode = models.CharField(max_length=1000, blank=True, null=True)
    pexecutedeptcode = models.CharField(max_length=20, blank=True, null=True)
    subexecutedeptcode = models.CharField(max_length=20, blank=True, null=True)
    delaycheckuser = models.CharField(max_length=20, blank=True, null=True)
    backcheckuser = models.CharField(max_length=20, blank=True, null=True)
    hechakeepersns = models.CharField(max_length=1000, blank=True, null=True)
    heshiuser = models.CharField(max_length=20, blank=True, null=True)
    hechauser = models.CharField(max_length=20, blank=True, null=True)
    hechausers = models.CharField(max_length=500, blank=True, null=True)
    leadtypeuser = models.CharField(max_length=20, blank=True, null=True)
    tentypeuser = models.CharField(max_length=20, blank=True, null=True)
    lajguser = models.CharField(max_length=20, blank=True, null=True)
    xtjguser = models.CharField(max_length=20, blank=True, null=True)
    jajguser = models.CharField(max_length=20, blank=True, null=True)
    csolvingtime = models.CharField(max_length=50, blank=True, null=True)
    isspeical = models.FloatField(blank=True, null=True)
    speicalsign = models.CharField(max_length=500, blank=True, null=True)
    cqendnum = models.FloatField()
    lajgcount = models.FloatField()
    xtjgcount = models.FloatField()
    jajgcount = models.FloatField()
    firstcontacttime = models.DateField(blank=True, null=True)
    cancletime = models.DateField(blank=True, null=True)
    backdeptcodes = models.CharField(max_length=500, blank=True, null=True)
    backnotes = models.CharField(max_length=4000, blank=True, null=True)
    facilitytype = models.FloatField(blank=True, null=True)
    contactinfo = models.CharField(max_length=100, blank=True, null=True)
    accepttime = models.DateField(blank=True, null=True)
    lastcontacttime = models.DateField(blank=True, null=True)
    solvingresult = models.CharField(max_length=20, blank=True, null=True)
    allmanyi = models.FloatField(blank=True, null=True)
    gcmanyi = models.FloatField(blank=True, null=True)
    tdmanyi = models.FloatField(blank=True, null=True)
    resulttype = models.FloatField(blank=True, null=True)
    zzdeptcode = models.CharField(max_length=20, blank=True, null=True)
    firstdeptcode = models.CharField(max_length=20, blank=True, null=True)
    secenddeptcode = models.CharField(max_length=20, blank=True, null=True)
    infosourcename = models.CharField(max_length=20, blank=True, null=True)
    infotypename = models.CharField(max_length=100, blank=True, null=True)
    infobcname = models.CharField(max_length=100, blank=True, null=True)
    infoscname = models.CharField(max_length=100, blank=True, null=True)
    infozcname = models.CharField(max_length=100, blank=True, null=True)
    streetname = models.CharField(max_length=30, blank=True, null=True)
    communityname = models.CharField(max_length=50, blank=True, null=True)
    workgridcode = models.CharField(max_length=6, blank=True, null=True)
    upkeepername = models.CharField(max_length=30, blank=True, null=True)
    insertdeptname = models.CharField(max_length=100, blank=True, null=True)
    executedeptname = models.CharField(max_length=100, blank=True, null=True)
    hechakeepername = models.CharField(max_length=30, blank=True, null=True)
    reporter = models.CharField(max_length=50, blank=True, null=True)
    reportdeptname = models.CharField(max_length=30, blank=True, null=True)
    caseendbccode = models.CharField(max_length=20, blank=True, null=True)
    caseendsccode = models.CharField(max_length=20, blank=True, null=True)
    delaydeptcode = models.CharField(max_length=20, blank=True, null=True)
    requestnote = models.CharField(max_length=200, blank=True, null=True)
    caseendbcname = models.CharField(max_length=50, blank=True, null=True)
    caseendscname = models.CharField(max_length=50, blank=True, null=True)
    statusname = models.CharField(max_length=50, blank=True, null=True)
    userevaluatename = models.CharField(max_length=50, blank=True, null=True)
    jsarrivenumname = models.CharField(max_length=50, blank=True, null=True)
    atname = models.CharField(max_length=100, blank=True, null=True)
    xexecutedeptname = models.CharField(max_length=1000, blank=True, null=True)
    fangongnumname = models.CharField(max_length=50, blank=True, null=True)
    allmanyiname = models.CharField(max_length=50, blank=True, null=True)
    gcmanyiname = models.CharField(max_length=50, blank=True, null=True)
    tdmanyiname = models.CharField(max_length=50, blank=True, null=True)
    firstcontacttimename = models.CharField(max_length=50, blank=True, null=True)
    issolvingname = models.CharField(max_length=50, blank=True, null=True)
    resulttypename = models.CharField(max_length=50, blank=True, null=True)
    synctime = models.DateField(blank=True, null=True)
    isfirstcontact = models.FloatField(blank=True, null=True)
    deptname = models.CharField(max_length=100, blank=True, null=True)
    backresult = models.CharField(max_length=10, blank=True, null=True)
    delayresult = models.CharField(max_length=10, blank=True, null=True)
    casevaluation = models.FloatField(blank=True, null=True)
    backtocitynote = models.CharField(max_length=500, blank=True, null=True)
    delaydeptcodename = models.CharField(max_length=100, blank=True, null=True)
    newworkgridname = models.CharField(max_length=100, blank=True, null=True)
    subexecutedeptcode_mh = models.CharField(max_length=100, blank=True, null=True)
    subexecutedeptname_mh = models.CharField(max_length=100, blank=True, null=True)
    servicetypename = models.CharField(max_length=20, blank=True, null=True)
    solvinglight = models.CharField(max_length=20, blank=True, null=True)
    alllight = models.CharField(max_length=20, blank=True, null=True)
    replayform = models.CharField(max_length=20, blank=True, null=True)
    solvingnote = models.CharField(max_length=2000, blank=True, null=True)
    iscaseendname = models.CharField(max_length=20, blank=True, null=True)
    cancelnote = models.CharField(max_length=1000, blank=True, null=True)
    spotcheckresult = models.CharField(max_length=1000, blank=True, null=True)
    hechamanyiname = models.CharField(max_length=30, blank=True, null=True)
    is_weixiancode = models.CharField(max_length=20, blank=True, null=True)
    is_weixianname = models.CharField(max_length=100, blank=True, null=True)
    caseendnote = models.CharField(max_length=1000, blank=True, null=True)
    queryuservaluate = models.CharField(max_length=20, blank=True, null=True)
    queryfuwuvaluate = models.CharField(max_length=20, blank=True, null=True)
    queryvaluation = models.CharField(max_length=2000, blank=True, null=True)
    newworkgridcode = models.CharField(max_length=50, blank=True, null=True)
    casevaluationname = models.CharField(max_length=100, blank=True, null=True)
    ismainrepeartcase = models.NullBooleanField()
    appealtype = models.CharField(max_length=100, blank=True, null=True)
    facttype = models.CharField(max_length=100, blank=True, null=True)
    appealtypecode = models.CharField(max_length=100, blank=True, null=True)
    facttypecode = models.CharField(max_length=100, blank=True, null=True)
    zgexecutedeptcode = models.CharField(max_length=100, blank=True, null=True)
    istypical = models.CharField(max_length=50, blank=True, null=True)
    isstubborn = models.CharField(max_length=50, blank=True, null=True)
    haslead = models.CharField(max_length=50, blank=True, null=True)
    hastentype = models.CharField(max_length=50, blank=True, null=True)
    firsthanddeptcode = models.CharField(max_length=50, blank=True, null=True)
    querycode = models.CharField(max_length=50, blank=True, null=True)
    wp_source = models.CharField(max_length=50, blank=True, null=True)
    isthreatened = models.CharField(max_length=50, blank=True, null=True)
    ispriorityarea = models.CharField(max_length=50, blank=True, null=True)
    userevaluate2 = models.CharField(max_length=200, blank=True, null=True)
    wp_type = models.CharField(max_length=50, blank=True, null=True)
    similarcount = models.CharField(max_length=20, blank=True, null=True)
    repeatflag = models.CharField(max_length=20, blank=True, null=True)
    casenumber = models.FloatField(blank=True, null=True)
    repeatmarker = models.CharField(max_length=100, blank=True, null=True)
    hotjssource = models.CharField(max_length=100, blank=True, null=True)
    zgexecutedeptname = models.CharField(max_length=50, blank=True, null=True)
    hecha = models.CharField(max_length=50, blank=True, null=True)
    pexecutedeptcode_mh = models.CharField(max_length=50, blank=True, null=True)
    pexecutedeptname_mh = models.CharField(max_length=50, blank=True, null=True)
    first_contact = models.CharField(max_length=20, blank=True, null=True)
    satisfied_explain = models.CharField(max_length=500, blank=True, null=True)
    fact_explain = models.CharField(max_length=500, blank=True, null=True)
    reply_type = models.CharField(max_length=50, blank=True, null=True)
    reply_time = models.DateField(blank=True, null=True)
    reply_point = models.CharField(max_length=1000, blank=True, null=True)
    is_public = models.CharField(max_length=50, blank=True, null=True)
    level2_handler = models.CharField(max_length=50, blank=True, null=True)
    level2_charger = models.CharField(max_length=50, blank=True, null=True)
    badging_unit = models.CharField(max_length=100, blank=True, null=True)
    appeal_explain = models.CharField(max_length=500, blank=True, null=True)
    description_12345 = models.CharField(max_length=1000, blank=True, null=True)
    not_reason = models.CharField(max_length=50, blank=True, null=True)
    viewinfo = models.CharField(max_length=50, blank=True, null=True)
    casevaluation_12345 = models.FloatField(blank=True, null=True)
    banliresult_12345 = models.FloatField(blank=True, null=True)
    isfast = models.CharField(max_length=20, blank=True, null=True)
    result_12345 = models.CharField(max_length=2000, blank=True, null=True)
    isreply = models.CharField(max_length=20, blank=True, null=True)
    isdelaysolving = models.CharField(max_length=20, blank=True, null=True)
    supervisedate = models.DateField(blank=True, null=True)
    tentypedate = models.DateField(blank=True, null=True)
    updateuser = models.CharField(max_length=20, blank=True, null=True)
    heshiistimely = models.CharField(max_length=20, blank=True, null=True)
    hechaistimely = models.CharField(max_length=20, blank=True, null=True)
    grade_call = models.CharField(max_length=20, blank=True, null=True)
    gradename_call = models.CharField(max_length=50, blank=True, null=True)
    jssolvingnum = models.FloatField(blank=True, null=True)
    solvingresultinfo = models.CharField(max_length=300, blank=True, null=True)
    subexecutedeptcode_jd = models.CharField(max_length=50, blank=True, null=True)
    dispatchnote = models.CharField(max_length=2000, blank=True, null=True)
    endnote = models.CharField(max_length=2000, blank=True, null=True)
    partsn = models.CharField(max_length=14, blank=True, null=True)
    imagefilename = models.CharField(max_length=3000, blank=True, null=True)
    wavfilename = models.CharField(max_length=500, blank=True, null=True)
    checkimage = models.CharField(max_length=3000, blank=True, null=True)
    checkwav = models.CharField(max_length=500, blank=True, null=True)
    areacode = models.CharField(max_length=20, blank=True, null=True)
    isstandard = models.CharField(max_length=20, blank=True, null=True)
    isspotcheck = models.CharField(max_length=20, blank=True, null=True)
    queryuservaluatecode = models.CharField(max_length=50, blank=True, null=True)
    queryfuwuvaluatecode = models.CharField(max_length=50, blank=True, null=True)
    hechamanyicode = models.CharField(max_length=50, blank=True, null=True)
    lasttakecasetime = models.DateField(blank=True, null=True)
    tentypenote = models.CharField(max_length=2000, blank=True, null=True)
    isfirstcontactname = models.CharField(max_length=50, blank=True, null=True)
    hechaistimelyname = models.CharField(max_length=50, blank=True, null=True)
    heshiistimelyname = models.CharField(max_length=50, blank=True, null=True)
    inertview = models.CharField(max_length=2000, blank=True, null=True)
    endresultnew = models.CharField(max_length=1000, blank=True, null=True)
    newworkgridtype = models.CharField(max_length=50, blank=True, null=True)
    hotpoint = models.CharField(max_length=500, blank=True, null=True)
    heshi = models.CharField(max_length=50, blank=True, null=True)
    infotbscode = models.CharField(max_length=50, blank=True, null=True)
    biinfosourceid = models.CharField(max_length=50, blank=True, null=True)
    wechatevaluate = models.CharField(max_length=50, blank=True, null=True)
    wechatevaluatename = models.CharField(max_length=50, blank=True, null=True)
    replayformname = models.CharField(max_length=20, blank=True, null=True)
    lastdisexecdeptcode = models.CharField(max_length=20, blank=True, null=True)
    lastdisexecdeptname = models.CharField(max_length=50, blank=True, null=True)
    satisfied = models.CharField(max_length=100, blank=True, null=True)
    manyi_12345 = models.CharField(max_length=10, blank=True, null=True)
    wgcallback_flag = models.CharField(max_length=2, blank=True, null=True)
    qpexecutedeptcode = models.CharField(max_length=20, blank=True, null=True)
    feedbacktime_12345 = models.DateField(blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    istimelyend = models.CharField(max_length=2, blank=True, null=True)
    statisticaldeptcode = models.CharField(max_length=30, blank=True, null=True)
    statisticaldeptname = models.CharField(max_length=100, blank=True, null=True)
    hashotlinereminders = models.FloatField(blank=True, null=True)
    hadbackdeptcodes = models.CharField(max_length=2000, blank=True, null=True)
    hadbackdeptnames = models.CharField(max_length=3000, blank=True, null=True)
    jzzqlimittime = models.CharField(max_length=20, blank=True, null=True)
    qpdispatchtime = models.DateField(blank=True, null=True)
    qpsolvingtime = models.DateField(blank=True, null=True)
    expsatisfaction = models.FloatField(blank=True, null=True)
    expsatisfactiontime = models.DateField(blank=True, null=True)
    iscontact = models.FloatField(blank=True, null=True)
    contact_time = models.CharField(max_length=50, blank=True, null=True)
    facttype_sl = models.FloatField(blank=True, null=True)
    appealtype_sl = models.FloatField(blank=True, null=True)
    huifustyle_sl = models.CharField(max_length=50, blank=True, null=True)
    replytime_sl = models.DateField(blank=True, null=True)
    replynote_sl = models.CharField(max_length=2000, blank=True, null=True)
    manyitype = models.FloatField(blank=True, null=True)
    telasktype_bf = models.FloatField(blank=True, null=True)
    issolving_bf = models.FloatField(blank=True, null=True)
    isfirstcontract_bf = models.FloatField(blank=True, null=True)
    isreply_bf = models.FloatField(blank=True, null=True)
    userevaluate_bf = models.FloatField(blank=True, null=True)
    tdmanyi_bf = models.FloatField(blank=True, null=True)
    visittype = models.FloatField(blank=True, null=True)
    middispatchtime = models.DateField(blank=True, null=True)
    qplastsolvingtime = models.DateField(blank=True, null=True)
    lssueleaders = models.CharField(max_length=200, blank=True, null=True)
    axexecutedeptcode = models.CharField(max_length=2000, blank=True, null=True)
    axexecutedeptname = models.CharField(max_length=3000, blank=True, null=True)
    keeperdeptcode = models.CharField(max_length=50, blank=True, null=True)
    allmanyi_bf = models.FloatField(blank=True, null=True)
    allmanyiname_bf = models.CharField(max_length=50, blank=True, null=True)
    gcmanyi_bf = models.FloatField(blank=True, null=True)
    gcmanyiname_bf = models.CharField(max_length=50, blank=True, null=True)
    huifangmanyi_bf = models.FloatField(blank=True, null=True)
    inertview_bf = models.CharField(max_length=2000, blank=True, null=True)
    resulttype_bf = models.FloatField(blank=True, null=True)
    resulttypename_bf = models.CharField(max_length=50, blank=True, null=True)
    tdmanyiname_bf = models.CharField(max_length=50, blank=True, null=True)
    telaskuser_bf = models.CharField(max_length=50, blank=True, null=True)
    telasktime_bf = models.CharField(max_length=50, blank=True, null=True)
    issimplify = models.FloatField(blank=True, null=True)
    supevisenote = models.CharField(max_length=20, blank=True, null=True)
    ishotlineduban = models.CharField(max_length=20, blank=True, null=True)
    hasleadtype = models.FloatField(blank=True, null=True)
    firstdispatchtime = models.DateField(blank=True, null=True)
    telasktype_jz = models.FloatField(blank=True, null=True)
    issolving_jz = models.FloatField(blank=True, null=True)
    isfirstcontact_jz = models.FloatField(blank=True, null=True)
    resulttype_jz = models.FloatField(blank=True, null=True)
    tdmanyi_jz = models.FloatField(blank=True, null=True)
    gcmanyi_jz = models.FloatField(blank=True, null=True)
    userevaluate_jz = models.FloatField(blank=True, null=True)
    allmanyi_jz = models.FloatField(blank=True, null=True)
    inertview_jz = models.CharField(max_length=2000, blank=True, null=True)
    isreply_jz = models.FloatField(blank=True, null=True)
    enterpriseinvoled = models.FloatField(blank=True, null=True)
    enterpriseinvoledname = models.CharField(max_length=100, blank=True, null=True)
    areahandleresult = models.CharField(max_length=1, blank=True, null=True)
    areahandleresultname = models.CharField(max_length=100, blank=True, null=True)
    supervisiontype = models.CharField(max_length=10, blank=True, null=True)
    isupdate = models.FloatField(blank=True, null=True)
    lastupdatetime = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_TASKINFO'


class TInfoSolving(models.Model):
    #id = models.FloatField()
    taskid = models.CharField(max_length=20)
    #taskid = models.ForeignKey(TTaskinfo, max_length=20)
    dispatchuserid = models.CharField(max_length=100, blank=True, null=True)
    dispatchnote = models.CharField(max_length=800, blank=True, null=True)
    executedeptcode = models.CharField(max_length=20, blank=True, null=True)
    carrivetime = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    csolvingtime = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acceptuserid = models.CharField(max_length=100, blank=True, null=True)
    accepttime = models.DateField(blank=True, null=True)
    acceptnote = models.CharField(max_length=2000, blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    solvinguserid = models.CharField(max_length=100, blank=True, null=True)
    arrivetime = models.DateField(blank=True, null=True)
    solvingtime = models.DateField(blank=True, null=True)
    swritetime = models.DateField(blank=True, null=True)
    arriveperson = models.CharField(max_length=20, blank=True, null=True)
    arrivestate = models.NullBooleanField()
    localecircs = models.CharField(max_length=500, blank=True, null=True)
    solvingperson = models.CharField(max_length=20, blank=True, null=True)
    solvingstate = models.NullBooleanField()
    infosbccode = models.CharField(max_length=2, blank=True, null=True)
    infossccode = models.CharField(max_length=2, blank=True, null=True)
    solvingmeasure = models.CharField(max_length=50, blank=True, null=True)
    reason = models.CharField(max_length=50, blank=True, null=True)
    solvingresult = models.CharField(max_length=20, blank=True, null=True)
    solvingnote = models.CharField(max_length=2000, blank=True, null=True)
    inserttime = models.DateField()
    insertuser = models.CharField(max_length=100, blank=True, null=True)
    updatetime = models.DateField()
    updateuser = models.CharField(max_length=100, blank=True, null=True)
    tag = models.CharField(max_length=1)
    lockuserid = models.CharField(max_length=100, blank=True, null=True)
    lockoptype = models.CharField(max_length=10, blank=True, null=True)
    isdelay = models.CharField(max_length=1, blank=True, null=True)
    hotlinesn = models.CharField(max_length=20, blank=True, null=True)
    depttag = models.CharField(max_length=1, blank=True, null=True)
    lastarrivetime = models.DateField(blank=True, null=True)
    lastsolvingtime = models.DateField(blank=True, null=True)
    dispatchid = models.FloatField(blank=True, null=True)
    deptcode = models.CharField(max_length=10)
    rejectuserid = models.CharField(max_length=100, blank=True, null=True)
    rejectnote = models.CharField(max_length=500, blank=True, null=True)
    rejecttime = models.DateField(blank=True, null=True)
    dispatchsum = models.FloatField(blank=True, null=True)
    infoszccode = models.CharField(max_length=2, blank=True, null=True)
    checkresult = models.CharField(max_length=1, blank=True, null=True)
    infoatcode = models.CharField(max_length=20, blank=True, null=True)
    solvingstyle = models.CharField(max_length=50, blank=True, null=True)
    manyitype = models.FloatField(blank=True, null=True)
    isqiangdu = models.FloatField(blank=True, null=True)
    huifustyle = models.CharField(max_length=50, blank=True, null=True)
    isbackauthority = models.FloatField(blank=True, null=True)
    isnt = models.FloatField(blank=True, null=True)
    deptbackcheckpass = models.FloatField(blank=True, null=True)
    facilitytype = models.FloatField(blank=True, null=True)
    firstcontacttime = models.DateField(blank=True, null=True)
    lasttakecasetime = models.DateField(blank=True, null=True)
    lastbackcasetime = models.DateField(blank=True, null=True)
    solvingdisreason = models.CharField(max_length=10, blank=True, null=True)
    rejectbcode = models.CharField(max_length=20, blank=True, null=True)
    rejectscode = models.CharField(max_length=20, blank=True, null=True)
    facttype = models.FloatField(blank=True, null=True)
    factnote = models.CharField(max_length=2000, blank=True, null=True)
    scenetype = models.FloatField(blank=True, null=True)
    appealtype = models.FloatField(blank=True, null=True)
    appealnote = models.CharField(max_length=2000, blank=True, null=True)
    replynote = models.CharField(max_length=2000, blank=True, null=True)
    isopen = models.FloatField(blank=True, null=True)
    noncontactreason = models.CharField(max_length=50, blank=True, null=True)
    iscontact = models.FloatField(blank=True, null=True)
    replytime = models.DateField(blank=True, null=True)
    greenresptype = models.CharField(max_length=20, blank=True, null=True)
    greenresptypecode = models.CharField(max_length=20, blank=True, null=True)
    contactperson = models.CharField(max_length=20, blank=True, null=True)
    platformstatus = models.FloatField(blank=True, null=True)
    isverifyauthority = models.FloatField(blank=True, null=True)
    citizen_feedbacknote = models.CharField(max_length=500, blank=True, null=True)
    islastexecutedpet = models.FloatField(blank=True, null=True)
    visitcount = models.FloatField(blank=True, null=True)
    statisticaldeptcode = models.CharField(max_length=10, blank=True, null=True)
    surveytime = models.DateField(blank=True, null=True)
    surveycontactinfo = models.CharField(max_length=50, blank=True, null=True)
    lssueleaders = models.CharField(max_length=200, blank=True, null=True)
    cfperson = models.CharField(max_length=200, blank=True, null=True)
    cjperson = models.CharField(max_length=200, blank=True, null=True)
    isfallback = models.FloatField(blank=True, null=True)
    factconfirm = models.CharField(max_length=20, blank=True, null=True)
    executedepttype = models.FloatField(blank=True, null=True)
    isallowend = models.FloatField(blank=True, null=True)
    lastcontacttime = models.DateField(blank=True, null=True)
    firstcontacttype = models.CharField(max_length=20, blank=True, null=True)
    keepersn = models.CharField(max_length=100, blank=True, null=True)
    solvekeepersn = models.CharField(max_length=20, blank=True, null=True)
    enterpriseinvoled = models.FloatField(blank=True, null=True)
    enterpriseinvoledname = models.CharField(max_length=100, blank=True, null=True)
    areahandleresult = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_INFO_SOLVING'