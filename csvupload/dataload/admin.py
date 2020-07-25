
from django.contrib import admin

from .models import Project, Facility, Zone;

# Register your models here.
admin.site.register(Project)
admin.site.register(Facility)
admin.site.register(Zone)

class ProjectAdmin(admin.ModelAdmin):
	list_display = ("project_id","project_name", "project_description")


class FacilityAdmin(admin.ModelAdmin):
	list_display = ("facility_id", "facility_name", "facility_description")


class ZoneAdmin(admin.ModelAdmin):
	list_display = ("zone_id","zone_name", "zone_description", "facility_id")