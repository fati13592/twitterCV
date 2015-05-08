from django.db import models

class Product(models.Model):
	barcode = models.CharField(max_length=50)
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Review(models.Model):
	product = models.ForeignKey(Product)
	title = models.CharField(max_length=100)
	text = models.CharField(max_length=500)

	def __unicode__(self):
		return self.title
