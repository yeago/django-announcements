from django.db import models

class SiteMessage(models.Model):
	sites = models.ManyToManyField('sites.Site',blank=True,help_text="If left blank, will always use current site")
	domain_insensitive = models.BooleanField(default=True,help_text="Will display across all domains")
	url = models.CharField(max_length=255,blank=True,null=True,help_text="Absolute URL to display message (include leading slash). Leave blank for all")
	start_time = models.DateTimeField(null=True,blank=True,help_text="For scheduling in the future")
	expire_time = models.DateTimeField(null=True,blank=True)
	acknowledge = models.BooleanField(verbose_name="Needs acknowledgment",\
		help_text="Will remain until the user waives the message away. Otherwise, its 'sticky'",default=False)
	auth_only = models.BooleanField(verbose_name="Authenticated users only",default=False)
	body = models.TextField()

	# Below field provides better acknowledgment support for auth users
	auth_acknowledgments = models.ManyToManyField('auth.User',blank=True,editable=False)