# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class TClassinfo(models.Model):
    id = models.FloatField()
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
