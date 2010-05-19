from django.contrib import admin
from django.contrib import messages
from django.contrib.messages.utils import get_level_tags
from django import forms

from announcements import models as amodels

def sites(val):
	return ", ".join(val.sites.values_list('name',flat=True).distinct())

class AnnouncementAdminForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(AnnouncementAdminForm,self).__init__(*args,**kwargs)
		level_tags = get_level_tags().values()
		choices = [(x,x) for x in level_tags]
		self.fields['message_level']  = forms.ChoiceField(choices=choices)

	class Meta:
		model = amodels.Announcement

class AnnouncementAdmin(admin.ModelAdmin):
	list_display = ['url','message_level','start_time','expire_time','acknowledge','auth_only',sites]
	form = AnnouncementAdminForm

admin.site.register(amodels.Announcement,AnnouncementAdmin)
