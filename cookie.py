from django.conf import settings

def get_cookie_varname():
	return getattr(settings,"ANNOUNCEMENT_COOKIE_VARNAME","announcements")

def decode_cookie(cookie_dict):
	pks = []
	if get_cookie_varname() in cookie_dict:
		for i in cookie_dict[get_cookie_varname()].split(","):
			try:
				pks.append(int(i))
			except ValueError:
				pass

	return pks
