from django.db import models

#Create your models here.
class Subscriber(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=128)

	def __str__(self):
		return 'Користувач: %s;    %s' % (self.name, self.email)

	class Meta:
		verbose_name = 'Підписник'
		verbose_name_plural = 'Підписники'