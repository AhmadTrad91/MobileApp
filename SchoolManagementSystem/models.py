# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Agenda(models.Model):
    agendaid = models.AutoField(db_column='AgendaID', primary_key=True)  # Field name made lowercase.
    sectionid = models.ForeignKey('Section', models.DO_NOTHING, db_column='SectionID')  # Field name made lowercase.
    courseid = models.ForeignKey('Course', models.DO_NOTHING, db_column='CourseID')  # Field name made lowercase.
    agendadate = models.DateField(db_column='AgendaDate')  # Field name made lowercase.
    agendadescription = models.TextField(db_column='AgendaDescription')  # Field name made lowercase.
    isquiz = models.IntegerField(db_column='IsQuiz')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Agenda'
        unique_together = (('sectionid', 'courseid', 'agendadate'),)


class Classes(models.Model):
    classid = models.AutoField(db_column='ClassID', primary_key=True)  # Field name made lowercase.
    classcode = models.CharField(db_column='ClassCode', max_length=20)  # Field name made lowercase.
    classname = models.CharField(db_column='ClassName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Classes'


class Course(models.Model):
    courseid = models.AutoField(db_column='CourseID', primary_key=True)  # Field name made lowercase.
    coursecode = models.CharField(db_column='CourseCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    coursename = models.CharField(db_column='CourseName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Course'


class Notifications(models.Model):
    notificationid = models.AutoField(db_column='NotificationID', primary_key=True)  # Field name made lowercase.
    notificationdescription = models.TextField(db_column='NotificationDescription')  # Field name made lowercase.
    notificationdate = models.DateField(db_column='NotificationDate')  # Field name made lowercase.
    isnotified = models.IntegerField(db_column='IsNotified')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notifications'


class Section(models.Model):
    sectionid = models.AutoField(db_column='SectionID', primary_key=True)  # Field name made lowercase.
    classid = models.ForeignKey(Classes, models.DO_NOTHING, db_column='ClassID')  # Field name made lowercase.
    sectioncode = models.CharField(db_column='SectionCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sectionname = models.CharField(db_column='SectionName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Section'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
