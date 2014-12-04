from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse


# Create your models here.
class Gift(models.Model):
	user=models.ForeignKey(User)
	short_name = models.CharField(max_length=250)
	description = models.CharField(max_length=500,default='')
	link=models.CharField(max_length=600, default='',blank=True)
	gifted=models.BooleanField(default=False)
	rank=models.IntegerField(default=0)
	slug = models.SlugField(unique=True)


	def save(self, *args, **kwargs):
		self.slug = slugify(self.short_name)
		super(Gift, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.short_name

	def get_absolute_url(self):
		return reverse('gift_detail',kwargs={'user_name':self.user.username,'gift_name':self.slug})

class  UserInfo(models.Model):
	user=models.OneToOneField(User, related_name="info")
	address_city = models.CharField(max_length=200,null=True)
	address_state = models.CharField(max_length=2,null=True)
	address_street = models.CharField(max_length=200,null=True)
	address_zip = models.IntegerField(max_length=5,null=True)

	def get_absolute_url(self):
		return reverse('detail',kwargs={'user_name':self.user.username})
	#santa_to = models.OneToOneField(User, related_name="santa")
