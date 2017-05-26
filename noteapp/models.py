from django.db import models
from django.utils import timezone

class Subject(models.Model):
	title=models.CharField(max_length=100, null=True)
	abbrev=models.CharField(max_length=20, default='TBA')

	def __str__(self):
		return self.title

class Note(models.Model):
	subj=models.ForeignKey(Subject, default=1)
	abbr=models.CharField(max_length=100, null=True)
	title=  models.CharField(max_length=100)
	topics= models.TextField()
	author= models.ForeignKey('auth.User')	
	srcfile= models.CharField(max_length=200, null=True)
	created_date= models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True , null=True)
	
	
	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title


class Branch(models.Model):
	branchname=models.CharField(max_length=100, null=True)
	branch_short=models.CharField(max_length=100,null=True)
	included_subjects=models.ManyToManyField(Subject)
	non= models.IntegerField(null=True)
	nos= models.IntegerField(null=True)
	


	def __str__(self):
		return self.branchname	