import datetime

from django.conf import settings
from django.db.models import Q

from announcements import models as amodels
from announcements.cookie import get_cookie_varname, decode_cookie

class AnnouncementMiddleware(object):
	def process_request(self, request):
		path = request.path
		if not path.startswith('/'):
			path = "/" + path

		acknowledged_announcements = []

		announcements = amodels.Announcement.objects.filter(\
			Q(url__isnull=True)|Q(url__exact=path)).filter(\
			Q(start_time__isnull=True)|Q(start_time__lte=datetime.datetime.now())).filter(\
			Q(expire_time__isnull=True)|Q(expire_time__gte=datetime.datetime.now()))

		if not request.user.is_authenticated():
			announcements = announcements.exclude(auth_only=True)
			acknowledged_announcements.extend(decode_cookie(request.COOKIES))

		else:
			announcements = announcements.exclude(auth_acknowledgments=request.user)
			acknowledged_announcements.extend(request.user.announcement_set.values_list('pk',flat=True).distinct())

		announcements = announcements.exclude(Q(acknowledge=True)&Q(pk__in=acknowledged_announcements))

		request._announcements =  announcements
