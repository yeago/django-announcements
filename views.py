from django.conf import settings
from django.shortcuts import get_object_or_404, redirect

from announcements import models as amodels

def acknowledge(request,id,return_url=None):
	announcement = get_object_or_404(amodels.Announcement,pk=id)

	if request.user.is_authenticated():
		use_auth = True

		for i in getattr(settings,"DATABASE_ROUTERS") or []:
			if "AnnouncementRouter" in i:
				use_auth = False
				break

		if use_auth:
			announcement.auth_acknowledgments.add(request.user)

		# TODO: set cookie acknowledgement

	return_url = request.GET.get('return_url') or return_url or '/'
	return redirect(return_url)
