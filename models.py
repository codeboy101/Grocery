from django.db import models

class List(models.Model):
	item_name = models.CharField(max_length=200)
	item_price = models.IntegerField(default=0)
	
	def __str__(self):
		return self.item_name
