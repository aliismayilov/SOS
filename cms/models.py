from django.db import models

class Language(models.Model):
	small_name = models.CharField(max_length=3)
	long_name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.small_name

	def get_absolute_url(self):
		return '/%s' % self.small_name

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

	class Meta:
		ordering = ['priority']

	def get_absolute_url(self):
		return '/%s/%s.html' % (self.language, self.slug)

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
		ordering = ['-date_published']

	def get_absolute_url(self):
		return '/%s/%s/%s.html' % (
				self.language,
				self.date_published.strftime("%Y/%b/%d").lower(),
				self.slug,
			)