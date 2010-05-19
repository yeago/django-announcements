def announcements(request):
	if hasattr(request,'_announcements'):
		return {'announcements': request._announcements}
