from django.db import models


# Create your models here.
class Staff(models.Model):
	name = models.CharField(max_length=35)
	position = models.CharField(max_length=45)
	staff_img = models.FileField()
	staff_desc = models.TextField()

	def __str__(self):
		return self.name


