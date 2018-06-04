# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class TInsCaseMain(models.Model):
    id = models.BigIntegerField(primary_key=True)
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
    deptcode = models.CharField(max_length=20, blank=True, null=True)
    fromusername = models.CharField(max_length=100, blank=True, null=True)
    isrediscuss = models.CharField(max_length=10, blank=True, null=True)
    isintervened = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T_INS_CASE_MAIN'
