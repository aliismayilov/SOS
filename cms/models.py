from django.db import models

class Language(models.Model):
	small_name = models.CharField(max_length=3)
	long_name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.small_name

class Page(models.Model):
	language = models.ForeignKey('Language')
	
	title = models.CharField(max_length=50)
	slug = models.SlugField()
	body = models.TextField()

	# optional fields
	parent = models.ForeignKey('self', blank=True, null=True)
	priority = models.IntegerField(blank=True, null=True)

	def __unicode__(self):
		return self.title

class Entry(models.Model):
	language = models.ForeignKey('Language')

	title = models.CharField(max_length=50)
	slug = models.SlugField()
	body = models.TextField()

	date_published = models.DateTimeField()

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural = "entries"