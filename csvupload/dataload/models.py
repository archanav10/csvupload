from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Project(models.Model):
    project_id = models.IntegerField(primary_key=True)
    project_name = models.CharField(max_length=50)
    project_description = models.CharField(max_length=200, blank=True, null=True)
    project_address = models.CharField(max_length=100, blank=True, null=True)
    project_city = models.CharField(max_length=50, blank=True, null=True)
    project_pincode = models.CharField(max_length=10, blank=True, null=True)
    project_status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'project'
        managed = True



class Facility(models.Model):
    facility_id = models.IntegerField(primary_key=True)
    facility_name = models.CharField(max_length=50)
    facility_description = models.CharField(max_length=100, blank=True, null=True)
    project = models.ForeignKey('Project', models.DO_NOTHING, null=True)
    locked_for_edit = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'facility'
        managed = True



class Zone(models.Model):
    zone_id = models.AutoField(primary_key=True)
    zone_name = models.CharField(max_length=20)
    zone_description = models.CharField(max_length=100, blank=True, null=True)
    facility = models.ForeignKey(Facility, models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'zone'
        managed = True
