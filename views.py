from django.shortcuts import get_object_or_404, redirect

from announcements import models as amodels

def acknowledge(request,id,return_url=None):
	announcement = get_object_or_404(amodels.Announcement,pk=id)
	return_url = request.GET.get('return_url') or return_url or '/'
	return redirect(return_url)
