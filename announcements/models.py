from django.db import models

class Announcement(models.Model):
	url = models.CharField(max_length=255,blank=True,null=True,help_text="Absolute URL to display message (include leading slash). Leave blank for all")
	start_time = models.DateTimeField(null=True,blank=True,help_text="For scheduling in the future")
	expire_time = models.DateTimeField(null=True,blank=True,help_text="Its a *VERY* good idea to use this.")
	body = models.TextField()
	message_level = models.CharField(max_length=20,choices=[],help_text="Borrowed from the messages framework")
	sites = models.ManyToManyField('sites.Site',blank=True,help_text="If left blank, will always use current site")
	acknowledge = models.BooleanField(verbose_name="Needs acknowledgment",\
		help_text="Will remain until the user waives the message away. Otherwise, its 'sticky'",default=False)
	auth_only = models.BooleanField(verbose_name="Authenticated users only",default=False)

	"""
	Below field provides better acknowledgment support for auth users.
	This can be overridden by settings ANNOUNCEMENT_FOREGO_USERTABLE = True

	One might not want to use this in situations where this announcement app 
	is kept in a separate db and serves multiple projects with different 
	databases. An FK link to the table makes no sense in this case.
	"""
	auth_acknowledgments = models.ManyToManyField('auth.User',blank=True,editable=False)
	def save(self,*args,**kwargs):
		if self.url == '':
			self.url = None

		super(Announcement,self).save(*args,**kwargs)
