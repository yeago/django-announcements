from django.conf.urls.defaults import *

urlpatterns = patterns('announcements.views',
	url(r'^(?P<id>[^/]+)/acknowledge/','acknowledge',name="announcement_acknowledge"),
)
