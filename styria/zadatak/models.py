from django.db import models

# Create your models here.
class Url(models.Model):
	url_data = models.URLField(max_length=400)
	status = models.BooleanField(default=False)
	def __unicode__(self):
		return self.url_data

class Words(models.Model):
	url = models.ForeignKey(Url)
	word = models.CharField(max_length=100, primary_key=True)
	def __unicode__(self):
		return self.word

class WordCount(models.Model):
	url = models.ForeignKey(Url)
	word = models.ForeignKey(Words)
	total = models.IntegerField(default=0)
	def __unicode__(self):
		return self.word
	def count(self):
		return self.total