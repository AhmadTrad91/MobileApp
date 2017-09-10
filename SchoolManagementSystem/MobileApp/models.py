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

