from django.contrib import admin
from announcements import models as amodels

def sites(val):
	return ", ".join(val.sites.values_list('name',flat=True).distinct())

class AnnouncementAdmin(admin.ModelAdmin):
	list_display = ['url','start_time','expire_time','acknowledge','auth_only',sites,'domain_insensitive']

admin.site.register(amodels.Announcement,AnnouncementAdmin)
