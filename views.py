from django.conf import settings
from django.shortcuts import get_object_or_404, redirect

from announcements import models as amodels
from announcements.cookie import get_cookie_varname, decode_cookie

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

	return_url = request.GET.get('return_url') or return_url or '/'
	response = redirect(return_url)

	cookie_acknowledgments = [str(i) for i in decode_cookie(request.COOKIES)]
	cookie_acknowledgments.append(str(announcement.pk))
	response.set_cookie(get_cookie_varname(),",".join(cookie_acknowledgments))
	return response
