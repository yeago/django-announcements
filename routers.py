from django.conf import settings

"""
This router is useful for setups where your messages need to go out to
several different projects using several different databases.

One snag in using this is that the User<->Announcement acknowledgment
table won't work anymore, so you will have to rely entirely on cookie-
based acknowledgments.
"""

class AnnouncementsRouter(object):
	def db_for_read(self, model,  **hints):
		if model._meta.app_label == "announcements":
			return getattr(settings,"ANNOUNCEMENTS_DBNAME","announcements")
		return None

	def db_for_write(self, model, **hints):
		if model._meta.app_label == "announcements":
			return getattr(settings,"ANNOUNCEMENTS_DBNAME","announcements")
		return None

	def allow_syncdb(self, db, model):
		if db == getattr(settings,"ANNOUNCEMENTS_DBNAME","announcements"):
			return model._meta.app_label == "announcements"

		elif model._meta.app_label == "announcements":
			return False

		return None
