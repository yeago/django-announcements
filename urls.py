from django.conf.urls.defaults import *

urlpatterns = patterns('announcement.views',
	url(r'^(?P<id>[^/]+)/acknowledge/','acknowledge',name="announcement_acknowledge"),
)
